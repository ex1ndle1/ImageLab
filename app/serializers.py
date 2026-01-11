from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.ImageModel
        fields = ('id', 'title', 'image', 'category')


class UsersSerializer(serializers.ModelSerializer):
    avatar = ImageSerializer(read_only=True)
    class Meta :
        model = models.User
        fields = ('id', 'username', 'age', 'avatar')
