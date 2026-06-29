from rest_framework import serializers
from apps.projects.models import Project
from apps.bids.models import Bid, BidItem

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'client_name', 'description', 'created_at']
        read_only_fields = ['created_at']

class BidItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidItem
        fields = ['id', 'item_name', 'quantity', 'unit_price', 'total_price']

class BidSerializer(serializers.ModelSerializer):
    items = BidItemSerializer(many=True, read_only=True)
    total_value = serializers.SerializerMethodField()
    
    class Meta:
        model = Bid
        fields = ['id', 'contractor_name', 'uploaded_at', 'total_value', 'items']
    
    def get_total_value(self, obj):
        return obj.get_total_value()