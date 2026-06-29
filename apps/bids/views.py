# apps/bids/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from apps.projects.models import Project
from .models import Bid, BidItem
from .forms import BidUploadForm

@login_required
def upload_bid(request, project_id):
    """Upload bid for project"""
    # Get current organization from session or request
    # You'll need to implement this based on your organization setup
    current_org = request.user.organization_set.first()  # Adjust this based on your model
    
    project = get_object_or_404(Project, pk=project_id)
    
    # Check if user has access to this project
    if project.organization != current_org:
        messages.error(request, 'You do not have permission to upload bids for this project.')
        return redirect('projects:project_list')
    
    if request.method == 'POST':
        form = BidUploadForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.project = project
            bid.save()
            
            messages.success(request, f'Bid from {bid.contractor_name} uploaded successfully!')
            return redirect('projects:project_detail', pk=project.pk)
    else:
        form = BidUploadForm()
    
    return render(request, 'bids/upload.html', {
        'form': form,
        'project': project
    })

@login_required
def bid_detail(request, bid_id):
    """Bid details"""
    bid = get_object_or_404(Bid, pk=bid_id)
    
    # Check if user has access to this bid
    current_org = request.user.organization_set.first()  # Adjust this
    if bid.project.organization != current_org:
        messages.error(request, 'You do not have permission to view this bid.')
        return redirect('projects:project_list')
    
    return render(request, 'bids/detail.html', {'bid': bid})

@login_required
def bid_delete(request, bid_id):
    """Delete bid"""
    bid = get_object_or_404(Bid, pk=bid_id)
    
    # Check if user has access to this bid
    current_org = request.user.organization_set.first()  # Adjust this
    if bid.project.organization != current_org:
        messages.error(request, 'You do not have permission to delete this bid.')
        return redirect('projects:project_list')
    
    if request.method == 'POST':
        project_id = bid.project.id
        bid.delete()
        messages.success(request, 'Bid deleted successfully!')
        return redirect('projects:project_detail', pk=project_id)
    
    return render(request, 'bids/confirm_delete.html', {'bid': bid})

def placeholder(request):
    """Placeholder view for testing"""
    return HttpResponse("Bids app is working!")