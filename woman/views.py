from rest_framework import  generics
from django.shortcuts import render
from .models import Woman
from .serializers import WomanSerializer



class WomanAPIView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
