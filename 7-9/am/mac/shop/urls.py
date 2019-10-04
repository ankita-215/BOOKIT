from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.home),
    path('home', views.home,name='home'),
    path("about", views.about, name="AboutUs"),
    path("contact", views.contact, name="contact us"),
    path("v_view", views.v_view, name="V_view"),
    path('authorized.html',views.authorized, name='Authorized'),
    path('accept<int:F_id>',views.accept, name='accept'),
    path('authorize<int:F_id>',views.reject, name='reject'), 
    path("areg", views.Areg),
    path("register1", views.register1,name="register"),
    path("forget", views.forgotpass),
    path("login", views.ulogin),
    path("logout",views.logout),
    path("driver1", views.driver1),  
    path("vlist", views.vlist), 
    path("blist", views.blist),
    path("list", views.list),
    path("ulist", views.ulist),
    path("dlist", views.dlist),
    path("bookinglist", views.bookinglist),       
    path("vehiclelist", views.vehiclelist),   
    path("vupload", views.vupload),   
    path("nextpage", views.nextpage,name="nextpage"),  
    path("vehicle/<int:myid>", views.quickview, name="quickview"),
    path('edit',views.edit_profile, name='edit_profile'), 
    #****************************************************************
    path('add1', views.book1, name='add1'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-point/', views.load_point, name='ajax_load_point'),
    path('ajax/load-cat/', views.load_cat, name='ajax_load_cat'),
    #*************************************************************************
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
