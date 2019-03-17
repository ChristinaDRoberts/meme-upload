from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MemeSerializer
from .models import Memes





class MemeViewSet(viewsets.ModelViewSet):

    serializer_class = MemeSerializer
    queryset = Memes.objects.all()



