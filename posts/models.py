from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.db.models.signals import pre_save,post_save




STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]



class Category(models.Model):
    title=models.CharField( max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 


    def natural_key(self):
        return [self.id ,self.title]
        

    class Meta:
        db_table="categories"
        verbose_name="Category"
        verbose_name_plural="Categories"
    



class Posts(models.Model):  
    
    title=models.CharField( max_length=250)
    content=models.TextField()
    user=models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE,default=1)
    
    thumbnail=models.FileField(upload_to="posts/",null=True)
    category=models.ManyToManyField(Category,related_name="categories")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.manager
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,default="d")
    
    def get_absolute_url(self):
        return reverse("post-detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.title
    

    __str__.short_description="Post Title"
    
    def show_thumbnail(self):
        return format_html('<img src="/static/%s" width="100" height="75" />'%self.thumbnail)
    def show_content(self):
        return format_html(self.content)
    show_content.short_description="Post Content"
    show_thumbnail.short_description="Post Thumbnail"
    title.short_description="Post Title"
    class Meta:
        db_table="posts"
        verbose_name="Post"
        verbose_name_plural="Posts"
    


class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['title','content','thumbnail','user','category']
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter post title length should be >10"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "user":forms.Select(attrs={"class":"forms-control"}),
            "category":forms.CheckboxSelectMultiple(attrs={"class":"forms-control"}),
            "thumbnail":forms.ClearableFileInput(attrs={'multiple': True}),
        }
    def clean(self):
        fields=self.cleaned_data
        keys=list(fields.keys())
        if(len(fields[keys[0]])<10):
            raise ValidationError(f"{keys[0]} have less then 10 valuse ")
        if(len(fields[keys[1]])<10):
            raise ValidationError(f"{keys[1]} have less then 10 valuse")

    
class Gallery(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    images=models.FileField(upload_to="posts/",blank=True,null=True)
    def __str__(self):
        return self.post.title
    class Meta:
        verbose_name="Gallery"
        verbose_name_plural="Galleries"

    
def before_category_save(sender,instance,**kwargs):
    print(f"Creating Category for {instance}")



def after_category_save(sender,instance,**kwargs):
    print(f"Instance is created {instance}")


pre_save.connect(before_category_save,sender=Category)
post_save.connect(after_category_save,sender=Category)