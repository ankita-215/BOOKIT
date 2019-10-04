from django import forms 
from .models import *
from django.conf import settings
from django.shortcuts import render  
from django.http import HttpRequest
import urllib


class v(forms.ModelForm): 
  
    class Meta: 

        model =vehicle
        fields = ['o_name','v_num','category','subcategory','address','Mono','city','Pincode','adharcard','policeverification','image','document','price','ex'] 
        
        labels = {
            "o_name": "Owner Name",
            "v_num":"Vehicle No",
            "category":"Category",
            "subcategory":"SubCategory",
            "image":"Vehicle Image",
            "document":"Document",
            "price":"Price",
            
            
        }
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['subcategory'].queryset = scat.objects.none()
        
         if 'category' in self.data:
                try:
                    c_id = int(self.data.get('category'))
                    self.fields['subcategory'].queryset = scat.objects.filter(id=c_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
         elif self.instance.pk:
                self.fields['subcategory'].queryset = self.instance.category.subcategory.order_by('name')
            

class adminreg(forms.ModelForm):

    class Meta:

        model=admin1
        fields=['email','password']  

class editU(forms.ModelForm): 
  
    class Meta: 

        model =register
        fields = ['name','address','Mono','city','Pincode','email','password'] 

class editD(forms.ModelForm): 
  
    class Meta: 

        model =driver
        fields = ['firstname','lastname','password','email','Mono','city','licence'] 

class editA(forms.ModelForm):

    class Meta:

        model=admin1
        fields=['email','password']   

class editV(forms.ModelForm):
    class Meta:
        model =vehicle
        fields = ['o_name','v_num','category','subcategory','address','Mono','city','Pincode','adharcard','policeverification','image','document','price','ex'] 
        
        labels = {
            "o_name": "Owner Name",
            "v_num":"Vehicle No",
            "category":"Category",
            "subcategory":"SubCategory",
            "image":"Vehicle Image",
            "document":"Document",
            "price":"Price",
            
            
        }
      
#*************************************************************************************
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
        
class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = book
        fields = ['name','Mono','email','Pincode','address','city','p']
        
        labels = {
            "name": "Name",
            "address":"Address",
            "Mono":"Mobile no",
            "city":"City",
            "p":"Departure point",
            "email":"Email",
            "Pincode":"Pincode",
            
            
        }
class dBookingForm(forms.ModelForm):
    
    class Meta:
        model = dbook
        fields = ['name','Mono','email','Pincode','address','city','p']
        
        labels = {
            "name": "Name",
            "address":"Address",
            "Mono":"Mobile no",
            "city":"City",
            "p":"Departure point",
            "email":"Email",
            "Pincode":"Pincode",
            
            
        }
        
     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['p'].queryset = P.objects.none()
        
       
  
        if 'city' in self.data:
            try:
                c_id= int(self.data.get('city'))
                self.fields['p'].queryset = P.objects.filter(c_id=c_id).order_by('name')
            
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['p'].queryset = self.instance.city.P.order_by('name')
        
