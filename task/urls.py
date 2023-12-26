from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('login/',views.LoginPage,name='Login'),
    path('register/',views.CreateUser,name='Register'),
    path('create/',views.CreateTask,name='CreateTask'),
    path('review/',views.CreateReview,name='CreateReview'),
    path('update/<str:pk>/',views.UpdateTask,name='UpdateTask'),
    path('delete/<str:pk>/',views.DeleteTask,name='DeleteTask'),
    path('ViewTask/<str:pk>/',views.ViewTask,name='ViewTask'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('filter_tasks/',views.filter_tasks,name='filter_tasks'),
    path('search_tasks/',views.search_tasks,name='search_tasks'),
    path('apiview/',views.TaskModelAPIView.as_view(),name='apiview'),
    path('apiview/<int:pk>',views.TaskApiVIew.as_view(),name='apiview'),
    path('api/',views.TaskGenericsAPIView.as_view(),name='genericview'),
    path('api/<int:pk>',views.TaskModelDetailAPIView.as_view(),name='genericviewItem'),
    # path('photo/<int:pk>',views.ImageModelAPIView.as_view(),name='photo')
    path('ImageDelete/<str:pk>',views.ImageDelete,name='ImageDelete')
]


