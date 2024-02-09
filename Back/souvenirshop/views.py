from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Souvenir
from .serializers import SouvenirSerializer

class SouvenirViewSet(viewsets.ModelViewSet):
    queryset = Souvenir.objects.all()
    serializer_class = SouvenirSerializer


def souvenirs_shop(request):
    souvenirs = Souvenir.objects.all()
    return render(request, 'souvenirs.html', {'souvenirs': souvenirs})
