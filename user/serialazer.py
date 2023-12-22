from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Parolni heshlab ko'rsatish
        data['password'] = "********"
        return data

class ProfileLoginserialazer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    