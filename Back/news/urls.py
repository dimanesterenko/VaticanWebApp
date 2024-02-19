from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsView
from news import views
router = DefaultRouter()
router.register(r'restnews', NewsView)

urlpatterns = [
    path('', include(router.urls)),
    path('newslist/',views.news_list, name='news'),
    path('newslist/news_detail/<int:pk>/', views.news_detai, name='news_detail')

]