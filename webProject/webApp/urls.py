from django.urls import path
from webApp import views


urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
]