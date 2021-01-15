from django.shortcuts import render
from rest_framework import viewsets
from service.serializer import PlansSerializer
from .models import Plans
from django.contrib.auth.models import User, Group
from rest_framework import permissions
# Create your views here.

class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all()
    print("inside view")
    serializer_class = PlansSerializer
    permission_classes = [permissions.IsAuthenticated]

