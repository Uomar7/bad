from django.contrib import admin
from .models import Profile,Original_image, Extracted_data

admin.site.register(Profile)
admin.site.register(Original_image)
admin.site.register(Extracted_data)