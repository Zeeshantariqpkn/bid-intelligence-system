from django.shortcuts import redirect

class OrganizationMiddleware:
    """Handle organization context"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            # Get current organization from session
            org_id = request.session.get('current_organization')
            
            if org_id:
                try:
                    from .models import Organization
                    request.current_organization = Organization.objects.get(
                        id=org_id,
                        members__user=request.user,
                        members__is_active=True
                    )
                except Organization.DoesNotExist:
                    request.current_organization = None
            else:
                request.current_organization = None
        
        response = self.get_response(request)
        return response