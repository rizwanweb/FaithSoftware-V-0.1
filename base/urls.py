from django.urls import path


from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('', views.home, name='home'),
    path('dashboard/', views.baseHome, name='dashboard'),
    path('headers/', views.HeaderFormView.as_view(), name='headers')
]
