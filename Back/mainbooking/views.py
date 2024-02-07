from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import VisitorForm

def create_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            # Редірект або інші дії після успішного збереження
    else:
        form = VisitorForm()
    return render(request, 'new_visitor.html', {'form': form})
