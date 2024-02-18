from django.shortcuts import render

def main_page(request):
    return render(request, 'main.html')

def visit_page(request):
    return render(request, 'visit_page.html')

def about_page(request):
    return render(request, 'about_page.html')

