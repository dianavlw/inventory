This is my rough draft of what an inventory management tracker could be. 

The reason I did not use this app was because I was returning JsonResponse
and not a HTML file. 

Installing
 
1. Create Virtual Environment
  - python -m venv venv

2. Activiate Env
 - source env/bin/activate
 
3.pip install Django

4. Pip install psycopg2 (because I used postgresql)
  - Go to DATABASE in settings.py
  - change to if its not already done for you:
    
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': "tracker_api",
      }
  }

5. create database
  -createdb inventory_api

6. pip3 install -r requirements.txt 



Execute App
1. Your env should be activated
2. python3 server.py



Diana Vargas 
