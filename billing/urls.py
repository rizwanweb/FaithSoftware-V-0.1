
from django.urls import path

from . import views



urlpatterns = [
    path('bill_management/', views.BillManagementView.as_view(), name='billHome'),
    path('pending_bills/', views.PendingBillsView.as_view(), name='pending_bills'),
    path('create_bill/<int:pk>', views.createBill, name='create_bill'),
    path('update_bill/<int:pk>', views.editBill, name='update_bill'),

    path('pidbill_management/', views.PIDBillManagementView.as_view(), name='pidbillHome'),
    path('create_pidbill/<int:pk>', views.createPIDBill, name='create_pid_bill'),
    #path('update_pidbill/<int:pk>', views.editPIDBill, name='update_pidbill'),
    path('pending_pid_bills/', views.PendingPIDBillsView.as_view(), name='pending_pid_bills'),
    path('update_pidbill/<int:pk>', views.editPIDBill, name='update_pidbill'),

    


    


]
