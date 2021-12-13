
from django.urls import path

from . import views


urlpatterns = [ 
    path('job_refund/<str:pk>', views.jobRefund, name='job_refund'),
    path('refund_list/', views.JobRefundListView.as_view(), name='refund_list'),
]
