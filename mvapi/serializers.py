from rest_framework import serializers
from posts.models import Posts,Category
from django.contrib.auth.models import User
from user.models import ActivityPeriod



class UserSerializer1(serializers.ModelSerializer):
    #posts=serializers.PrimaryKeyRelatedField(many=True,queryset=Posts.objects.all())#a user can create many posts so we use many=True
    activity=serializers.StringRelatedField(many=True)
    class Meta:
        model=User
        fields=[
            'id','username','activity',
        ]




class PostSerializers1(serializers.ModelSerializer):
    # user=serializers.ReadOnlyField(source='user.username')
   # category=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="category")
    #user=serializers.StringRelatedField(many=False)
    user=UserSerializer1(many=False,read_only=True)

    
    class Meta:
        model=Posts
        fields=[
            'id','title','content','user',
        ]





class CategorySerializer(serializers.ModelSerializer):
    posts=PostSerializers1(many=True,read_only=True,source="categories")
    class Meta:
        model=Category
        fields=[
            'id','title','posts'
        ]





class PostSerializers(serializers.ModelSerializer):
    # user=serializers.ReadOnlyField(source='user.username')
    category=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="category")
    user=serializers.StringRelatedField(many=False)
    
    class Meta:
        model=Posts
        fields=[
            'id','title','content','user','category',
        ]



class UserSerializer(serializers.ModelSerializer):
    posts=serializers.StringRelatedField(many=True)#a user can create many posts so we use many=True
    activity=serializers.StringRelatedField(many=True)
    class Meta:
        model=User
        fields=[
            'id','username','email','activity','posts',
        ]


