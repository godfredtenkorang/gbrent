from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='signUp'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    
    # Dashboard
    path('dashboard', views.dashboardHome, name='dashboardHome'),
    path('schedule', views.schedule, name='schedule'),
    path('wishListPage', views.wishListPage, name='wishListPage'),
    path('help', views.help, name='help'),
    path('account_settings', views.account, name='account'),
    path('userDashboard', views.userDashboard, name='userDashboard'),
    
]