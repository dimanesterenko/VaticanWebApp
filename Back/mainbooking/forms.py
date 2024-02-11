from django import forms
from .models import Visitor
from .models import Ticket
class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['Visitor_Name', 'Visitor_Mail', 'Visitor_Tel', 'Visitor_Card']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['Ticket_Guide', 'Ticket_Type', 'Ticket_Date', 'Ticket_Count','Ticket_Time' ]
    Ticket_Date = forms.DateField(widget=forms.SelectDateWidget())

    def save(self, commit=True):
        ticket = super().save(commit=False)
        ticket.calculate_price()
        if commit:
            ticket.save()
        return ticket
