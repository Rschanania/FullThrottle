from django.urls import path,include
from . import views


urlpatterns=[
    path('contact/',views.contact),
    path('members/',views.team,name="members"),
    path('member/cat/<int:cat_id>/team/<int:team_id>',views.member,name="member"),
    path('re/',views.re),
    path('hr/',views.Hr),
    path('about/',views.about),
]