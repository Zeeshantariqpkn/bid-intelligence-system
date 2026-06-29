# apps/subscriptions/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import SubscriptionPlan, Subscription
from apps.organizations.models import Organization

@login_required
def subscription_plans(request):
    """View available subscription plans"""
    plans = SubscriptionPlan.objects.filter(is_active=True)
    current_org = request.current_organization
    
    # Get current subscription if exists
    current_subscription = None
    if hasattr(current_org, 'subscription'):
        current_subscription = current_org.subscription
    
    context = {
        'plans': plans,
        'current_subscription': current_subscription,
        'current_organization': current_org,
    }
    return render(request, 'subscriptions/plans.html', context)

@login_required
def change_plan(request, plan_id):
    """Change organization subscription plan"""
    new_plan = get_object_or_404(SubscriptionPlan, id=plan_id, is_active=True)
    current_org = request.current_organization
    
    if request.method == 'POST':
        # Check if subscription exists
        subscription, created = Subscription.objects.get_or_create(
            organization=current_org,
            defaults={
                'plan': new_plan,
                'status': 'trialing' if new_plan.name == 'free' else 'active',
                'current_period_start': timezone.now(),
                'current_period_end': timezone.now() + timedelta(days=30),
                'trial_ends_at': timezone.now() + timedelta(days=14) if new_plan.name != 'free' else None,
            }
        )
        
        if not created:
            # Update existing subscription
            old_plan = subscription.plan
            subscription.plan = new_plan
            
            # Reset trial if going from free to paid
            if old_plan.name == 'free' and new_plan.name != 'free':
                subscription.trial_ends_at = timezone.now() + timedelta(days=14)
                subscription.status = 'trialing'
            elif new_plan.name == 'free':
                subscription.status = 'active'
                subscription.trial_ends_at = None
            
            subscription.save()
        
        # Update organization limits
        current_org.max_projects = new_plan.max_projects
        current_org.max_bids_per_project = new_plan.max_bids_per_project
        current_org.plan = new_plan.name
        current_org.save()
        
        messages.success(request, f'Plan changed to {new_plan.display_name} successfully!')
        return redirect('subscriptions:plans')
    
    return render(request, 'subscriptions/confirm_change.html', {
        'new_plan': new_plan,
        'current_organization': current_org
    })

@login_required
def cancel_subscription(request):
    """Cancel current subscription"""
    current_org = request.current_organization
    
    if request.method == 'POST':
        if hasattr(current_org, 'subscription'):
            subscription = current_org.subscription
            subscription.status = 'canceled'
            subscription.save()
            
            # Downgrade to free plan
            free_plan = SubscriptionPlan.objects.get(name='free')
            subscription.plan = free_plan
            subscription.save()
            
            # Update organization limits
            current_org.max_projects = free_plan.max_projects
            current_org.max_bids_per_project = free_plan.max_bids_per_project
            current_org.plan = 'free'
            current_org.save()
            
            messages.success(request, 'Your subscription has been canceled. You have been downgraded to the Free plan.')
        else:
            messages.warning(request, 'No active subscription found.')
        
        return redirect('subscriptions:plans')
    
    return render(request, 'subscriptions/cancel.html')

@login_required
def subscription_success(request):
    """Subscription success page"""
    return render(request, 'subscriptions/success.html')