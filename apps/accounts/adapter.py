# apps/accounts/adapter.py
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom account adapter to handle username generation
    """
    
    def save_user(self, request, user, form, commit=True):
        """
        Override save_user to ensure username is set before saving
        """
        # First save the user with basic info
        user = super().save_user(request, user, form, commit=False)
        
        # Generate username from email if not set
        if not user.username and user.email:
            base_username = re.sub(r'[^a-zA-Z0-9_]', '', user.email.split('@')[0])
            if not base_username:
                base_username = 'user'
            
            # Ensure uniqueness
            username = base_username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            user.username = username
        
        if commit:
            user.save()
        
        return user