from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.page_not_found, name='404'),
]