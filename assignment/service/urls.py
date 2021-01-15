from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from service import views
router = DefaultRouter()
router.register(r'plans', views.PlansViewSet)

urlpatterns = [
    path('', include(router.urls)),
]