from django.db import models
from django.contrib.auth.models import User


class ActivityPeriod(models.Model):
    user=models.ForeignKey(User,related_name="activity",on_delete=models.CASCADE)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)
    

    def __str__(self):
        return f"{self.start_time} To  {self.end_time}"
