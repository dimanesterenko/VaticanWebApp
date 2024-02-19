from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import News
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
class NewsView(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

def news_list(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})

def news_detai(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'new': new})
