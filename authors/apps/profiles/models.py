from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from authors.apps.authentication.models import User

UserModel = getattr(settings, "AUTH_USER_MODEL", User)


class Profile(models.Model):
    """
       Create a data model to hold more information,
       about our awesome users.
       It is through profiles that we get to know
       more about the name behind a user account.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    date_of_birth = models.DateField(_("Date"), blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, max_length=200, default="url")
    following = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


def user_post_save_receiver(instance, created, *args, **kwargs):
    """
    Handle creating the profile when a user finishes
    the signup process
    """
    if created:
        Profile.objects.get_or_create(
            user=instance
        )


post_save.connect(user_post_save_receiver, sender=User)


class Follower(models.Model):
    """
    Followers model class holding users and their followers,
     activities carriedout by a user are being followed.
    """
    author = models.CharField(max_length=254)
    follow = models.CharField(max_length=254)

    class meta:
        unique_together = ('author', 'follow')
