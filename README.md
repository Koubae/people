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
