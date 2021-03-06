from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driver', views.driver, name='driver'),
    path('createdriver', views.createdriver, name='createdriver'),
    path('driver/<int:pk>/delete', views.deletedriver, name='deletedriver'),
    path('editdriver/<int:pk>', views.editdriver, name='editdriver'),
    path('edituser/<int:pk>', views.edituser, name='edituser'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('createvehicle', views.createvehicle, name='createvehicle'),
    path('bookinghistory', views.bookinghistory, name='bookinghistory'),
    path('bookingdetails', views.bookingdetails, name='bookingdetails'),
    path('customeruser', views.customeruser, name='customeruser'),
    path('users', views.alluser, name='users'),
    path('signup', views.signupuser, name='signupuser'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),
    path('notification', views.notification, name='notification'),
    path('createnotification', views.createnotification, name='createnotification'), 
    path('notification/<int:pk>/delete', views.deletenotification, name='deletenotification'),  
    path('coupons', views.coupons, name='coupons'),
    path('createcoupons', views.createcoupons, name='createcoupons'), 

    path('editcontact', views.editcontact, name='editcontact'), 
    path('createfrompoint', views.createfrompoint, name='createfrompoint'), 

    path('brand', views.brand, name='brand'),
    path('createbrand', views.createbrand, name='createbrand'), 

    path('model', views.brandmodel, name='brandmodel'),
    path('createmodel', views.createbrandmodel, name='createbrandmodel'), 

    path('insurance', views.insurance, name='insurance'),
    path('createinsurance', views.createinsurance, name='createinsurance'), 

    path('coupons/<int:pk>/delete', views.deletecoupons, name='deletecoupons'),
    path('bookinghistory/<int:pk>/delete', views.deletebookinghistory, name='deletebookinghistory'),
    path('vehicle/<int:pk>/delete', views.deletevehicle, name='deletevehicle'),
    path('bookingdetails/<int:pk>/delete', views.deletebookingdetails, name='deletebookingdetails'),
    path('customer/<int:pk>/delete', views.deletecustomer, name='deletecustomer'),
    path('driversverify', views.drivers_verify, name='drivers_verify'),
    path('bookingrequest', views.booking_request, name='booking_request'),

    path('assigndriver/<int:pk>', views.assigndriver, name='assigndriver'),
    path('assigndriver/<int:pk>/<int:pk2>', views.assigndriver2, name='assigndriver2'),

    path('rejectdriver/<int:pk>', views.rejectdriver, name='rejectdriver'),   
    path('profile', views.profile, name='profile'),
    path('today', views.today, name='today'),
    path('week', views.week, name='week'), 
    path('month', views.month, name='month'),
    path('aftercompleted', views.aftercompleted, name='aftercompleted') 

]