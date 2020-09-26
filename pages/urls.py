from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'is_front_page': True}, name='home'),
    path('<str:slug>', views.index, name='index'),
]


