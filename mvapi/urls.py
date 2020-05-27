from django.urls import path,include
from .views import PostView,PostDetails,UserDetails,UserList,PostDetailsUpdate,PostListCreate,CategoryDetails,CategoryList,ApiRoot,CategoryCreate
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    path('',include('rest_framework.urls')),
    path('',ApiRoot.as_view(),name="root"),
    path('posts/',PostListCreate.as_view(),name="posts"),
    path('post/<int:pk>/',PostDetailsUpdate.as_view(),name="single-post"),
    path('users/',UserList.as_view(),name="users"),
    path('user/<int:pk>/',UserDetails.as_view(),name="single-user"),
    path('categories/',CategoryList.as_view(),name="categories"),
    path('category/<int:pk>/',CategoryDetails.as_view(),name="category"),
    path('admin/category/',CategoryCreate.as_view(),name="admin-category"),
    
]

urlpatterns=format_suffix_patterns(urlpatterns)