from django.db import models
from django.contrib.auth.models import User
from apps.organizations.models import Organization

class Project(models.Model):
    """Project model"""
    name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='projects')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_bid_count(self):
        return self.bids.count()