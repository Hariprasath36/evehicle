from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
   
    path('public_register/',views.public_register,name='public_register'),
    
    path('public_login/',views.public_login,name='public_login'),
    path('public_logout/',views.public_logout,name='public_logout'),
    path('public_dashboard/',views.public_dashboard,name='public_dashboard'),
    path('search/',views.search,name='search'),
    path('book_slot/',views.book_slot,name='book_slot'),
    path('slot_detail/',views.slot_detail,name='slot_detail'),
    path('booking_status/',views.booking_status,name='booking_status'),
    path('admin_booking/',views.admin_booking,name='admin_booking'),
    path('accept/<int:pk>/',views.accept,name='accept'),
    path('reject/<int:pk>/',views.reject,name='reject'),
    path('payment_status/<int:pk>/',views.payment_status,name='payment_status'),
]