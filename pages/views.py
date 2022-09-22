from django.shortcuts import render
from django.http import HttpResponse

# Create your views here by creaating functions.
def home_view(*args,**kwargs):
    return HttpResponse("<h1>Hello, welcom to Django app</h1>")

def contact_view(*args,**kwargs):
    return HttpResponse("<h1>contact form: xxxxxxxx</h1>")