from django.shortcuts import render, redirect
from django.views.generic import CreateView , ListView
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required   
from . import models
from rest_framework import generics , views , permissions , authentication
from .serializers import UsersSerializer
from .permissions import IsNotExpired
from rest_framework.response import Response
# from django.contrib.a
# Create your views here.

class LtsAPIView(generics.views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def  get(self, request):
        return Response(f'hi {request.user.username}')

class PeopleListApiView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsNotExpired]
    

class ImageListView(ListView):
    template_name = 'home.html'
    context_object_name = 'images'
    def get_queryset(self):
        return models.ImageModel.objects.order_by('id')
        


def upload_image_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:home') 
    else:
        form = ImageUploadForm()
    return render(request, 'crud/create.html', {'form': form})
