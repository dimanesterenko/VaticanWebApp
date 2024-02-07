from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['Visitor_ID', 'Visitor_Name', 'Visitor_Mail', 'Visitor_Tel', 'Visitor_Card']
