from django.urls import path
from .views import  show,add,edit,delete,Post_Detail

urlpatterns=[

    path('',show.as_view(),name="show"),
    path('edit/<int:pk>/',edit.as_view(),name='post-edit'),
    path('delete/<int:pk>/',delete.as_view(),name='post-delete'),
    path('add/',add.as_view(),name='post-add'),
    path('post-details/<int:pk>/',Post_Detail.as_view(),name='post-detail'),




]