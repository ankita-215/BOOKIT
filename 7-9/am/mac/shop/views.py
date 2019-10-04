from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse
from django.db import models
from math import ceil
from . import views
from urllib import request
from .models import register,vehicle,driver,book,Country,City,P,C
from django.urls import reverse
import re
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
import datetime
from django.contrib import messages
from django.views.decorators.cache import cache_control
#************************************************************
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person
#***************************************************************


def home(request):
    allProds = []
    catprods = vehicle.objects.values('category','vid')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = vehicle.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds':allProds}
    return render(request, 'home.html', params)
def about(request):
    return render(request,'shop/about.html')
#contact us page
def contact(request):
    return HttpResponse("contact page")
#page for view vehicless
#home page
def v_view(request):
    allProds = []
    catprods = vehicle.objects.values('category','vid')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = vehicle.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds':allProds}
    return render(request, 'shop/v_view.html', params)
#about us page


#user registration
def register1(request):
  if request.method=="POST":
    print(request)
    name= request.POST.get('name','')
    address= request.POST.get('address','')
    Mono= request.POST.get('Mono','')
    city= request.POST.get('city','')
    pincode= request.POST.get('pincode','')
    email= request.POST.get('email','')
    password= request.POST.get('password','')
    Cpassword= request.POST.get('Cpassword','')
    Rdate=request.POST.get(date.today)
    if password==Cpassword:
   # mobile number and email check
      if register.objects.filter(email=email).exists():
         if register.objects.filter(Mono=Mono).exists():
           messages.warning(request,'mobile number is already exist as user!')
           return render(request,'shop/register1.html')             
         else:
           messages.warning(request,'Email already exists as a user!') 
           return render(request,'shop/register1.html')
         return render(request,'shop/register1.html') 
       
          # mobile number and email check
      elif driver.objects.filter(email=email).exists():
          if driver.objects.filter(Mono=Mono).exists():
              messages.warning(request,'mobile number and Email already exists as a driver!')
              return render(request,'shop/register1.html')             
          else:
              messages.warning(request,'Your email already exists as a driver! please enter another email!') 
              return render(request,'shop/register1.html')
          return render(request,'shop/register1.html')  
        # email number check
      elif register.objects.filter(email=email).exists():
              messages.error(request,'Your email already exists as a user! please enter another email!')
              return render(request,'shop/register1.html')
      elif driver.objects.filter(email=email).exists():
              messages.error(request,'Your email already exists as a user! please enter another email!')
              return render(request,'shop/register1.html')
      elif admin1.objects.filter(email=email).exists():
              messages.error(request,'Your email already exists as a user! please enter another email!')
              return render(request,'shop/register1.html') 
       # mobile number check
      elif register.objects.filter(Mono=Mono).exists():
              messages.error(request,'mobile number already exists as a Farmer!')
              return render(request,'shop/register1.html') 
      elif driver.objects.filter(Mono=Mono).exists():
              messages.error(request,'mobile number already exists as a Trader!')
              return render(request,'shop/register1.html')             
      else:
            reg= register(name=name, address=address,Mono=Mono,city=city,Pincode=pincode,email=email,password=password,Rdate=Rdate)
            reg.save()
            messages.success(request,'registered sucessfully!')
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return render(request, 'shop/register1.html')
    else:
        messages.warning(request,'Password not matching!')
        return render(request,'shop/register1.html')
  else:       
    return render(request,'shop/register1.html')

  
#user login
def ulogin(request):
      if request.method == 'POST': 
        if register.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            reg=register.objects.get(email=request.POST['email'], password=request.POST['password'])
            if reg.status==0:
                messages.warning(request,'Your Approval is still panding please wait')
                return render(request,'shop/login.html',{'reg':reg})
            else:
                request.session["lgnu"] ='Welcome' + " " +reg.email  
                request.session["mail"]=reg.email      
                return render(request, 'shop/next.html', {'reg': reg})
          #driver
        elif driver.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            dri = driver.objects.get(email=request.POST['email'], password=request.POST['password']) 
            if dri.status==0:
                messages.warning(request,'Your Approval is still panding please wait')
                return render(request,'shop/login.html',{'dri':dri})
            else:   
                request.session["lgnd"] ='Welcome' + " " +dri.email 
                request.session["dri"]=dri.email 
                request.session["mail"]=dri.email      
                return render(request,'shop/next.html', {'dri': dri})
        
       #admin
        elif admin1.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            ad= admin1.objects.get(email=request.POST['email'], password=request.POST['password'])
            if ad.status==0:
                messages.warning(request,'Your Approval is still panding please wait')
                return render(request,'shop/login.html',{'ad':ad})
            else: 
                request.session["lgna"] ='Welcome' + " " +ad.email 
                request.session["mail"]=ad.email   
                          
                return render(request, 'shop/next.html', {'ad': ad})
        else:
          context = {'msg': 'Invalid username or password'}
          return render(request,'shop/login.html',context)
      return render(request,'shop/login.html')



