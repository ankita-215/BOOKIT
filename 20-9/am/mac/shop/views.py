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
from django.views.generic import ListView, CreateView, UpdateView,View
from django.urls import reverse_lazy
from .models import Person
#**************************************************************
from shop.utils import render_to_pdf
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from datetime import datetime,date
#***********************************
import datetime
import json
#**************************

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
            subject = 'submit your query here'
            message = request.POST.get('message','')
            email_from = request.POST.get('email','')
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'shop/contactus.html')
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
                request.session["user"]=reg.email    
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
          messages.warning(request,'invalid username and password!!')
          return render(request,'shop/login.html')
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
    r=vehicle.objects.all()
    if request.method == 'POST': 
        form = v(request.POST, request.FILES)
        if form.is_valid(): 
                vupload= form.save(commit=False)
                vupload.email=d1.email
                g=vupload.v_num
                if vehicle.objects.filter(v_num=g):
                    messages.warning("this vehicle is already presanted")
                vupload.save()
                messages.success(request,'sucessfully upload')           
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
   r=d.price+1*float(request.session["diff"])
   request.session["pr"]=r
   request.session['num']=d.v_num
   request.session["id"]=d.vid
   return render(request, 'shop/quickview.html', {'v':v[0],'r':r})

def dview(request,myid):  
   v= driver.objects.filter(did=myid)
   d = driver.objects.get(did=myid)
  # r=d.price+1*float(request.session["diff"])
   #request.session["pr"]=r
   #request.session['num']=d.v_num
   request.session["id"]=d.did
   return render(request, 'shop/dview.html', {'v':v[0]})

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

def book1(request,*args, **kwargs):
    storage=messages.get_messages(request)
    storage.used=True
    v= vehicle.objects.filter(v_num=request.session['num'])
    d = vehicle.objects.get(v_num=request.session['num'])
    s=date.today()
    if request.method == 'POST': 
       
        form = BookingForm(request.POST, request.FILES) 
        if form.is_valid(): 
          book1= form.save(commit=False)
          
          #book1.v_num= book.objects.get(v_num=request.session['num'])
            
          book1.v_num=d.v_num
          book1.startdate=request.session['sdate']
          book1.enddate=request.session['edate']
          book1.amount=request.session['pr']
          book1.save()
          
          messages.success(request,'booking sucessfully!')
          template = get_template('shop/invioce.html')
          context = {'e':book1,'s':s }
          html = template.render(context)
          pdf = render_to_pdf('shop/invioce.html', context)
          if pdf:
              response = HttpResponse(pdf, content_type='application/pdf')
              filename = "Invoice.pdf" 
              content = "inline; filename='%s'" %(filename)
              download = request.GET.get("download")
              
              subject = 'Welcome to BOOKIT Portal.'
              message = 'Thank you for being part of us. \n We are glad to have you. \n Regards'

              from_email = settings.EMAIL_HOST_USER
              to_list = [book1.email]

              message = EmailMessage(subject, message, from_email, to_list)
              
              if download:
                  content = "attachment; filename='%s'" %(filename)
              response['Content-Disposition'] = content
              message.attach(filename,content, 'application/pdf')
              message.send()
              return response

          return HttpResponse("Not found")
         
    else: 
        form = BookingForm() 
        return render(request, 'shop/book_form.html',{'form':form,'v':v[0],'s':s}) 
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
    elif vehicle.objects.filter(email=request.session['mail']).exists():
      user = vehicle.objects.get(email=request.session['mail'])
      form = editV(instance=user)
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
       if register.objects.filter(id=F_id).exists():
          register.objects.get(id=F_id).delete()
          messages.success(request,'rejected sucessfully')
          return redirect('authorized.html')
       elif driver.objects.filter(did=F_id).exists():
          driver.objects.get(did=F_id).delete()            
          messages.success(request,'rejected sucessfully')
          return redirect('authorized.html') 
       elif admin1.objects.filter(aid=F_id).exists():
          admin1.objects.get(aid=F_id).delete()            
          messages.success(request,'rejected sucessfully')
          return redirect('authorized.html')
       elif vehicle.objects.filter(vid=F_id).exists():
          vehicle.objects.get(vid=F_id).delete()            
          messages.success(request,'rejected sucessfully')
          return redirect('authorized.html')
       return redirect('shop/authorized.html')
           
  #accept Farmer request
