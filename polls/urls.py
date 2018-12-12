from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#perfected
    path('sendmail', views.sendmail),#perfected
    path('converse/',views.displaychatbot),
    path('converse/sendtochatterbot/',views.send_replyfromChatterbot),#perfected
    path('sendamail/', views.sendamail), #perfected
    path('getmail/getamail/', views.getamail), #perfected
    path('getmail/', views.getmail), #perfected
]
