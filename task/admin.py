from django.contrib import admin
from .models import Task,Review,ProfilePic,ImageModel

# Register your models here.
admin.site.register(Task)
admin.site.register(Review)
admin.site.register(ProfilePic)
admin.site.register(ImageModel)

