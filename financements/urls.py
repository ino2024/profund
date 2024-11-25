from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about, name='about'), 
    path('services/', views.services, name='services'), 
    path('formulaire/', views.formulaire, name='formulaire'), 
    path('contact/', views.contact, name='contact'), 
    path('confirmation/', views.confirmation, name='confirmation'), 
    path('mention/', views.mention, name='mention'),
    path('merci/', views.merci, name='merci'),
    path('envoyer_email_confirmation/', views.envoyer_email_confirmation, name='envoyer_email_confirmation'),
    
]

