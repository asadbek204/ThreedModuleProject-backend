from rest_framework import serializers
from .models import User, Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ['id', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = '__all__'

