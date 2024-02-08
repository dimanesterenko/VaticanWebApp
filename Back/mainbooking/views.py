
# Create your views here.
from django.shortcuts import render, redirect
from .forms import VisitorForm
from .models import Booking
def create_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.save()
            booking_data = {
                'Visitor_ID': visitor.pk,  # Отримуємо ID збереженого візітора
                'Responsible_ID': request.POST['responsible_id'],  # Отримуємо ID відповідальної особи з POST запиту
                'Guide_ID': request.POST['guide_id'],  # Отримуємо ID гіда з POST запиту
                'Booking_Count': int(request.POST['booking_count']),  # Отримуємо кількість з POST запиту
                'Booking_Date': request.POST['booking_date'],  # Отримуємо дату з POST запиту
                'Booking_Time': request.POST['booking_time'],  # Отримуємо час з POST запиту
            }
            booking = Booking(**booking_data)  # Створюємо об'єкт бронювання
            booking.save()  # Зберігаємо бронювання в БД

            # Після успішного збереження можна редіректити або робити інші дії
            return redirect('success_page')
            # Редірект або інші дії після успішного збереження
    else:
        form = VisitorForm()
    return render(request, 'new_visitor.html', {'form': form})
