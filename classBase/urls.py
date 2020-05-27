from django.urls import path
from classBase.views import cbview,CbView,Post_Table
from django.views.generic import TemplateView
from classBase.views import View_based

urlpatterns=[
    path('cbview/',TemplateView.as_view(template_name='cbview.html')),
    path("CbView",CbView.as_view()),
    path("Table/",Post_Table.as_view()),
    path("View_based",View_based.as_view()),
]