
# PFMS - Personal Finance Management System

![PFMS Logo](https://shahriarhossain.com/pfms.shahriarhossain.com/Asset/Image/PFMS.png)

## It’s a Personal Finance Management System. A place where an individual can track personal finance. 
___

> [Demo](https://shahriarhossain1.pythonanywhere.com/)  
User Name: demo  
Password: pfms@demo1
___

> #### !!! Important !!!
> Just a heads up this repository is going to contain lots & lots of mistakes, ugly code & some bullshit logics.  
I am trying to learn as I build the project.  
Please let me know if you have any suggestions or if you find any Security Issue.  
Thank You.
___

### Different parts of the Project:

    1. Multiple Bank, Mobile finance & Cash in hand account. 
    2. Inter Account Transaction System.
    3. Income Record.
    4. Expanse Record.
    5. Dashboard with Income & Expense Summary (Charts).
    6. Investment Record & Tracking (Stock, Crypto) - Not in Real Time.

### Advance Feature:

    1. Bank statement analysis.
    2. Family / Joint account system.
    3. Personal Balance sheet.


### Technology Stack For The Project (initial planning):

    * Front End: Html, Css, Js, Bootstrap
    * Back End: Python  - Framework ( Django)
    * Charts : Haven't decide yet
    * Database : sqlite3 (Development)

# Installation Guide

* ### Clone this repository
```sh
git clone https://github.com/Shahriar-Hossain-IT/PFMS.git
```
* ### Change Directories
```sh
cd PFMS
```
* ### Create Virtual Environment
```powershell
python3 -m venv venv
```
or
```powershell
python -m venv venv
```
* ### Activate the Virtual Environment
```powershell
venv\Scripts\activate
```
* ### Install Required package's
```powershell
pip install -r requirements.txt
```
* ### Change Directories
```sh
cd PFMS
```

* ### Create a file name secret.py and set this values

    SECRET_KEY = "Enter your SECRET_KEY" # [Create One](https://miniwebtool.com/django-secret-key-generator/)  #  

    ALLOWED_HOSTS = ['127.0.0.1']  # Add your host #

    DEBUG = True # (Set to False in Production) #  

    INTERNAL_IPS= ["127.0.0.1"]  # For Django Debug Toolbar - [Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)  #  

    TIME_ZONE = 'Enter Your Time Zone' # [Find Your Timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  (use the TZ databse name)  #  

* ### Make Migrations
```powershell
python3 manage.py makemigrations
```
or
```powershell
python manage.py makemigrations
```
* ### Migrate
```powershell
python3 manage.py migrate
```
or
```powershell
python manage.py migrate
```

* ### Create Super User
```powershell
python3 manage.py createsuperuser
```
or
```powershell
python manage.py createsuperuser
```
Enter Username , Email, & Password  
Remember this username & password you will need it to login.

* ### Run the server
```powershell
python3 manage.py runserver
```
or
```powershell
python manage.py runserver
```




