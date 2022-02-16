"""
Tell me about yourself
Roles and responsibilities
About the project
Experience in Flask and django(years)
List vs Sets
Memory Management in python
Pickling and unpickling
Method overloading in python
Class methods and instance methods
Instance variables can access class variables
Append and extend
Decorators
Call by refrence and call by value
Shallow copy and Deep copy
Circular Import
Avoid circular import
Generator and Iterator
_init.py_ uses
Method resolution order
how import works
Django vs Flask
Middleware
Signals in django
gunicorn in mongodb

Mongodb wth django
make migrations  # its generates  sql commands
migrate          # its executes sql commands
allowed_host in settings.py    #
authentication in flask and django #
==============================================================================
The Questions
1.Roles and Responsibilities
2.Instance Variable
3.Static Variable
4.Class Variable
5.Pickling and Unpickling
6.diff between Django and Flask
7.List Vs Set
8.Diff Between Append() and Extend() in List
9.Shallow Copy and Deep Copy
10. Diff Between Iterator vs Generator
11.Is Python Call by Value or Call By Reference
12.Middleware Classes in Django
13.Signals in Django
14.why django is a full stack Web framework
15.Diff Between  migrate and make migrations
16.what is Allowed_Hosts in  Django
17.what is NoSQL Database


19.sessions in Django
20.architechture of Django
21.Jinja2 Template
22. Decorators in python



"""

# architechture of Django
"""
The Django is a free and open-source web application framework that is written in Python language. 
The initial version of Django is released on 15th July 2005, which is developed by Django Software Foundation.
The main advantages of Django is to make the creation of complicated database included web applications as easy as possible, 
it is fast, many components are available implicitly, scalability and good security.
M stands for Model
V stands for View
T stands for Template


Django Architecture Model
==============================
In Django, the model does the linking to the database and each model gets mapped to a single table in the database. 
These fields and methods are declared under the file models.py
With this linking to the database, we can actually each and every record or row from that particular table and can perform 
the DML operations on the table.
Django.db.models.The model is the subclass that is used here. We can use the import statement by defining as from django.
db import models.
So after defining our database tables, columns and records; we are going to get the data linked 
to our application by defining the mapping in settings.py file under the INSTALLED_APPS.
Django View
This is the part where actually we would be mentioning our logic. This coding is done through the python file views.py
This view also sends responses to the user when the application is used, to understand briefly, we can say that this view.py can deal with HttpResponse.
Now, after creating a view, how can we link it to our application? How do you think that the system is going to understand to display a particular view? This can be done by mapping the views.py in urls.py file. As already mentioned, urls.py keeps track of all those different pages that we created and hence map each of them.
Django Template
This template helps us to create a dynamic website in an easy manner. The dynamic website deals with dynamic data. Dynamic data deals with a scenario where each user is displayed with their personalized data; as Facebook feeds, Instagram feeds, etc.
The configuration of the template is done in settings.py file under INSTALLED_APPS. So python code would search for the files under the template subdirectory. We can create an HTML file or import any dynamic web page from the browser and place it under the template folder.
And after that our usual linking of this file in urls.py and views.py to get a response is mandatory.
In this way after linking all these together and running the server, we can get our web application ready.
Django Template Language
In short, it is called as DTL. Django template has its own syntax in rendering the data on to the web page. For displaying a dynamic variable, the variable name is written inside the curly braces; denoted by “{{variable_name}}”. And to write if conditions, the syntax would be defined as: {% if condition %}. The same would be followed for the end if syntax also. Django uses render function in DTL. This render function takes three parameters.

Request
Mentioning the path of template in settings.py
Parameters that contain all variables and can create as many as possible.
By these render functions we can have our DTL to make dynamic web pages.

"""

# jinja templates
"""A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). 
A Jinja template doesn’t need to have a specific extension: .html, .xml, or any other extension is just fine.

A template contains variables and/or expressions, which get replaced with values when a template is rendered; 
and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python."""

# decarators in python
"""Python has an interesting feature called decorators to add functionality to an existing code.

This is also called metaprog ramming because a part of the program tries to modify another part of the program at compile time."""

"""
The difference between makemigrations and migrate is this: make migrations auto generates migration files containing 
changes that need to be applied to the database, but doesn't do migrate will make the actual modifications to your database.


migrate will make the actual modifications to your database, based on the migration files.
"""

# pickling and unpickling

"""In Python, pickling is the process by which Python objects are converted to byte streams. Pickling is about serializing the object structure in python."""

# Method overloading in python

"""


"""

# Signals in django
"""  

"""

# how import works
"""

he import keyword in Python is used to load other Python source code files in to the current interpreter session.
 This is how you re-use code and share it among multiple files or different projects.


When you import a package it runs the __init__.py file inside the package directory.
When you execute a package (e.g. python -m my_package) it executes the __main__.py file.
When you import a module it runs the entire file from top to bottom.
When you execute a module ir runs the entire file from top-to-bottom and sets the __name__ variable to the string "__main__".

"""

#  18.diff between union and union all in SQL Query
""" All is that Union extracts the rows that are being specified in the query while Union 
All extracts all the rows including the duplicates (repeated values) from both the queries  """

"""

ALLOWED_HOSTS
ALLOWED_HOSTS is list having addresses of all domains which can run your Django Project. 
 

When DEBUG set to True 
ALLOWED_HOSTS can be an empty list i.e. ALLOWED_HOSTS=[ ] because by Default it is 127.0.0.1 or localhost 
When DEBUG set to False 
ALLOWED_HOSTS can not be an empty list. We have to give hosts name in list. i.e. ALLOWED_HOSTS=[“127.0.0.1”, “*.heroku.com”].
 “127.0.0.1” represents Your PC, “*.heroku.com” represents this application can be run on heroku also. 
 

 

INSTALLED_APPS
In this section, we mention all apps that will be used in our Django project.
 Previously we made an app polls we have to tell Django its existence To do so have to put into INSTALLED_APPS: 
 

    INSTALLED_APPS = [
        // Some preloaded apps by Django,
        'polls', // don't forget to quote it and also commas after every app
]
 """

# roles and responsibilities
# Django vs flask 8/10
# flask vs Django
# create rest api in Django
# exception handling in flask
"""
Why Is It Important to Handle Exceptions in Flask?
Enables the smooth flow of programs:
===================================
Handling exceptions at every possible aspect allows your code to run smoothly regardless of any errors

Security purposes:
================== 
Handling exceptions from a security point also helps secure your programs since you’re unlikely
to leak or expose your code’s configurations to random people


"""

# db conneciton in flask
"""
import sqlite3
from flask import g # g and current_app object
current_app.config['DATABASE'] = 'MYDB' # Name of the database
 
def get_db():
    '''A method to get the database connection'''
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row 
 
   return g.db
def close_db(e=None):
    '''A method to close the database connection'''
    db = g.pop('db', None)    
if db is not None:
        db.close()


"""
# authenitication in falsk
# get vs filter in django
# django authentication
# authitnication vs authoization
# check authorization in django
# token based in rest api
# serlizers in django
# signals in django
# decorators in django
# acid in django
# queue based system kafka
# micro services in flask
# deployment in projects
# max salary of each department in sql
# indexing in sql
# template in djagno dashboard


