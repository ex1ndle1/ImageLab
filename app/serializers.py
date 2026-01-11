from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.ImageModel
        fields = ('id', 'title', 'image', 'category')


class UsersSerializer(serializers.ModelSerializer):
    avatar = ImageSerializer(read_only=True)
    age_status = serializers.SerializerMethodField()
    password_quality = serializers.SerializerMethodField()
    class Meta :
        model = models.User
        fields = ('id', 'username', 'age', 'avatar', 'age_status', 'password_quality')


    def get_age_status(self, obj):

        if obj.age < 18:
             return 'User not adult yet'
        return 'User is adult'

    def get_password_quality(self, obj):
        if len(obj.password) < 8:
            return 'Weak Password'
        print(obj.password)
        return 'Strong password'