from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SouvenirViewSet
from souvenirshop import views
router = DefaultRouter()
router.register(r'souvenirs', SouvenirViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('shop/',views.souvenirs_shop, name='souvenirs_shop')
]