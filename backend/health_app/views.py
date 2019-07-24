from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .models import Profile, Extracted_data, Original_image 
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OriginalSerializer,ProfileSerializer, ExtractedSerializer,UserSerializer
from .permissions import IsAdminOrReadOnly

# * serializing the Django User model
class UserList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    #* api for getting all users
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)
    
    #* creating new user api
    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# * serializing the Profile objects
class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    # * creating api to get all profile objects as json
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
    
    # * function to add a new object in the models via the API
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class OriginalList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_originals = Original_image.objects.all()
        serializers = OriginalSerializer(all_originals,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = OriginalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)   

class ExtractedList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format=None):
        all_extracts = Extracted_data.objects.all()
        serializers = ExtractedSerializer(all_extracts,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ExtractedSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

# * Descriptions for all objects
class ProfileDescr(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_prof(self,pk):
        try:
            prof = Profile.objects.get(pk=pk)
            return prof

        except Profile.DoesNotExist:
            return Http404
    
    def get(self, request, pk , format=None):
        profile = self.get_prof(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        prof = self.get_prof(pk)
        serializers = ProfileSerializer(prof, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        prof =self.get_prof(pk)
        prof.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class OriginalDescr(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_original(self,pk):
        try:
            original = Original_image.objects.get(pk=pk)
            return original

        except Original_image.DoesNotExist:
            return Http404
    
    def get(self, request, pk , format=None):
        orig = self.get_original(pk)
        serializers = OriginalSerializer(orig)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        original = self.get_original(pk)
        serializers = OriginalSerializer(original, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        original =self.get_original(pk)
        original.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ExtractDescr(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_extract(self,pk):
        try:
            extract = Extracted_data.objects.get(pk=pk)
            return extract

        except Extracted_data.DoesNotExist:
            return Http404
    
    def get(self, request, pk , format=None):
        extract = self.get_extract(pk)
        serializers = ExtractedSerializer(extract)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        extract = self.get_extract(pk)
        serializers = ExtractedSerializer(extract, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        extract =self.get_extract(pk)
        extract.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)