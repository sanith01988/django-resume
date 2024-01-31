from django.urls import path,re_path
from . import views

urlpatterns = [re_path('^$',views.HomePageTemplateView.as_view(),name='HomePageTemplateView'),
               path('', views.contact_view, name='contact'),
               ]