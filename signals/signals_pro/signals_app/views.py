from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver


# Create your views here.


def index(request):
    return HttpResponse("<h1> hellooo </h1>")



@receiver(request_finished)
def my_callback(sender , **kwargs):
    print("request finished")

