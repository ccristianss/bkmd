# v1/views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from django.http import Http404
from .models import (
    Account, 
    Service, 
    User,
    Request,
    Mander,
    RequestManager,
    Document,
    Vehicle)
from .serializers import (
    MyTokenObtainPairSerializer, 
    AccountSerializer, 
    ServiceSerializer, 
    UserSerializer,
    RequestSerializer,
    ManderSerializer,
    RequestManagerSerializer,
    DocumentSerializer,
    VehicleSerializer)

# Auth
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

# Accounts
class AccountLoginView(APIView):
    def post(self, request):
        # Obtener el correo electrónico y la contraseña del cuerpo de la solicitud
        email = request.data.get('email_account', '')
        password = request.data.get('password_account', '')

        # Buscar un usuario con el mismo correo electrónico
        try:
            account = Account.objects.get(email_account=email)
        except Account.DoesNotExist:
            # Si el usuario no existe, puedes devolver un error
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar si la contraseña coincide
        if check_password(password, account.password_account):
            # Si la contraseña es correcta, devolver el id_account
            return Response({'id_account': account.id_account}, status=status.HTTP_200_OK)
        else:
            # Si la contraseña no coincide, devolver un error
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountListView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.validated_data['password_account'] = make_password(serializer.validated_data['password_account'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetailView(APIView):
    def get(self, request, id_account):
        account = get_object_or_404(Account, id_account=id_account)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    def patch(self, request, id_account):
        account = get_object_or_404(Account, id_account=id_account)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_account):
        account = get_object_or_404(Account, id_account=id_account)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_object(self, id_account):
        try:
            return Account.objects.get(id_account=id_account)
        except Account.DoesNotExist:
            raise Http404
    
class AccountPatchView(UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
# Services
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceListView(APIView):
    def get(self, request):
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get_object(self, id_user):
        try:
            return User.objects.get(id_user=id_user)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id_user):
        user = self.get_object(id_user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id_user):
        user = self.get_object(id_user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_user):
        user = self.get_object(id_user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Request
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestListView(APIView):
    def get(self, request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestDetailView(APIView):
    def get_object(self, id_request):
        try:
            return Request.objects.get(id_request=id_request)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, id_request):
        request_obj = self.get_object(id_request)
        serializer = RequestSerializer(request_obj)
        return Response(serializer.data)

    def put(self, request, id_request):
        request_obj = self.get_object(id_request)
        serializer = RequestSerializer(request_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_request):
        request_obj = self.get_object(id_request)
        request_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Mander
class ManderViewSet(viewsets.ModelViewSet):
    queryset = Mander.objects.all()
    serializer_class = ManderSerializer

class ManderListView(APIView):
    def get(self, request):
        manders = Mander.objects.all()
        serializer = ManderSerializer(manders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManderDetailView(APIView):
    def get_object(self, id_mander):
        try:
            return Mander.objects.get(id_mander=id_mander)
        except Mander.DoesNotExist:
            raise Http404

    def get(self, request, id_mander):
        mander = self.get_object(id_mander)
        serializer = ManderSerializer(mander)
        return Response(serializer.data)

    def put(self, request, id_mander):
        mander = self.get_object(id_mander)
        serializer = ManderSerializer(mander, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_mander):
        mander = self.get_object(id_mander)
        mander.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# RequestManager
class RequestManagerViewSet(viewsets.ModelViewSet):
    queryset = RequestManager.objects.all()
    serializer_class = RequestManagerSerializer

class RequestManagerListView(APIView):
    def get(self, request):
        request_managers = RequestManager.objects.all()
        serializer = RequestManagerSerializer(request_managers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestManagerDetailView(APIView):
    def get_object(self, id_requestmanager):
        try:
            return RequestManager.objects.get(id_requestmanager=id_requestmanager)
        except RequestManager.DoesNotExist:
            raise Http404

    def get(self, request, id_requestmanager):
        request_manager = self.get_object(id_requestmanager)
        serializer = RequestManagerSerializer(request_manager)
        return Response(serializer.data)

    def put(self, request, id_requestmanager):
        request_manager = self.get_object(id_requestmanager)
        serializer = RequestManagerSerializer(request_manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_requestmanager):
        request_manager = self.get_object(id_requestmanager)
        request_manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Document
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentListView(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentDetailView(APIView):
    def get_object(self, id_document):
        try:
            return Document.objects.get(id_document=id_document)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, id_document):
        document = self.get_object(id_document)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, id_document):
        document = self.get_object(id_document)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_document):
        document = self.get_object(id_document)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Vehicle
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleListView(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetailView(APIView):
    def get_object(self, id_vehicle):
        try:
            return Vehicle.objects.get(id_vehicle=id_vehicle)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, id_vehicle):
        vehicle = self.get_object(id_vehicle)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, id_vehicle):
        vehicle = self.get_object(id_vehicle)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_vehicle):
        vehicle = self.get_object(id_vehicle)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



