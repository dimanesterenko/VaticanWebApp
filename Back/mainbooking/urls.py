from django.urls import path
from .views import create_visitor

urlpatterns = [
    path('create/', create_visitor, name='create_visitor'),
    # Додайте інші URL-шляхи за необхідності
]