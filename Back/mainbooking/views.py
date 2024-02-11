from datetime import datetime
from .models import Responsible
from django.db.models import Max
import random
from django.shortcuts import render, redirect
from .forms import VisitorForm, TicketForm
from .models import Visitor
from .models import Booking
def create_visitor(request):
    if request.method == 'POST':
        visitor_form = VisitorForm(request.POST, prefix='visitor')
        ticket_form = TicketForm(request.POST, prefix='ticket')
        if visitor_form.is_valid() and ticket_form.is_valid():
            visitor = visitor_form.save(commit=False)
            visitor_id = get_next_visitor_id()
            visitor.visitor_id = visitor_id
            visitor.save()

            ticket = ticket_form.save(commit=False)
            ticket.Visitor_ID_id = visitor_id
            ticket.save()
            responsible = Responsible.objects.order_by('?').first()

            booking = Booking(
                Visitor_ID_id=visitor_id,
                Responsible_ID_id=responsible.Responsible_ID if responsible else None,
                Guide_ID_id=random.randint(1,4),
                Booking_Count=1,
                Booking_Date=datetime.now().date(),
                Booking_Time=datetime.now().time(),
            )
            booking.save()
            return redirect('news')

    else:
        visitor_form = VisitorForm(prefix='visitor')
        ticket_form = TicketForm(prefix='ticket')
    return render(request, 'visitor_test.html', {'visitor_form': visitor_form, 'ticket_form': ticket_form})


def get_next_visitor_id():
    # Получаем максимальное значение Visitor_ID из базы данных
    max_visitor_id = Visitor.objects.aggregate(Max('Visitor_ID'))['Visitor_ID__max']

    # Если нет записей в базе данных, начинаем с 1, иначе увеличиваем максимальное значение на 1
    if max_visitor_id is None:
        return 1
    else:
        return max_visitor_id + 1