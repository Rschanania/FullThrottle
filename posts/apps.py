from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class PostsConfig(AppConfig):
    name = 'posts'
    verbose_name="Blog System "


class MyAdminConfig(AdminConfig):
    default_site = 'posts.admin.MyAdminSite'
    verbose_name = "KaamKr  Administration"

