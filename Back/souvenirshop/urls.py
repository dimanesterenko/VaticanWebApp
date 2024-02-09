from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SouvenirViewSet

router = DefaultRouter()
router.register(r'souvenirs', SouvenirViewSet)

urlpatterns = [
    path('', include(router.urls)),
]