from operator import imod
from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect
from .forms import landing_pageleads
from .models import landing_pageRegistrationForm

# Create your views here.

def landing_page(request):
      if request.method =='POST':
            leads = landing_pageleads(request.POST)
            if leads.is_valid():
                  name = leads.cleaned_data['name']
                  email = leads.cleaned_data['email']
                  phone = leads.cleaned_data['phone']
                  lead = landing_pageRegistrationForm(name=name, email=email)
                  lead.save()
                  return HttpResponseRedirect('/')
            else:
                  print('Incorrect data, not saved to db')

      else:
            leads = landing_pageleads()
      return render(request,'index.html',{"leads":leads})

def studymat(request):
      return render(request,'studymaterials.html')


def scholarships(request):
      return render(request,'scholarships.html')

def buycourse(request):
      return render(request,'course.html')

def about(request):
      return render(request,'about.html')

def career(request):
      return render(request,'career.html')

def child(request):
      return render(request,'child.html')

def privacy(request):
      return render(request,'privacy.html')
def termscondition(request):
      return render(request,'termsandcondition.html')
def contact(request):
      return render(request,'contact.html')
       
    



    


