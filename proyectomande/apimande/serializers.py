

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from .models import (
    Account,
    Service, 
    User,
    Request,
    Mander,
    RequestManager,
    Document,
    Vehicle)

# Auth
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Aquí puedes personalizar la respuesta del token si lo necesitas
        # Por ejemplo, agregar más información del usuario
        data['email'] = self.user.email_account
        data['is_admin'] = self.user.isadmin_account
        # ... Otras personalizaciones ...
        return data

# Account
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id_account', 'email_account', 'password_account', 'dateregister_account', 'dateupdate_account', 'isadmin_account']
        read_only_fields = ['id_account']

    def create(self, validated_data):
        # Cifra la contraseña antes de guardarla
        validated_data['password_account'] = make_password(validated_data['password_account'])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.email_account = validated_data.get('email_account', instance.email_account)
        instance.password_account = validated_data.get('password_account', instance.password_account)
        instance.isadmin_account = validated_data.get('isadmin_account', instance.isadmin_account)
        instance.save()
        return instance
    
# Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['id_service']

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Request
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

# Mander
class ManderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mander
        fields = '__all__'

# RequestManager
class RequestManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestManager
        fields = '__all__'

# Document
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

#Vehicle
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
