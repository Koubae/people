People!
======

_Django Social Media App - Social Networking called "People", built to learn the framework_


### What is it

Is a simple, non production ready, Social Media Web Application use for learning and meant to be used as an example. 

### Quick Start

* Make sure you have Python3.12 installed else please install via --> https://www.python.org/downloads/
* Install MySQL, preferably `MySQL 8`, should work in lower version but I developed using version 8 so can't guarantee it works for older ones.

```bash
git clone git@github.com:Koubae/people.git
cd people
# create Python environment 
python -m venv env 
# Activate (linux)
source env/bin/activate
# Activate (windows)
env/Scripts/activate.bat

# Install 
python -m pip install requirements.txt
# Go Inside MySQL
mysql -u<user> -p<password
# create database 'people'
mysql> CREATE DATABASE people;
mysql> USE people;
mysql> SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| people     |
+------------+
# exit mysql 
mysql> exit

# Cool now, let's create migration to intialize the database
python manage.py makemigrations
python manage.py migrate

# run Django 
python manage.py runserver

# Now go to
localhost:8000
```

### Stack

* Python3.12
* Django 5
* Django Template _intentionally avoiding using any 'big' javascript framework in order to use Django Templating system_
* MySQL 8

### Specifications 

* [Model Structure](./model_structure.md)


Projects
---------------

### Plugin - Django Library and cool Projects

* [Datta Able Django](https://github.com/app-generator/django-datta-able)
* [Django Material Dashboard](https://github.com/app-generator/django-material-dashboard)


### Other Django Examples

_Here a list of some example I found in github and online_

* [django-realworld-example-app](https://github.com/gothinkster/django-realworld-example-app/tree/master)
* [My django project](https://github.com/mach1el/my-django)
* [E-Commerce Project For Baby Tools](https://github.com/MET-DEV/Django-E-Commerce)
* [example.django.mi_aplicacion](https://github.com/macagua/example.django.mi_aplicacion)
* [django-blog-example](https://github.com/rgab1508/django-blog-example)
* [simple-django-page](https://github.com/90x-Development/simple-django-page)
* [Simple Django Signals](https://github.com/BaseMax/SimpleDjangoSignals)
* [django-tutorial-step-by-step](https://github.com/consideratecode/django-tutorial-step-by-step)


Troubleshooting
---------------

To keep things more organize, rather than have the application in root of the repository, I moved it inside [app](./app) folder.
PyCharm by default starts and expect Django application to be developed at root level, so in order to make it work see the below article

In general simply do

1. Go to Settings --> Languages & Frameworks --> Django --> 
2. Modify `Django Project Root` and make it pointing to `app` 

Additionally you may want to change Run configuration of PyCharm, set `Working Directory` also to `app` folder


* [Getting Pycharm to run Django tests after moving the entire django source to a subfolder](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000622670-Getting-Pycharm-to-run-Django-tests-after-moving-the-entire-django-source-to-a-subfolder)


### PyCharm complaining about 'templates' folder

* [PyCharm code inspection complains template file not found, how to fix?](https://stackoverflow.com/questions/20873625/pycharm-code-inspection-complains-template-file-not-found-how-to-fix)


Further Reading
---------------

* [Organize django apps inside](https://stackoverflow.com/questions/73354083/organize-django-apps-inside)
* [When to create a new app (with startapp) in Django?](https://stackoverflow.com/questions/64237/when-to-create-a-new-app-with-startapp-in-django)