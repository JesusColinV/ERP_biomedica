from django.shortcuts import render

def create_device(request):
    return render(
        request,
        "new_device.html",
        {
            "name":"a",
            "serie":"b",
            "description":"c"
        }
        )

def create_partner(request):
    return render(request,"new_partner.html",None)

def create_people(request):
    return render(request,"new_people.html",None)

def delete_object(request):
    return render(request,"object.html",None)