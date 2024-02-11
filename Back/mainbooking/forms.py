from django import forms
from .models import Visitor
from .models import Ticket
class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['Visitor_Name', 'Visitor_Mail', 'Visitor_Tel', 'Visitor_Card']
        labels = {
            'Visitor_Name': 'Name',
            'Visitor_Mail': 'Email',
            'Visitor_Tel': 'Phone number',
            'Visitor_Card': 'Card Number'
        }
        placeholders = {
            'Visitor_Name': 'Enter your name',
            'Visitor_Mail': 'Enter your email',
            'Visitor_Tel': 'Enter your phone number',
            'Visitor_Card': 'Enter your card number'
        }

    def __init__(self, *args, **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = self.Meta.placeholders.get(field, '')

class LimitedTimeWidget(forms.TimeInput):
    def __init__(self, attrs=None):
        default_attrs = {'type': 'time', 'min': '09:00', 'max': '18:00'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['Ticket_Type', 'Ticket_Date', 'Ticket_Count','Ticket_Time',]
    Ticket_Date = forms.DateField(widget=forms.SelectDateWidget())
    # Ticket_Time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    Ticket_Time = forms.TimeField(widget=LimitedTimeWidget)




    def save(self, commit=True):
        ticket = super().save(commit=False)
        ticket.calculate_price()
        if commit:
            ticket.save()
        return ticket
