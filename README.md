Django Project template
=======================

A django project template with my preferences

Installation
------------

To use the project template when starting a Django project you only need to type: 

    django-admin.py startproject --template=https://github.com/jonathan-s/Django-Project-template/archive/master.zip project_name

After you've installed the project template start a virtual environment where you have pip installed and run:
    
    sudo sh env.sh 

That script will install all the requirements for this project template. It will also set the environment variable so that you will be working with the local settings and no other settings as well as set the secret key environment variable. 

Todo
-----
- Fix installing requirements automatically
- Fix dev settings
- Possibly setting up postgres automatically
- 

Developing with Livereload
--------------------------

You need to have nodeJS installed and `grunt-cli`. 

install grunt-cli by `npm install -g grunt-cli`

Package.json contains all the dependencies for running livereload. Follow the instructions below and grunt will be installed and it will watch any changes for html and CSS files. 

1. Change to the project's root directory
2. Install project dependencies with `npm install`
3. Run Grunt with grunt