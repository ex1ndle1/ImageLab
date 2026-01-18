from django.contrib import admin
from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



app_name = 'app'

urlpatterns = [
    path('' , views.ImageListView.as_view() , name='home'),
    path('create/' , views.upload_image_view , name='upload'),
   path('api/users/', views.PeopleListApiView.as_view(), name='api-users'),
   path('api/', views.LtsAPIView.as_view() , name='api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/' , TokenVerifyView.as_view() , name='token_verify'),
    path('api/logout/', views.LogoutView.as_view() , name='logout')
]
