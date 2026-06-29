# apps/bids/urls.py
from django.urls import path
from . import views

app_name = 'bids'  # This creates the 'bids' namespace

urlpatterns = [
    path('upload/<int:project_id>/', views.upload_bid, name='upload_bid'),
    path('<int:bid_id>/', views.bid_detail, name='bid_detail'),
    path('<int:bid_id>/delete/', views.bid_delete, name='bid_delete'),
]