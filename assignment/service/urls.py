from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from service import views
from django.views.generic.base import TemplateView
from django.conf.urls import url
router = DefaultRouter()



router.register(r'plans', views.PlansViewSet)
router.register(r'createuser',views.CustomUserViewSet)
# router.register(r'genericplans',views.Plans.getplans)
urlpatterns = [
    path('', include(router.urls)),
    path('login',views.userlogin),
    path('logout',views.userlogout),
    url('genericplans',views.PlansView.getplans)
    # url('view', TemplateView.as_view(template_name="plan.html"), name="home")
]