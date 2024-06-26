"""
URL configuration for Back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

import Back.views
from exhibits import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'exibits', views.ExhibitView, 'exibit')

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns = [
    path('', Back.views.main_page,name='main_page'),
    path('admin/', admin.site.urls),
    path('exibitions/', include(router.urls)),
    path('exhibitsview/', views.exhibit_list_html, name='exhibit_list'),
    path('exhibit_detail/<int:pk>/', views.exhibit_detail, name='exhibit_detail'),
    path('mainbooking/', include('mainbooking.urls')),
    path('souvenirshop/', include('souvenirshop.urls')),
    path('news/', include('news.urls')),
    path('about/',Back.views.about_page),
    path('visit/',Back.views.visit_page)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