def accept(request,F_id):
      a=register.objects.filter(id=F_id).update(status=1)
      b=driver.objects.filter(did=F_id).update(status=1)
      c=admin1.objects.filter(aid=F_id).update(status=1)
      d=vehicle.objects.filter(vid=F_id).update(status=1) 
      if a:
        e=register.objects.get(id=F_id)      
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
        e=admin1.objects.get(aid=F_id)      
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
     if vehicle.objects.filter(email=request.session['dri']).exists():
         a=vehicle.objects.filter(email=request.session['dri'])
         for i in a:
             if book.objects.filter(v_num=i.v_num).exists():
                  c=book.objects.filter(v_num=i.v_num)    
                  return render(request,'shop/blist.html',{'c':c})    
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
        ci=request.POST.get('city','')
        request.session["diff"]=request.POST.get('leave','')
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
            if vehicle.objects.filter(bstatus=1).filter(city=ci):
                messages.warning(request,'no vehicle available')
            if vehicle.objects.filter(bstatus=0).filter(city=ci):
                d=vehicle.objects.filter(bstatus=0).filter(city=ci)
            return render(request,'shop/list.html',locals())   
    return render(request,'shop/list.html',locals())   


def GeneratePDF(request,id,*args, **kwargs):
          return HttpResponse("Not found")

def ulog(request):
   u=book.objects.filter(email=request.session["user"])
   if (request.POST.get('DeleteButton')):
        book.objects.filter(bid = request.POST.get('DeleteButton')).delete()
        
   return render(request,'shop/ulog.html',{'u':u})

def editveh(request,myid):
     if vehicle.objects.filter(vid=myid).exists():
      user = vehicle.objects.get(vid=myid)
      form = editV(instance=user)
      if request.method == "POST":
        form =editV(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)            
          update.user = user
          update.save()    
          messages.success(request,'Your profile update Successfully')       
    
     return render(request,'shop/eveh.html', {'form': form})

def dbook1(request,*args, **kwargs):
    storage=messages.get_messages(request)
    storage.used=True
    s=date.today()
    v= driver.objects.filter(did=request.session['id'])
    d = driver.objects.get(did=request.session['id'])
    if request.method == 'POST': 
       
        form = dBookingForm(request.POST, request.FILES) 
        if form.is_valid(): 
          dbook1= form.save(commit=False)
          dbook1.startdate=request.session['sdate']
          dbook1.enddate=request.session['edate']
          #dbook1.amount=request.session['pr']
          dbook1.save()
          
          messages.success(request,'booking sucessfully!')
          return render(request, 'shop/dbook.html',{'form':form,'s':s,'v':v[0]})
        else: 
          form = dBookingForm() 
          return render(request, 'shop/dbook.html',{'form':form,'s':s,'v':v[0]}) 
    return render(request, 'shop/dbook.html',{'s':s,'v':v[0]}) 

def dblist(request):
    if request.method == 'POST':
        s= request.POST.get('sdate','')
        e= request.POST.get('edate','')
        ci=request.POST.get('city','')
        request.session["diff"]=request.POST.get('leave','')
        request.session["sddate"]=s
        request.session["eddate"]=e
        if dbook.objects.filter(enddate__gt=s):
            c=dbook.objects.filter(enddate__gt=s)
            for i in c:
              id=i.did
              x=driver.objects.filter(did=id).update(bstatus=1)
             
        else:
           c=dbook.objects.filter(enddate__lt=s)
           for i in c:
              id=i.did
              x=driver.objects.filter(did=id).update(bstatus=0)          
            
        g=driver.objects.all()
        for i in g:
            if driver.objects.filter(bstatus=1).filter(city=ci):
                messages.warning(request,'no vehicle available')
            if driver.objects.filter(bstatus=0).filter(city=ci):
                d=driver.objects.filter(bstatus=0).filter(city=ci)
            return render(request,'shop/dblist.html',locals())   
    return render(request,'shop/dblist.html',locals())   
