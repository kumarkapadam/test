"""
_25_Django   : it is a free and opensourse web framework
django will make use of python
python ---official website www.python.org
django--- djangoproject.com



django was create in 2003 as an internal project at lowrence journal word news paper
officially django framework was released as open source framework july21st 2005
adrian holovaty and simson willison invented django frameworrk
django was named in the memory of guitarist "django rainhard"
django software foundation will maintan django framework
it is used by several top websites like  youtube insta google nasa

features of django:
-------------------

fast
secured
full loaded
scalability(it meets heavy demand (100users,1000 users)
versatile(small app,big app,scientific application



Rest API:( representational state transfor)
--------
prerequisites : python + django

basic terminalogy :
 API --- application of programming interface


========================================================================
Ip address ::check the ip address of local machine
            in cmd > ipconfig  > IPv4 configure


port number ::
port number is the address / unique number generated scheduler under the control of os
port no will be used to executed the process tasks present on the ram



------------------------------------------
web servers::
1.tomcat
2.glassfish
3.IIFS(internet informatio security) (microsoft)
4.jetty
5.resin


-----------------------------------------------

install django :
------------------
 cmd prompt > pip install django==version
 pip3 install django
 python -m pip install django


pip update ::     python -m pip install --upgrade pip

how to know which version  we are  using ::
--------------------------------------------
django-admin --version
pip show django
pip show django --version



difference between project and  application
-------------------------------------------------
 project is collection of application and their corresponding configuration files
 application is a group of programs which are used to perform some tasks

pluggable django application :
-----------------------------
the django application can be plugged into other projects we can reuse the django apllication


===============================================================================================
how to create django project :
-----------------------------
django-admin startproject project_name

ex: django-admin startproject first_project

              first_project   --->main package
                    first_project  ---> sub package
                           __init__
                           asgi.py
                           settings.py
                           urls.py
                           wsgi.py
                    manage.py

    all are project level configuration files

command used to run project::
-------------------------------
       python manage.py runserver
       py manage.py runserver

steps  to run django development server:
------------------------------------------
python manage.py ruserver
copy url
oepn any webbrowser
send the req pasting url in any
we will get the response

=====================================================
create a first project :
create a project:
-------------------
              django-admin startproject project_name
create app:
---------------
             cd project
             inside the project

             django-admin startapp webapp
             python manage.py startapp webapp

                            webapp
                              __init__
                              admin.py
                              apps.py
                              models.py
                              tests.py
                              views.py




**************create a django project to display the welcome msg

webbrowser -- request --- internet
interner -----response --- webbrowser

internet -----request ---webserver
webserver---response ---internet

         webserver ===-----settings.py -----urls.py -----views.py

views.py  responce to webserver




django development server:8000


execution  of python program
------------------------------
3 ways
 1.online editor
 2.python idle
 3.ide's



settings.py
---------------
        installedapps ---- add the app in installed apps
                           and check the root url
urls.py
-----------




views.py:
------------
        from django.shortcuts import render
        from django.http import HttpResponse

        def display(request):
              return HttpResponse("")


functions:
----------
    a function is a set statements that takes nput and perform some operat
 incase of python we can define functions in 2 days
 1.using def keyword
 2.using lambda keyword

4 types of fuunction:
   user defined ---- function which are defined user explisiltly according to customer requirements
   lambda
   builtin
   recursive


modules:

packages :
----------

Instagram application:
 login.py ::
        username
        password
  homepage.py
  chat.py
  stories.py
  block.py
  logout.py


project2:::
-------------------
django-admin startproject projectname
cd projectname

django-admin startapp webapp




import datetime

now_time = datetime.datetime.now()
print("now time is :",now_time)
hour = datetime.datetime.now().hour
print(hour)

if hour>0 and hour > 12:
    print("morning")




we can create a multiple projects and mulriple apps and all views assign a one url

like in urls.py


from appname import views as v1
from appname import views as v2
from appname import views as v3

urlpatterns =[
path(),v1.views
path(),v2.views
]

creation of multiple URL patterns at project level
---------------------------------------------------

 using django framework develop the project which consists of
multiple url at the project level

----it is clumsy

project :::

settings.py
urls.py
    3apps
        views.py ---> bangaloreapp
        views.py ----> mysureapp
        views.py ---> hublicovidapp




create application inside url
--------------------------------
from django.urls import path
from appname import views as v1

urlpatterns = [
path('',v1.function_name)
]



project :

from django.urls import path,include

path("",include('appname.urls')),




==============================================================================
(10-video)_25_Django-templates:
----------------
main project create a folder name should be "templates"
templates create a folder app
then create a html file


 settings.py

TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

urls.py


views.py

from django.shortcuts import render
def function_name(request):
      return render(request =request,template_name =appname/.html file


note:
-----
--> according to the requirements we can use Templates in python file
-->templates folder has to be created within the main project level folder
-->we can create multiple html files at the templetes folder
-->
views.py is used to write business logic
using template based project approchh we can increase the modularity,codereusability,code redability


static_files:::
---------------



=====================
package -name ---Djanerio




"""
"""
num = int(input("enter no of subjects:"))
dict = {}
count = 0
for i in range(num):
    sub_name = input("enter name")
    sub_marks = int(input("enter marks"))
    dict[sub_name]=sub_marks

print(dict)
sum =0
for i,j in dict.items():
    count+=1
    sum+=j
    if count == num:
        avg = sum /count
        print(avg)

"""


