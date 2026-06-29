from django.contrib import admin
from .models import Bid, BidItem, RiskAnalysis

class BidItemInline(admin.TabularInline):
    model = BidItem
    extra = 0

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['contractor_name', 'project', 'uploaded_at']
    list_filter = ['project', 'uploaded_at']
    search_fields = ['contractor_name']
    inlines = [BidItemInline]

@admin.register(RiskAnalysis)
class RiskAnalysisAdmin(admin.ModelAdmin):
    list_display = ['bid', 'risk_score', 'analyzed_at']
    list_filter = ['risk_score']