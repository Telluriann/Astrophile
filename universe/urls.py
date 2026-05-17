from django.urls import path
from . import views

app_name = 'universe'

urlpatterns = [
    path('', views.index, name='index'),
    path('object/<slug:slug>/', views.detail, name='detail'),
]
