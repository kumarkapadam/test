from django.shortcuts import render, redirect
from .models import Stundent_data

# Create your views here.

def index(request):
    data=Stundent_data.objects.all()
    context = {'data':data}
    return render(request, "crudapp/index.html",context)





def insert(request):
   # data = Stundent_data.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name,email,age,gender)
        query = Stundent_data(name=name , email=email,age = age , gender=gender)
        query.save()
    return render(request,'crudapp/index.html')

def update(request,id):
    data=Stundent_data.objects.all()
    context = {'data':data}
    return render(request, "crudapp/edit.html",context)



def index(request):
    data=Stundent_data.objects.all()
    context = {'data':data}
    return render(request, "crudapp/index.html",context)