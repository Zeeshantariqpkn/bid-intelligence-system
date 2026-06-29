# apps/subscriptions/models.py
from django.db import models
from django.contrib.auth.models import User
from apps.organizations.models import Organization

class SubscriptionPlan(models.Model):
    """Subscription plans available"""
    PLAN_TYPES = [
        ('free', 'Free'),
        ('basic', 'Basic'),
        ('pro', 'Professional'),
        ('enterprise', 'Enterprise'),
    ]
    
    name = models.CharField(max_length=50, choices=PLAN_TYPES, unique=True)
    display_name = models.CharField(max_length=100)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_yearly = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Plan features
    max_projects = models.IntegerField(default=5)
    max_bids_per_project = models.IntegerField(default=10)
    max_storage_mb = models.IntegerField(default=100)
    has_advanced_analytics = models.BooleanField(default=False)
    has_api_access = models.BooleanField(default=False)
    priority_support = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.get_name_display()

class Subscription(models.Model):
    """User subscription"""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('trialing', 'Trialing'),
        ('past_due', 'Past Due'),
        ('canceled', 'Canceled'),
        ('incomplete', 'Incomplete'),
    ]
    
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE, related_name='subscription')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='trialing')
    trial_ends_at = models.DateTimeField(null=True, blank=True)
    current_period_start = models.DateTimeField()
    current_period_end = models.DateTimeField()
    
    # Stripe integration
    stripe_customer_id = models.CharField(max_length=100, blank=True)
    stripe_subscription_id = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.organization.name} - {self.plan.get_name_display()}"

class SubscriptionInvoice(models.Model):
    """Invoice records"""
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='invoices')
    stripe_invoice_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    invoice_pdf = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Invoice {self.stripe_invoice_id} - {self.amount}"