# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     """Custom user model"""
#     company = models.CharField(max_length=200, blank=True)
#     phone = models.CharField(max_length=20, blank=True)
#     email_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         db_table = 'auth_user'
    
#     def __str__(self):
#         return self.email