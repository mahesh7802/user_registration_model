from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
# Create your views here.

def registration(request):
    d={'usfo':UserForm,'pfo':ProfileForm}
    if request.method=='POST' and request.FILES:
        usfd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if usfd.is_valid() and pfd.is_valid():
            NSUFO=usfd.save(commit=False)
            submitedpw=usfd.cleaned_data['password']
            NSUFO.set_password(submitedpw)
            NSUFO.save()
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUFO
            NSPO.save()
            return HttpResponse('<center>Registration is successfully</center>')
    return render(request,'registration.html',d)
