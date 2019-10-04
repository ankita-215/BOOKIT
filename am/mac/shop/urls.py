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
    path('authorized.html',views.authorized),
    path('accept<int:F_id>',views.accept, name='accept'),
    path('authorized<int:F_id>',views.reject, name='reject'), 
    path("areg", views.Areg),
    path("register1", views.register1,name="register"),
    path("forget", views.forgotpass),
    path("login", views.ulogin),
    path("logout",views.logout),
    path("driver1", views.driver1),  
    path("vlist", views.vlist),
    path("catlist", views.catlist),
    path("subcatlist", views.subcatlist),
    path("editveh<int:myid>", views.editveh),
    path("editc<int:myid>", views.editc), 
    path("editsc<int:myid>", views.editsc), 
    path("ecity<int:myid>", views.ecity), 
    path("epoint<int:myid>", views.epoint), 
    path("delcat<int:myid>", views.delcat), 
    path("delSC<int:myid>", views.delSC), 
    path("delcity<int:myid>", views.delcity), 
    path("delpoint<int:myid>", views.delpoint), 
    path("blist", views.blist),
    path("dbooklist", views.dbooklist),
    path("list", views.list),
    path("dblist", views.dblist),
    path("driverbooklist", views.driverbooklist),
    path("dbookinglist", views.dbookinglist),
    path("oreg",views.oreg),
    path("bookd", views.bookd),
    path("ulist", views.ulist),
    path("ulog", views.ulog),
    path("addcat", views.addcat),
    path("addcity", views.addcity),
    path("addpoint", views.addpoint),
    path("addsubcat", views.addsubcat),
    path("dlist", views.dlist),
    path("citylist", views.citylist),
    path("GeneratePDF<int:id>", views.GeneratePDF),
    path("bookinglist", views.bookinglist),       
    path("vehiclelist", views.vehiclelist),  
    path("pointlist", views.pointlist), 
    path("vupload", views.vupload),   
    path("nextpage", views.nextpage,name="nextpage"),  
    path("vehicle/<int:myid>", views.quickview, name="quickview"),
    path("driver/<int:myid>", views.dview),
    path('edit',views.edit_profile, name='edit_profile'), 
    path('edit_admin',views.edit_admin, name='edit_admin'),
    #****************************************************************
    path('add1', views.book1, name='add1'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-point/', views.load_point, name='ajax_load_point'),
    path('ajax/load-cat/', views.load_cat, name='ajax_load_cat'),
    #*************************************************************************
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
