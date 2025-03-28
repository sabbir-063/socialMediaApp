# Custom User Model in accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.png')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def follow(self, user):
        """Follow another user"""
        self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user"""
        self.following.remove(user)

    def is_following(self, user):
        """Check if following a user"""
        return self.following.filter(id=user.id).exists()

    def __str__(self):
        return self.username