# Activities

In this Project, I have created an app, activityapp which has this functionality:
1. Dummy data using custom management command
2. Created an api to show the activity detail corresponding to user details.


## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv-2.7 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

## Deploy to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/memcachier/examples-django.git
$ cd examples-django
$ heroku create
$ git push heroku master:master
$ heroku open
```
