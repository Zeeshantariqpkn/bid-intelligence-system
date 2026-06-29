from django.db import models
from apps.projects.models import Project

class Bid(models.Model):
    """Bid model"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bids')
    contractor_name = models.CharField(max_length=200)
    uploaded_file = models.FileField(upload_to='bids/%Y/%m/%d/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.contractor_name} - {self.project.name}"
    
    def get_total_value(self):
        total = self.bid_items.aggregate(total=models.Sum('total_price'))['total'] or 0
        return float(total)

class BidItem(models.Model):
    """Individual bid items"""
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='bid_items')
    item_name = models.CharField(max_length=500)
    quantity = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.item_name} - {self.bid.contractor_name}"

class RiskAnalysis(models.Model):
    """Risk analysis results"""
    bid = models.OneToOneField(Bid, on_delete=models.CASCADE, related_name='riskanalysis')
    overprice_items = models.JSONField(default=list)
    underprice_items = models.JSONField(default=list)
    missing_items = models.JSONField(default=list)
    risk_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    analyzed_at = models.DateTimeField(auto_now_add=True)
    
    def get_risk_level(self):
        if self.risk_score <= 20:
            return ('Low', 'success')
        elif self.risk_score <= 50:
            return ('Medium', 'warning')
        elif self.risk_score <= 75:
            return ('High', 'danger')
        else:
            return ('Critical', 'dark')