from django.shortcuts import render, redirect
from django.views.generic import CreateView , ListView
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required   
from . import models
from rest_framework import generics , views , permissions , authentication
from . import serializers
from .permissions import IsNotExpired
from rest_framework.response import Response
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from django.core.paginator import Paginator
from django.core.cache import cache



class ImageDetailAPIView(generics.RetrieveAPIView):
    queryset = models.ImageModel.objects.all()
    serializer_class = serializers.ImageSerializer
    lookup_field = 'id'
    authentication_classes = [authentication.BasicAuthentication]


    def retrieve(self, request, *args, **kwargs):

        cache_key = f'image_detail_{kwargs.get('id')}'        
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, 128)
        
        return response


class PeopleListApiView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self , request  , *args , **kwargs):
        cache_key  = f'list_people_{request.get_full_path()}'
        cahced_data = cache.get(cache_key)
        if cahced_data:
             return Response(cahced_data)
        
        #####added for calling basic ListApi logic
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data)
        return response







def FBVListView(request):
    images = models.ImageModel.objects.order_by('id')
    paginator = Paginator(images, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj,'images':images , 'is_paginated': page_obj.has_other_pages(),'paginator': paginator })


#################################################CBV paginator view###################
class ImageListView(ListView):
    template_name = 'home.html'
    context_object_name = 'images'
    paginate_by = 1
    def get_queryset(self):
        return models.ImageModel.objects.order_by('id')
        
class CategoryAPIView(generics.ListAPIView):
    pass


class CategoryAPIView(generics.ListAPIView):
   pass

    
class LtsAPIView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
\
    def  get(self, request):
        return Response(f'hi {request.user.username}')
    
class CreateAPI(generics.views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
     
    def post(self ,  request : Request):
        user = request.user
        Token.objects.create(user=user)
        return Response('SUCCESSFULLY CREATED')

class LogoutView(generics.views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication , authentication.BasicAuthentication]
    def post(self ,  request : Request ):
        if request.user:
         user = request.user
         token = Token.objects.get(user = user )
         token.delete()
         return Response('successfully loged out')
        return Response('Token is not valid')
    



def upload_image_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:home') 
    else:
        form = ImageUploadForm()
    return render(request, 'crud/create.html', {'form': form})




