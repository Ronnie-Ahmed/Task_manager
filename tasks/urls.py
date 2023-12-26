
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


# def LoginPage(request):
#     return render(request, 'login.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('task.urls')),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