"""
static ::
-------------
go to main project and create static directory(folder) ,
   and then create app name and css folder  and images folder
   
   css folder:
       .css file
    static folder
   



#### update static path in settings.py 

STATIC_DIR = os.path.join(BASE_DIR,'static')

STATICFILES_DIRS  = [STATIC_DIR]


.css file:
-----------
<! DOCTYPE html>
{% load static %}
<link rel ="stylesheet" type = "text/css"  href = "{% static "appname/css/.css file" %}"
<img src="{% static "appname/images/.jpg" %}


=============================================================================
redirection of html files using bootstrap:
------------------------------------------
11th video

=============================================================================
12th video:
----------
  
database ::

CRUD operations


create ---- insert
retrive ---read
update ---update
delete----delete




create _models
=========================

models.py
--------------
            from django.db import models
            
            class Student(models.Model):
                  name = models.Charfield(max_length=15)
                  age  = models.Integerfield()
                  address = models.CharField(max_length=40)

import Student class import admin.py


admin.py
----------


from django.contrib import admin
from dbapp.models import Student 


class StudentAdmin(admin.ModelAdmin):
        list_display = ['name','age']        


admin.site.register(Student,StudentAdmin)



------------
python manage.py makemigrations   # it only used convert python code to sql query
python manage.py migrate    # create a table
python manage.py createsuperuser
 

ORM :::(object relational mapper)
--------
_25_Django follows ORM ,these technique convert python class into database  details


difference between makemigrations and migration
____________________________________________________

makemigrations is responsible to generate SQL code for python model class
whereas migrate is responsible to execute that SQl code so that table will be created in the database


advatage / importance of creating table using migrate command:
-----------------------------------------------------------------
-->   if we use migrate command ,then all the django related tables will be created in addition to our application specific tables
--->  if we create the table manually using sql code then only our application specific table will be created and django may not work properly
---> hence we have to create table s with migrate command

checking django database connection
======================================
command in cmd ::::::  python manage.py shell
      (interactiveconsole )
      >>>  from django.db import connection  # create connection
      >>>   my_cursor = connection.cursor()   # create curson
      >>>   quit()
 



install mysql:::
----------------
pip install mysqlclient


in settings.py:
------------------------
DATABASE ={
  'default':{
  'ENGINE':
  'USER':
  'PASSWORD' :
  'HOST' :
  'PORT':
   }
}


models.py
=========
class Student:
         
      def __str__(self):
           return self.name     
         

  
get :::
--------
1.. we can use GET method to get the information from the server
2.. Using GET method we can only read the data
3..GEt is one of the HTTP method using while submitting the form data        
4.it is a default http method when submitting the form data
5.when GET is used ,the form data will be visible in the page address bar
6.. never use get to send the confidential data,because it is less secured
7.length of url is limited 2048
8..we can send more than 2kb data
post:::
-------
1..we can use POST method to post the information to the server
2..Using POST method we can write and update the data
3.same
4.it is not a default Http method
5.it is not visible
6.POST is used send the  confidential data,because it is secured
7.no limited


=============================================================================== 
FORM validation :::
-----------------------
we can validate the data/input entered by the end user machanism is called 
 
 
 
 we can implement validation logic in django by using 4 ways
 
 1. Explicitly by the programmers by using clean_fieldname methods
                clean_fieldname
 
 
 
===== >>>>  validating the forms explicitly by the programmers by using clean_fielddname methods:
 create a project 
 and app create
 
 
 create template folder : 
         templates
              appname
                 home.html
                 feedback.html
                thanks.html

settings.py ::
--------------
add TEMPLATE_DIR

urls.py (mainproject)
---------

urls.py(app)
-----------
from django.urls import path
from studentapp import views


urlpatterns =[
            path('homepage',views.home_page),
            path('feedback',views.feedback_data),
            path('thankyou',views.thank_you)


]  


        

models.py
-------






forms.py
--------
from django import forms


class Studentform(form.Form)

     name = forms.Charfield()
     mail_id = forms.EmailField()
     feedback = forms.Charfield(widget = forms.Textarea)
     
     
     
     def clean_name(self):
          input_name = self.cleaned_data['name',]
          print("validation of name field')
                
          :return input_name         
                







authentication and authorization
==================================

authentication :: it is the process of validating the user  ex--signup
authorization  ::   it is the process of validating/verify  the accessed data of the user and providing the permission to user (or)
                    it is the process of validating/verify  the accessed data checking whether  its correct or not validations
ex--signin


NOTE : generally in any web application there will be a proper authentication and autherizarion process inorder to acces the content from that web application
        the user should be a valid user
        ---
        inorder to do this activiries in django it will provide the builtin  access using a application auth application(default application)
        
        built in module :: contrib.auth
        
        auth is the module present within django.contrib
        auth application is the authentication application in django framework
        auth application internally  uses content types application ehich is present within django.contrib
        bydefault these application would be present within serrings.py under the section INSTALLED_APPS
        
CREATE A PROJECT ::
django-admin startproject projectname
python manage.py startproject projectname
py -m django  startproject projectnam
   
### bydefault django provide
<a class="nav-link" href="/accounts/login">login</a>
<a class="nav-link" href="/accounts/logout">logout</a>


in urls path :::

import include

path('accounts/",include(django.contrib.auth.   urls)





django_ORM::
DJANGO follows ORM technique to convert python code into query code


models.py 

from django.db import models

class Student(models.Model):
     name = models.charfield(max_length=20)
     age = models.integerfield()
     city = models.charfield()


python manage.py makemigrations
python manage.py migrate  
python manage.py create superuser


  
"""


"""
unit-testing:
===============
unit testing is a software testing method by which individual units of source code are tested to determine whether they are fit for use

why unit test :
===============
 tests reduce bugs in new fearures and existing features
 tests ate good documentation
 tests reduce the cost of change
 faster debugging
 faster development
better design


unit test frame works :
unittest : in the python standard library
nose  : Not in the standard library .simpler tests than unittest
pytest : Not in the python standard library


pip install pytest

pytest -h                 (help command)





math_test.py
            def add(x, y=2):
                return x + y
            def product(x, y=2):
                return x * y



import math_test


def test_add():
    assert math_test.add(10, 12) == 22
    assert math_test.add(10) == 12


def test_product():
    assert math_test.product(10) == 20

# >>> pytest test_math_test .py :: test_add


>pytest -v -k  "add"  # any function name

>pytest -v -m number

import pytest
@pytest.mark.strings
def test_add_strings():
     result = math_func.add('hello','world')
     assert result =='hello world'
     assert type(result) is str
     assert 'Hello' in result


"""