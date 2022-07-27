from tkinter import Label
from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=400)
    address = forms.CharField(label="Address", max_length=400)