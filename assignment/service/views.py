from django.shortcuts import render
from rest_framework import viewsets
from service.serializer import PlansSerializer
from .models import Plans
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        print(kwargs['pk'])
        # print(Plans.objects.get(plan_id=kwargs['pk']))
        try:
            p = Plans.objects.get(plan_id=kwargs['pk'])
        except Plans.DoesNotExist:
            p = None
        
        if p:
            p.delete()
            print("destroy")
            return Response({"status":"Successfulyy Deleted"},status=202)
        else:
            return Response({"error":"No Plans Found"},status=status.HTTP_404_NOT_FOUND)
