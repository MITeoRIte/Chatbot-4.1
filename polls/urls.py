from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#perfected
    path('sendmail', views.sendmail),#perfected
    path('converse/',views.displaychatbot),
    path('converse/sendtochatterbot/',views.send_replyfromChatterbot),#perfected
    path('getmail/sendtochatterbot/', views.send_replyfromChatterbot),
    path('sendtochatterbot/', views.send_replyfromChatterbot),
    path('sendamail/', views.sendamail), #perfected
    path('getmail/getamail/', views.getamail), #perfected
    path('getmail/sendamail/', views.sendamail),
    path('getmail/', views.getmail), #perfected
    path('newgetmail/', views.newgetmail),
    path('newgetmail/getmail', views.getmail),
    path('newgetmail/automatedemailreplier', views.automatedemailreplier),

]
