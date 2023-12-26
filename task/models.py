from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    is_complete=models.BooleanField(default=False)
    creation_date=models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,null=True)
    
    def save(self, *args, **kwargs):
        # Set the creation_date to the current time in the 'Asia/Dhaka' timezone
        if not self.creation_date:
            self.creation_date = timezone.now() + timezone.timedelta(hours=6)  # UTC+6 for Bangladesh

        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    review_name=models.CharField(max_length=200)
    review_title=models.CharField(max_length=200)
    rating=models.IntegerField()
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.review_name


class ProfilePic(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True,blank=True,default='1.jpg')
    
    
class ImageModel(models.Model):
    task_id=models.ForeignKey(Task,on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='photos/')