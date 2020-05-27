from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from .serializers import PostSerializers,UserSerializer,CategorySerializer
from posts.models import Posts,Category
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly,IsOwnerIsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse





class PostView(APIView):
    def get(self, request, format=None):
        posts = Posts.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PostDetails(APIView):
    def get_object(self,pk):
        try:
            return Posts.objects.get(id=pk)
        except Posts.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        post=self.get_object(pk)
        serializer=PostSerializers(post)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        post=self.get_object(pk)
        serializer=PostSerializers(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        post=self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PostListCreate(generics.ListCreateAPIView):
    queryset=Posts.objects.all()
    serializer_class=PostSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Posts.objects.all()
    serializer_class=PostSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerIsAdminOrReadOnly]



class UserList(generics.ListAPIView):
    
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAdminUser]

class UserDetails(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAdminUser]




class CategoryList(generics.ListAPIView):
    
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAdminUser]



class CategoryCreate(generics.ListCreateAPIView):
    
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAdminUser]


class CategoryDetails(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAdminUser]



class ApiRoot(APIView):

    def get(self,request,format=None):
        return Response({
            'users':reverse('users',request=request,format=format),
            'categories':reverse('categories',request=request,format=format),
            'posts':reverse('posts',request=request,format=format),
            'admin_category':reverse('admin-category',request=request,format=format),
        })
    


    



