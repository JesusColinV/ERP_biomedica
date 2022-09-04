from django.shortcuts import render

def logbook_report(request):
    return render(request,"report.html",None)

def service_order(request):
    return render(request,"order.html",None)

def device_recall(request):
    return render(request,"recall.html",None)