# driver registration
 
def driver1(request):
    if request.method == 'POST':
       password= request.POST.get('password','')
       firstname= request.POST.get('firstname','')
       lastname= request.POST.get('lastname','')
       email= request.POST.get('email','')
       Mono= request.POST.get(' Mono','')
       city= request.POST.get('city','')
       licence=request.POST.get('licence')
       Cpassword= request.POST.get('password','')
       if password==Cpassword:
   # mobile number and email check
         if register.objects.filter(email=email).exists():
           if register.objects.filter(Mono=Mono).exists():
             messages.warning(request,'mobile number is already exist as user!')             
           else:
             messages.warning(request,'Email already exists as a user!') 
           return render(request,'shop/register1.html') 
       
          # mobile number and email check
         elif driver.objects.filter(email=email).exists():
            if driver.objects.filter(Mono=Mono).exists():
              messages.warning(request,'mobile number and Email already exists as a driver!')
              return render(request, 'shop/driver.html')             
            else:
              messages.warning(request,'Your email already exists as a driver! please enter another email!')
              return render(request, 'shop/driver.html') 
            return render(request, 'shop/driver.html')  
        # email number check
         elif register.objects.filter(email=email).exists():
              messages.error(request,'Your email already exists as a user! please enter another email!')
              return render(request, 'shop/driver.html')
         elif driver.objects.filter(email=email).exists():
              messages.error(request,'Your email already exists as a user! please enter another email!')
              return render(request, 'shop/driver.html')
         elif admin1.objects.filter(email=email).exists():
              messages.error(request,'Your email already exists as a user! please enter another email!')
              return render(request, 'shop/driver.html')
       # mobile number check
         elif register.objects.filter(Mono=Mono).exists():
              messages.error(request,'mobile number already exists as a Farmer!')
              return render(request, 'shop/driver.html') 
         elif driver.objects.filter(Mono=Mono).exists():
              messages.error(request,'mobile number already exists as a Trader!')
              return render(request, 'shop/driver.html')            
         else:
            dri = driver(password=password,firstname=firstname,lastname=lastname,email=email,Mono=Mono,city=city,licence=licence)
            dri.save()
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return render(request, 'shop/driver.html')
      
       else:
         messages.warning(request,'Password not matching!')
         return render(request,'shop/driver.html')
    else:       
      return render(request,'shop/driver.html')

 
#after login sucessfull page
def nextpage(request):
    return render(request,'shop/next.html')
#upload vehicle details page
def vupload(request): 
    d=driver.objects.filter(email=request.session["dri"])
    d1=driver.objects.get(email=request.session["dri"])
    if request.method == 'POST': 
        form = v(request.POST, request.FILES) 
        if form.is_valid(): 
           vupload= form.save(commit=False)
           vupload.email=d1.email
           vupload.save()
           return HttpResponse("sucessfully uploaded") 
    else: 
        form = v() 
    return render(request, 'shop/vupload.html', {'form' : form}) 

