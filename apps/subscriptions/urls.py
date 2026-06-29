# apps/subscriptions/urls.py
from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('plans/', views.subscription_plans, name='plans'),
    path('change/<int:plan_id>/', views.change_plan, name='change_plan'),
    path('cancel/', views.cancel_subscription, name='cancel'),
    path('success/', views.subscription_success, name='success'),
]