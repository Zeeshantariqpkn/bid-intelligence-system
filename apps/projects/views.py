from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from apps.organizations.models import Organization, OrganizationMember

@login_required
def dashboard(request):
    """Main dashboard"""
    # Get user's organizations
    organizations = Organization.objects.filter(members__user=request.user, members__is_active=True)
    
    if not organizations.exists():
        # Create default organization for user
        org = Organization.objects.create(
            name=f"{request.user.username}'s Company",
            slug=f"{request.user.username.lower()}-company"
        )
        OrganizationMember.objects.create(
            user=request.user,
            organization=org,
            role='owner'
        )
        organizations = [org]
    
    # Get current organization
    current_org = organizations[0]
    
    # Get projects for current organization
    projects = Project.objects.filter(organization=current_org)
    
    context = {
        'organizations': organizations,
        'current_organization': current_org,
        'projects': projects,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def project_list(request):
    """List all projects"""
    organizations = Organization.objects.filter(members__user=request.user)
    current_org = organizations.first()
    
    if not current_org:
        messages.warning(request, 'Please create an organization first.')
        return redirect('dashboard')
    
    projects = Project.objects.filter(organization=current_org)
    
    return render(request, 'projects/list.html', {
        'projects': projects,
        'current_organization': current_org
    })

@login_required
def project_create(request):
    """Create new project"""
    organizations = Organization.objects.filter(members__user=request.user)
    current_org = organizations.first()
    
    if not current_org:
        return redirect('dashboard')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        client_name = request.POST.get('client_name')
        description = request.POST.get('description')
        
        project = Project.objects.create(
            name=name,
            client_name=client_name,
            description=description,
            organization=current_org,
            created_by=request.user
        )
        
        messages.success(request, f'Project "{name}" created successfully!')
        return redirect('projects:project_detail', pk=project.pk)
    
    return render(request, 'projects/form.html', {'title': 'Create Project'})

@login_required
def project_detail(request, pk):
    """Project details"""
    organizations = Organization.objects.filter(members__user=request.user)
    current_org = organizations.first()
    project = get_object_or_404(Project, pk=pk, organization=current_org)
    
    return render(request, 'projects/detail.html', {'project': project})

@login_required
def project_update(request, pk):
    """Update project"""
    organizations = Organization.objects.filter(members__user=request.user)
    current_org = organizations.first()
    project = get_object_or_404(Project, pk=pk, organization=current_org)
    
    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.client_name = request.POST.get('client_name')
        project.description = request.POST.get('description')
        project.save()
        
        messages.success(request, 'Project updated successfully!')
        return redirect('project_detail', pk=project.pk)
    
    return render(request, 'projects/form.html', {'project': project, 'title': 'Edit Project'})

@login_required
def project_delete(request, pk):
    """Delete project"""
    organizations = Organization.objects.filter(members__user=request.user)
    current_org = organizations.first()
    project = get_object_or_404(Project, pk=pk, organization=current_org)
    
    if request.method == 'POST':
        project_name = project.name
        project.delete()
        messages.success(request, f'Project "{project_name}" deleted successfully!')
        return redirect('project_list')
    
    return render(request, 'projects/delete.html', {'project': project})