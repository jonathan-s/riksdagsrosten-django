# Riksdagsrösten
=======================

To start developing on riksdagsrösten you can follow the instructions below. 

Installation
------------

    git clone git address here. 

After you've installed the project template start a virtual environment where you have pip installed and run:
    
    sudo sh env.py

That script will install all the requirements for this project template. It will also set the environment variable so that you will be working with the local settings and no other settings as well as set the secret key environment variable. 

For the time being ask Jonathan Sundqvist about env.py if you want to play around locally. 

## Developing with Livereload
--------------------------

You need to have nodeJS installed and `grunt-cli`. 

install grunt-cli by `npm install -g grunt-cli`

Package.json contains all the dependencies for running livereload. Follow the instructions below and grunt will be installed and it will watch any changes for html and CSS files. 

1. Change to the project's root directory
2. Install project dependencies with `npm install`
3. Run Grunt with grunt

When starting the server you have to set the live-reload port the following way: `python manage.py runserver --livereload-port 22220`

## Features to be added
-----------------------
If you would like other features, please start a discussion on github issues and we'll see what we can do. 
