from dataclasses import fields
from logging import error
from sre_constants import IN
from tkinter.ttk import Widget
from turtle import textinput, width
from django.core import validators
from django import forms
from .models import landing_pageRegistrationForm
#from phonenumber_field.formfields import PhoneNumberField
#from phonenumber_field.widgets import PhoneNumberPrefixWidget

class landing_pageleads(forms.ModelForm):
     error_css_class = 'error'
     required_css_class ='required'
     class Meta:
        model = landing_pageRegistrationForm
        fields = ['name','email']
        labels = {'name': 'Name', 'email': 'Email id'}
        error_messages = {  'name':{'required':'Please enter your full name'},
                            'email':{'required':'Please enter the email id'},
                            #'phone':{'required':'Please Enter valid Mobile number eg. +911234567899'}
        }
        
        widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Candidate name'}),
                    'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Correct Email Id'}),
                    #'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'+910000000000'}),
                    
        }
        #phone = PhoneNumberField(widget = PhoneNumberPrefixWidget(initial='IN'))
        
        