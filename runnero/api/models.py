from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile", primary_key=True)

    travelled_dist = models.PositiveIntegerField(blank=True, null=True)
    points = models.PositiveIntegerField(blank=True, null=True)


class Challenge(models.Model):
    class LevelChoices(models.TextChoices):
        BEGINNER = 'BEG', 'Beginner'
        NORMAL = 'NOR', 'Normal'
        ADVANCED = 'ADV', 'Advanced'

    for_level = models.CharField(
        max_length=3,
        choices=LevelChoices.choices,
        default=LevelChoices.NORMAL
    )
    description = models.CharField(max_length=128)
    start_at = models.CharField(max_length=5)
    end_at = models.CharField(max_length=5)
    points = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()

    def __str__(self):
        return self.description


class UserActiveChallenge(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)


class UserDoneChallenge(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)


class Prize(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    points = models.PositiveIntegerField()
    png = models.CharField(max_length=256)
    shop_name = models.CharField(max_length=64)


class UserPrize(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
