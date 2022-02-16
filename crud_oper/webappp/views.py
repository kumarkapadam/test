from django.shortcuts import render, redirect

# Create your views here.
from webappp.forms import EmployeeForm
from webappp.models import *


def retrive(request):
    emp = Employee.objects.all()
    my_dict = {'emp': emp}
    return render(request, 'webappp/display.html', context=my_dict)


def create(request):
    form = EmployeeForm()
    my_dict = {'form': form}
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/display/")

    return render(request, 'webappp/create.html', context=my_dict)


def update_view(request, id):
    employee = Employee.objects.get(id=id)
    my_dict = {'employee': employee}
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/display/')

    return render(request, 'webappp/update.html', context=my_dict)


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/display/")


def index():
    return None