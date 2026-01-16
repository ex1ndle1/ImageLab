from django.contrib import admin
from django.urls import path 
from . import views
app_name = 'app'

urlpatterns = [
    path('' , views.ImageListView.as_view() , name='home'),
    path('create/' , views.upload_image_view , name='upload'),
   path('api/users/', views.PeopleListApiView.as_view(), name='api-users'),
   path('api/', views.LtsAPIView.as_view() , name='api')
]
