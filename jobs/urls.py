
from django.urls import path

from . import views

from .views import CreateView, JobCreateView, JobListView, PIDCreateView, PIDListView


urlpatterns = [ 
    path('create_job/', JobCreateView.as_view(), name='create_job'),
    path('job_list/', JobListView.as_view(), name='job_list'),
    path('edit_job/<str:pk>', views.editJob, name='edit_job'),
    path('sendmail/<str:pk>', views.sendMail, name='sendmail'),

    #PID URLS
    
    path('create_pid/', PIDCreateView.as_view(), name='create_pid'),
    path('edit_pid/<str:pk>', views.editPID, name='edit_pid'),
    path('pid_list/', PIDListView.as_view(), name='pid_list'),
]
