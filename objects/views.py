from django.shortcuts import render
from django.http import HttpResponse

def device(request):
    a=0
    return render(request,"device.html",None)

def partner(request):
    return render(request,"partner.html",None)

def worker(request):
    return render(request,"worker.html",None)

def create_device(request):
    a=0
    return render(request,"device.html",None)

def create_partner(request):
    return render(request,"partner.html",None)

def create_worker(request):
    return render(request,"worker.html",None)
