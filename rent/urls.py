from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
    path('house_for_rent', views.house_for_rent, name='house_for_rent'),
    path('house_for_rent_detail/<slug:rent_slug>/', views.house_for_rent_detail, name='house_for_rent_detail'),
    path('house_for_sale', views.house_for_sale, name='house_for_sale'),
    path('house_for_sale_detail/<slug:sale_slug>/', views.house_for_sale_detail, name='house_for_sale_detail'),
    
    path('land', views.land, name='land'),
    path('landDetail/<slug:land_slug>/', views.landDetail, name='landDetail'),
    
    path('hostel', views.hostel, name='hostel'),
    path('hostelDetail/<slug:hostel_slug>/', views.hostelDetail, name='hostelDetail'),
    
    # path('search/<slug:category_slug>/', views.list_category, name='list-category'),
  
    
    path('about', views.about, name='about'),
    path('tenant', views.tenant, name='tenant'),
    path('propertyDetails', views.propertyDetails, name='propertyDetails'),
    
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact'),
]