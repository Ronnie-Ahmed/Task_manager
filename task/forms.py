from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput
from django.forms import DateTimeInput

from .models import Task,Review,ImageModel

class TaskForm(ModelForm):
    class Meta:
        model=Task
        # fields=['title','description','complete']
        fields='__all__'
        exclude=['creation_date','user']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'date'}),
        }
       
        
class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        exclude = ['user']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class LoginForms(AuthenticationForm):
    username=forms.CharField(widget=TextInput)
    password=forms.CharField(widget=PasswordInput)
    
class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageModel
        fields='__all__'
        exclude=['task_id']
        