from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):


    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 30 )
    position = models.CharField(max_length = 50)
    bio = models.TextField(max_length=500, blank=True)
    pic = models.ImageField(upload_to = 'avatar/', blank=True, default='')
    work_id = models.CharField(max_length=30, blank=True)
    hospital_name = models.CharField(max_length = 54, null=True, blank=True)

    def __str__(self):
        return self.user

class Original_image(models.Model):
    image = models.ImageField(upload_to = 'forms/')
    sickness_form = models.CharField(max_length = 82)
    posted_by = models.ForeignKey(Profile, related_name='forms')

    def __str__(self):
        return self.sickness_form

class Extracted_data(models.Model):

    sickness_name = models.CharField(max_length = 60)
    age = models.IntegerField()
    contents = models.TextField()
    posted_by = models.ForeignKey(Profile)

    def __str__(self):
        return self.sickness_name




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()