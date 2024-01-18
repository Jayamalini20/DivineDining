from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Contact
from first_app.models import Contact2
from first_app.models import Res


def index(request):
    if request.method=="POST":
        name2=request.POST.get('name2')
        email2=request.POST.get('email2')
        phone2=request.POST.get('phone2')
        index=Contact2(name2=name2, email2=email2, phone2=phone2)
        index.save()
    return render(request,"index.html")
def zomato(request):
     if request.method=="POST":
            Restaurant=request.POST.get('Restaurant')
            zomato=Res(Restaurant=Restaurant)
            zomato.save()
     return render(request,"zomato.html")

