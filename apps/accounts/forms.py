# apps/accounts/forms.py
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
import re

User = get_user_model()  # This will get the default auth.User

class CustomSignupForm(SignupForm):
    """
    Custom signup form that automatically generates a username from email
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the username field completely
        if 'username' in self.fields:
            del self.fields['username']
    
    def save(self, request):
        # Get the email
        email = self.cleaned_data.get('email')
        
        # Generate a username from email
        base_username = re.sub(r'[^a-zA-Z0-9_]', '', email.split('@')[0])
        if not base_username:
            base_username = 'user'
        
        # Make username unique
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        
        # Create the user
        user = super().save(request)
        
        # Set the username
        user.username = username
        user.save()
        
        return user