def forgotpass(request):
    if request.method == 'POST':  
          email= request.POST.get('email','')
          # farmer
          if register.objects.filter(email=request.POST['email']).exists():
            dri =  register.objects.get(email=request.POST['email'])
            password=dri.password
            name=dri.name
            subject = 'recover your password'
            message = 'Your Name is:'+ name + '\nYour password is:'+ password           
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("email sent successfully")
            #holder
          elif driver.objects.filter(email=request.POST['email']).exists():
            dri = driver.objects.get(email=request.POST['email'])
            password=dri.password
            name=dri.name
            subject = 'recover your password'
            message = 'Your Name is:'+ name + '\nYour Password is:'+ password             
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("email sent successfully")
          elif admin1.objects.filter(email=request.POST['email']).exists():
            dri = admin1.objects.get(email=request.POST['email'])
            password=dri.password
            name=dri.name
            subject = 'recover your password'
            message = 'Your Name is:'+ name + '\nYour Password is:'+ password             
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("email sent successfully")
            #trader
          else:
            return render(request,'shop/forget.html')
    else:
       return render(request,'shop/forget.html')

# logout
@cache_control(no_cache=True, must_revalidate=True,non_store=True,max_age=0)
def logout(request):
    request.session.modified = True
    request.session.flush()
    request.session.modified = True
    return render(request,'home.html')


def quickview(request,myid):
   v= vehicle.objects.filter(vid=myid)
   d = vehicle.objects.get(vid=myid)
   request.session['num']=d.v_num
   return render(request, 'shop/quickview.html', {'v':v[0]})

def booking1(request):
   vnum=request.session['num']
   v= vehicle.objects.filter(v_num=vnum)
   dist=District.objects.all()
   pod=pd.objects.all()
   name= request.POST.get('name','')
   address=request.POST.get('address','')
   Mono=request.POST.get('Mono','')
   City=request.POST.get('city','')
   Pincode=request.POST.get('pincode','')
   email=request.POST.get('email','')
   v_num=request.session['num']
   dp=request.POST.get('pd','')
   startdate=request.POST.get('startdate')
   enddate=request.POST.get('enddate')
   b= books(name=name,address=address,Mono=Mono,City=City,Pincode= Pincode,email=email,v_num=v_num,startdate=startdate,enddate=enddate)
   b.save()
   return render(request,'shop/booking.html', {'v':v[0],'dist':dist,'pod':pod})


#*******************************************************************************************************************************************
class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'shop/dd.html', {'cities': cities})

def load_point(request):
    c = request.GET.get('city')
    p = P.objects.filter(c=c).order_by('name')
    return render(request, 'shop/dd.html', {'p': p})

def load_cat(request):
    c = request.GET.get('subcategory')
    p = scat.objects.filter(c=c).order_by('name')
    return render(request, 'shop/dd.html', {'p': p})

class bookingCreateView(CreateView):
    model = book
    form_class = BookingForm
    success_url = reverse_lazy('person_changelist')

def book1(request):
    storage=messages.get_messages(request)
    storage.used=True
    v= vehicle.objects.filter(v_num=request.session['num'])
    d = vehicle.objects.get(v_num=request.session['num'])
    if request.method == 'POST': 
       
        form = BookingForm(request.POST, request.FILES) 
        if form.is_valid(): 
          book1= form.save(commit=False)
          
          #book1.v_num= book.objects.get(v_num=request.session['num'])

          book1.v_num=d.v_num
          book1.startdate=request.session['sdate']
          book1.enddate=request.session['edate']
          book1.save()
          messages.success(request,'booking sucessfully!')
          return render(request, 'shop/book_form.html', {'v':v[0]}) 
    else: 
        form = BookingForm() 
    return render(request, 'shop/book_form.html',{'form':form,'v':v[0]}) 

def edit_profile(request):  
    if register.objects.filter(email=request.session['mail']).exists():
      user = register.objects.get(email=request.session['mail'])
      form = editU(instance=user)
      if request.method == "POST":
        form = editU(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)               
          update.user = user
          update.save()         
    elif driver.objects.filter(email=request.session['mail']).exists():
      user = driver.objects.get(email=request.session['mail'])
      form =editD(instance=user)
      if request.method == "POST":
        form =editD(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)               
          update.user = user
          update.save()   
          messages.success(request,'Your profile update Successfully')         
    elif admin1.objects.filter(email=request.session['mail']).exists():
      user = admin1.objects.get(email=request.session['mail'])
      form = editA(instance=user)
      if request.method == "POST":
        form =editA(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)               
          update.user = user
          update.save()    
          messages.success(request,'Your profile update Successfully')       
    return render(request, 'shop/edit_profile.html', {'form': form})

