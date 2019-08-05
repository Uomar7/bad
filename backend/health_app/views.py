from .serializers import OriginalSerializer, ProfileSerializer, ExtractedSerializer, UserSerializer
from .forms import NewProfileForm, NewOriginalForm, Extracted_data
from .models import Profile, Extracted_data, Original_image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db import transaction
from rest_framework import status
from .blob import blobScan

# @login_required(login_url='/accounts/login/')


def welcome(request):

    return render(request, 'index.html')

# * ---------------------------EDIT PROFILE------------------------------
@login_required(login_url='/accounts/login/')
@transaction.atomic
def new_profile(request):
    user = request.user
    current_user = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES,
                              instance=current_user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm(instance=current_user)
    return render(request, 'new-profile.html', {"form": form, "user": user})

# * ----------------------------PROFILE----------------------------------
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm(instance=profile)

    return render(request, 'profile-page.html', {"profile": profile, "form": form})

# ! view function to view different forms and add a form or scan a form.


def scan(request):
    # dict = {'23.51547': 'male', '388.3149': 'first visit'

    #         }
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    forms = Original_image.objects.all()
    im=forms[2]
    image = im.image.url
    image= image[1:]
    # s=str(image)
    print("no")
    # print(image[1:])
    pts = blobScan(image)
    print(pts)
    # di=[]
    # for k, v in dict.items():
    #     for i in range(len(pts)):
    #         for j in range(len(pts[0])):
    #             ind = 0
    #             if int(float(pts[i][j])) == int(float(k)):
    #                 st = str(pts[i][j])
    #                 di.append(dict.get(st))
    #             else:
    #                 ind += 1

    # for k,v in dict.items():
    # 	for i in range(len(pts)):
    # 		for j in range(len(pts[0])):
    # 			ind=0
    # 			if int(float(pts[i][j]))==int(float(k)):
    # 				st = str(pts[i][j])
    # 				print(dict.get(st))
    # 				ind += 1
    # 			else :
    # 				ind+=1

    if request.method == 'POST':
        form = NewOriginalForm(request.POST, request.FILES)
        if form.is_valid():
            # image = form.cleaned_data['image']
            # pts = blobScan(image)
            # di=[]
            # for k, v in dict.items():
            #     for i in range(len(pts)):
            #         for j in range(len(pts[0])):
            #             ind = 0
            #             if int(float(pts[i][j])) == int(float(k)):
            #                 st = str(pts[i][j])
            #                 ren = di.append(dict.get(st))
            #             else:
            #                 ind += 1
            if Original_image.objects.filter(sickness_form__icontains=form.cleaned_data['sickness_form']):
                error = 'Form already exists'
            else:
                new = form.save(commit=False)
                new.posted_by = profile
                new.save()

                return redirect('scan')
    else:
        form = NewOriginalForm()
    return render(request, 'scan.html', {'profile': profile, 'form': form, 'forms': forms, 'pts':pts})


def delete_item(request, image_id):
    # current_user = request.user
    # item = Original_image.objects.get(id =image_id)
    if request.user:
        Original_image.objects.get(id=image_id).delete()

    return redirect('scan')


# ! ------------------------END VIEWS---------------------------------
# * serializing the Django User model
class UserList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    # * api for getting all users
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)

    # * creating new user api
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
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class OriginalList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_originals = Original_image.objects.all()
        serializers = OriginalSerializer(all_originals, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = OriginalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtractedList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_extracts = Extracted_data.objects.all()
        serializers = ExtractedSerializer(all_extracts, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ExtractedSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# * Descriptions for all objects


class ProfileDescr(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_prof(self, pk):
        try:
            prof = Profile.objects.get(pk=pk)
            return prof

        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
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
        prof = self.get_prof(pk)
        prof.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OriginalDescr(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_original(self, pk):
        try:
            original = Original_image.objects.get(pk=pk)
            return original

        except Original_image.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
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
        original = self.get_original(pk)
        original.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExtractDescr(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_extract(self, pk):
        try:
            extract = Extracted_data.objects.get(pk=pk)
            return extract

        except Extracted_data.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
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
        extract = self.get_extract(pk)
        extract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
