from rest_framework import serializers
from user.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
        user.set_password(user.password)
        user.save()
        return user
