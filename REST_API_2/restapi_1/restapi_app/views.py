from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def student_data(request):
    data = {'eno':27,'name':'kumar','eage':'25','eaddress':'atp'}
    response = '<h1>Employee Number :{} <br> Employee Name :{} <br> employee age:{} <br> Employee Address :{} </h1>'.format(data['eno'],data['name'],data['eage'],data['eaddress'])
    return HttpResponse(response)


