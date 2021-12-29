"""

def registerpage(request):

    context = {}
    return render(request,'accounts/register.html',context)

def loginpage(request):
    contect = {}
    return render(request,"/login.html",contect)

def home(request):
    orders = order.objects.all()
    customers = order.objects.all()

    total_customers = customers.count()

    total_order =orders.count()
    delivered = orders.filter(status="delivered").count()
    pending = orders.filter(status="pending ").count()
    context = {'orders':orders,'customers':customers
               'total_orders':total_order,
               'delivered':delivered,
               'pending':pending}
    return render(request,'accounts/dashboard.html',context)






## registerpage

from django.contrib.auth.forms import UserCreationForm


def registerpage(request):
    form  = UserCreationForm()
    if request.method == 'post':
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()
    context = {}
    return render(request,'accounts/register.html',context)

forms.py::
--------
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import user

from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
class CreateUSerForm(UserCreationForm):
    class Meta:
        model = user
        fields = ["username",'email','password','pass2']





register.html
------------

<h3> Register </h3>
<form method="post" action ="">


{%  csrf_token %}
{{ form.username.label }}
{{ form.username }}


{{ form.email.label }}
{{ form.email }}


{{ form.password1.label }}
{{ form.password1}}

{{ form.password2.label }}
{{ form.password2 }}


""" 