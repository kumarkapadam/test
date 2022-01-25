"""

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
----------------------------------------------------------------- -->   if we use migrate command ,then all the
django related tables will be created in addition to our application specific tables --->  if we create the table
manually using sql code then only our application specific table will be created and django may not work properly
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

authentication :: it is the process of validating the user  ex--signup authorization  ::   it is the process of
validating/verify  the accessed data of the user and providing the permission to user (or) it is the process of
validating/verify  the accessed data checking whether  its correct or not validations ex--signin

"""