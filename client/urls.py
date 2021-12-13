
from django.urls import path

from . import views
from .views import ClientListView


urlpatterns = [
    path('clientslist/', ClientListView.as_view(), name='clientslist'),
    path('create_client/', views.createClient, name='create_client'),

    path('edit_client/<str:pk>', views.editClient, name='edit_client'),
    path('client_home/<str:pk>', views.clientHome, name='client_home'),

    


]
