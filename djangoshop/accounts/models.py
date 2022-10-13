from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)
    date_of_birth = models.DateField(blank = True, null = True)
    biography = models.TextField(blank = True)
    photo = models.ImageField(upload_to = "profile/%y/%m/%d", blank = True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile."

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
