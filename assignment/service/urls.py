from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from service import views
from django.views.generic.base import TemplateView
from django.conf.urls import url
router = DefaultRouter()



router.register(r'plans', views.PlansViewSet)
router.register(r'createuser',views.CustomUserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # url('view', TemplateView.as_view(template_name="index.html"), name="home")
]