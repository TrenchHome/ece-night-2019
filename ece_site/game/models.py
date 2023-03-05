from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, unique=True, null=False, 
        db_index=True, 
        on_delete=models.CASCADE,
        default=0,
    )
    username = models.TextField(max_length=15, default='')
    email = models.CharField(max_length=50)
    scores = models.IntegerField(default=0)

    @staticmethod
    def get_profile(user):
        try:
            profile = Profile.objects.get(user=user)
        except:
            profile = Profile.objects.create(user=user, email=user.email)
            profile.save()

        return profile
    
    def set_username(user, username):
        Profile.objects.filter(user=user).update(username=username)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-scores']
