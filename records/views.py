from django.shortcuts import render

def logbook_reports(request):
    return render(request,"reports.html",None)

def service_orders(request):
    return render(request,"orders.html",None)

def device_recalls(request):
    return render(request,"recalls.html",None)