def Areg(request): 
    if request.method == 'POST': 
        form = adminreg(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return HttpResponse("sucessfully uploaded") 
    else: 
        form = adminreg() 
    return render(request, 'shop/Areg.html', {'form' : form}) 

def authorized(request):
    reg= register.objects.all()
    dri = driver.objects.all()
    ad=admin1.objects.all() 
    veh=vehicle.objects.all() 
    
    return render(request,'shop/authorized.html', locals())

def reject(request,F_id):
      register.objects.get(uid=F_id).delete()
      driver.objects.get(did=F_id).delete()
      admin1.objects.get(id=F_id).delete() 
      vehicle.objects.get(vid=F_id).delete()          
      messages.warning(request,'Rejected Successfully')
      return redirect('shop/authorized.html')
           
  #accept Farmer request
def accept(request,F_id):
      a=register.objects.filter(uid=F_id).update(status=1)
      b=driver.objects.filter(did=F_id).update(status=1)
      c=admin1.objects.filter(id=F_id).update(status=1)
      d=vehicle.objects.filter(vid=F_id).update(status=1) 
      if a:
        e=register.objects.get(uid=F_id)      
        subject = 'For Authentication of request'
        message = 'Authentication Successfully '
        to = e.email     
        email_from = settings.EMAIL_HOST_USER    
        send_mail( subject, message, email_from, [to] )               
        messages.success(request,'Approved Successfully') 
        return redirect('authorized.html')
      elif b:
        e=driver.objects.get(did=F_id)      
        subject = 'For Authentication of request'
        message = 'Authentication Successfully '
        to = e.email     
        email_from = settings.EMAIL_HOST_USER    
        send_mail( subject, message, email_from, [to] )               
        messages.success(request,'Approved Successfully')
        return redirect('authorized.html') 
      elif c:
        e=admin1.objects.get(id=F_id)      
        subject = 'For Authentication of request'
        message = 'Authentication Successfully '
        to = e.email     
        email_from = settings.EMAIL_HOST_USER    
        send_mail( subject, message, email_from, [to] )               
        messages.success(request,'Approved Successfully')
        return redirect('authorized.html') 
      elif d:
        e=vehicle.objects.get(vid=F_id)      
        subject = 'For Authentication of request'
        message = 'Authentication Successfully '
        to = e.email     
        email_from = settings.EMAIL_HOST_USER    
        send_mail( subject, message, email_from, [to] )               
        messages.success(request,'Approved Successfully')
        return redirect('authorized.html') 

      return redirect('shop/authorized.html')
     
def vlist(request):
      v=vehicle.objects.filter(email=request.session['dri'])
      return render(request,'shop/vlist.html',{'v':v})
      
def ulist(request):
      v=register.objects.all()
      return render(request,'shop/ulist.html',{'v':v})

def dlist(request):
      v=driver.objects.all()
      return render(request,'shop/dlist.html',{'v':v})

def blist(request):
     a = vehicle.objects.get(email=request.session['dri'])
     d=a.v_num
     c=book.objects.filter(v_num=d)
     return render(request,'shop/blist.html',{'c':c})    

def bookinglist(request):
    b=book.objects.all()
    return render(request,'shop/bookinglist.html',{'b':b}) 

def vehiclelist(request):
      v=vehicle.objects.all()
      return render(request,'shop/vehiclelist.html',{'v':v})   

def list(request):
    if request.method == 'POST':
        s= request.POST.get('sdate','')
        e= request.POST.get('edate','')
        request.session["sdate"]=s
        request.session["edate"]=e
        if book.objects.filter(enddate__gt=s):
            c=book.objects.filter(enddate__gt=s)
            for i in c:
              vnm=i.v_num
              x=vehicle.objects.filter(v_num=vnm).update(bstatus=1)
        else:
           c=book.objects.filter(enddate__lt=s)
           for i in c:
              vnm=i.v_num
              x=vehicle.objects.filter(v_num=vnm).update(bstatus=0)          
        g=vehicle.objects.all()
        for i in g:
            if vehicle.objects.filter(bstatus=1):
                messages.warning(request,'no vehicle available')
            if vehicle.objects.filter(bstatus=0):
                d=vehicle.objects.filter(bstatus=0)
            return render(request,'shop/list.html',locals())   
    return render(request,'shop/list.html',locals())   