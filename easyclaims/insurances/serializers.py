from insurances.models import Insurance
from rest_framework import serializers
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ('policy_name','type_of_policy', 'start_date', 'end_date', 'life_assureddetails', 'payment_information', 'premium_details','user_id','policy_created_time','created_at','insurance_policy_id')
