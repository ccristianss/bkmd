# v1/urls.py

from django.urls import path
from .views import (
    AccountListView,        AccountDetailView,          AccountPatchView,    
    MyTokenObtainPairView,  MyTokenRefreshView,
    ServiceListView,
    UserListView,           UserDetailView,
    RequestListView,        RequestDetailView,
    ManderListView,         ManderDetailView,
    RequestManagerListView, RequestManagerDetailView,
    DocumentListView,       DocumentDetailView,
    VehicleListView,        VehicleDetailView
    
    )

urlpatterns = [
    # Accounts
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('accounts/<int:id_account>/', AccountDetailView.as_view(), name='account-detail'),
    #path('accounts/<int:pk>/patch/', AccountPatchView.as_view(), name='account-patch'),
    # Auth
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    # Service
    path('service/', ServiceListView.as_view(), name='account-list'),
    #User
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id_user>/', UserDetailView.as_view(), name='user-detail'),
    #Request
    path('requests/', RequestListView.as_view(), name='request-list'),
    path('requests/<int:id_request>/', RequestDetailView.as_view(), name='request-detail'),
    #Mander
    path('manders/', ManderListView.as_view(), name='mander-list'),
    path('manders/<int:id_mander>/', ManderDetailView.as_view(), name='mander-detail'),
    #RequestManager
    path('requestmanagers/', RequestManagerListView.as_view(), name='requestmanager-list'),
    path('requestmanagers/<int:id_requestmanager>/', RequestManagerDetailView.as_view(), name='requestmanager-detail'),
    #Document
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('documents/<int:id_document>/', DocumentDetailView.as_view(), name='document-detail'),
    # Vehicle
    path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/<int:id_vehicle>/', VehicleDetailView.as_view(), name='vehicle-detail'),

]
