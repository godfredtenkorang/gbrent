from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('property', views.property, name='property'),
    path('propertyDetail', views.propertyDetail, name='propertyDetail'),
    path('wishListPage', views.wishListPage, name='wishListPage'),
    path('userDashboard', views.userDashboard, name='userDashboard'),
    path('dashboardHome', views.dashboardHome, name='dashboardHome'),
    path('schedule', views.schedule, name='schedule'),
    path('help', views.help, name='help'),
    path('account', views.account, name='account'),
    path('about', views.about, name='about'),
    path('tenant', views.tenant, name='tenant'),
    path('signUp', views.signUp, name='signUp'),
    path('login', views.login, name='login'),
]