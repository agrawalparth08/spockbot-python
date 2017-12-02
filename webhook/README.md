1)Install Heroku CLI and make accounts <br />
2)Make you app directory and open cmd and write heroku login <br />
3)Then setup "virtualenv env" (if not present then first pip install virtualenv <br />
4)Type env\Scripts\activate <br />
5)Inside env , write pip install flask <br />
6)Then pip install gunicorn (For multiple user access) <br />
7)git init <br />
8) Go to the directory and create a .gitignore file and just type env in it <br />
9)Make a Procfile with content web: gunicorn {app-name}:app and also make the app. <br />
9a) Also pip freeze > requirements.txt <br />
10)git add . <br />
11)git commit -m "commited" <br />
12)heroku create <br />
13)heroku open to check basic app <br />
14)git push heroku master
