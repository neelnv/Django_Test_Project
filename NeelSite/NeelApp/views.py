from django.http import response
from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewList

# Create your views here.
def homefunc(request):
    return render(request, 'Home.html')

def aboutfunc(request):
    return render(request, 'About.html')

def basicformfunc(request):
    if request.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            lead = CreateNewList(name=name, email=email, address=address)
            lead.save()
            # return HttpResponseRedirect('') ----------- How to make this work? Showing error when tried 
        else:
            print("Incorrect! Not stored to db")
    else:
        form = CreateNewList()
    return render(request, 'BasicForm.html', {"form":form})