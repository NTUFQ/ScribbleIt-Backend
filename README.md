# ScribbleIt-Backend

## Getting Started

### Requirements
- Install [Python 3.5](https://www.python.org/downloads/).
- Install `pip` and `virtualenv` with this [guide](http://dont-be-afraid-to-commit.readthedocs.io/en/latest/virtualenv.html) and familiarize yourself with them (how to create virtual environment).

### Development

**NOTE**: don't copy `$` character! It only means that the command should be executed in command-line / terminal!

**Create virtual environment:**

```
$ virtualenv venv
```

**Activate virtual environment:**

*OSX / Linux*

```
$ source venv/bin/activate
```
or if the above does not work

```
$ . venv/bin/activate
```

*Windows*

```
$ Scripts\activate
```

After activating the virtual environment your terminal should show `(venv)`. If i does not show that, **DO NOT** proceed with installation step because it will install all packages globally!

**Add project files**

You can either unzip the download project files to your working directory or 

```
$ git clone https://github.com/NTUFQ/ScribbleIt-Backend.git
```


**Install dependencies**

```
$ cd /PATH_TO_SCRIBBLEIT_BACKEND/
$ pip install -r requirements.txt
```

**Updating dependencies**

If you add a new package remember to add it to `requirements.txt` file:

```
$ pip freeze > requirements.txt
```

**Run server**


```
 $ python manage.py runserver
```

## References

 * [Python 3.5](https://docs.python.org/3/) 
 * [Django 1.10](https://github.com/django/django) Python web framework for backend HTTP request.  [Tutorial](https://docs.djangoproject.com/en/1.10/)
 * [Django-REST-framework](https://github.com/tomchristie/django-rest-framework) for RESTful API. [Tutorial](http://www.django-rest-framework.org/)
