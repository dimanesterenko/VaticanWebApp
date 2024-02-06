# from django.shortcuts import render
#
# # Create your views here.
#
# from django.shortcuts import render
# from .models import Exhibit
#
# def exhibit_list(request):
#     exhibits = Exhibit.objects.all()
#     return render(request, 'exhibit_list.html', {'exhibits': exhibits})
#
#

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExibitSerializer
from .models import Exhibit
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
class ExhibitView(viewsets.ModelViewSet):
    serializer_class = ExibitSerializer
    queryset = Exhibit.objects.all()

def exhibit_list_html(request):
    exhibits = Exhibit.objects.all()
    return render(request, 'exhibit_list.html', {'exhibits': exhibits})


#
# def show_exhibit_photo(request, photo_name):
#     # Отримайте експонат за допомогою імені фотографії (photo_name)
#     exhibit = get_object_or_404(Exhibit, photo=photo_name)
#     photo_path = 'media/exhibit_photos/' + photo_name
#     with open(photo_path, 'rb') as photo_file:
#         return HttpResponse(photo_file.read(), content_type='image/jpg')
