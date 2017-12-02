1)Install Heroku CLI and make accounts
2)Make you app directory and open cmd and write heroku login
3)Then setup "virtualenv env" (if not present then first pip install virtualenv
4)Type env\Scripts\activate
5)Inside env , write pip install flask
6)Then pip install gunicorn (For multiple user access)
7)git init 
8) Go to the directory and create a .gitignore file and just type env in it
9)Make a Procfile with content web: gunicorn {app-name}:app and also make the app.
9a) Also pip freeze > requirements.txt
10)git add .
11)git commit -m "commited"
12)heroku create
13)heroku open to check basic app
14)git push heroku master
