from django.contrib import admin
from user.models import ActivityPeriod
# Register your models here.

from posts.admin import MyAdminSite
admin_site=MyAdminSite()
admin_site.register(ActivityPeriod)
