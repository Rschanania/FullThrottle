from django.urls import path
from BRM import views

urlpatterns=[
    path('login/',views.login),
    path('logout/',views.logout),
    path('profile/',views.profile),
]