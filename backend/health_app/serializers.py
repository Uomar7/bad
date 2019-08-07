from rest_framework import serializers
from .models import Profile, Original_image
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','first_name','last_name','gender', 'phone_number','position','bio','pic','work_id','hospital_name')

