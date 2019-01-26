from django import forms
from claim.models import Claim
from rest_framework import serializers

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model=Claim
        fields=["claim_name","dob","address","typeOfClaim","details","status","is_approved","policy_id","user_id","claim_created_time","created_at","claim_id"]

