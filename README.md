# celebrityComparer

## Prerequisites
1. Python 3.10 or above must be installed

## How To Run Program
1. Clone repository from GitHub
2. Create venv on command line in folder (python -m venv venv --upgrade-deps)
3. Activate venv 
4. Install requirements (pip install -r requirements.txt)
5. Set the API key in the environment using the console (set "X-RapidAPI-Key= <get key from Maya>")
6. Run the server (python manage.py runserver)
7. On the broswer, use the link http://127.0.0.1:8000/celebrity-ranking to open the program.

## Setup For Development
1. Install and activate venv : python -m venv venv --upgrade-deps 
2. Installing django package : pip install django 
3. Created project (celebrityComparer is the name of the project, . means in this directory) : django-admin startproject celebrityComparer . 
4. Creating app : python manage.py startapp celebrityRankingApp

## Testing 
1. Running the server : python manage.py runserver
2. URL : http://127.0.0.1:8000/

## Websites used
1. Bootstrap

## Setting API KEY in Environment   
set "X-RapidAPI-Key=apiKey"
