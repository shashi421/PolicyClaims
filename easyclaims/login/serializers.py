from login.models import User
from rest_framework import serializers
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'password', 'postcode', 'dob', 'created_at')
