from django.db import models






class  ImageCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

# Create your models here.
class ImageModel(models.Model):
    title = models.CharField(max_length=100 )
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ImageCategory, related_name='images', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class User(models.Model):
    username = models.CharField(max_length=150, unique=True )
    age = models.IntegerField()
    
    def __str__(self):
        return self.username
    