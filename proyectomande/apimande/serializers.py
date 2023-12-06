

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
        fields = '__all__'
        read_only_fields = ['id_account']
    
# Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['id_service']
    
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
