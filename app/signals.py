
from django.db.models.signals import post_delete
from django.dispatch import receiver
import cloudinary.uploader
from .models import ImageModel

@receiver(post_delete, sender=ImageModel)
def delete_image_from_cloudinary(sender, instance, **kwargs):
    
    if instance.image:
            file_path = instance.image.name
            import os
            public_id = os.path.splitext(file_path)[0]
            cloudinary.uploader.destroy(public_id)
            print(f"Удалено из Cloudinary: {public_id}")