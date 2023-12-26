from rest_framework import serializers
from .models import Task,ImageModel

class TaskModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

class ImageModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=ImageModel
        fields='__all__'