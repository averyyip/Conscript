from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

"""
Tips for making templates and linking with handlers

{{ex}} is for dynamic content
use "ex" as an argument in the flask handler 


 
Example of control statements (utilizes Jinja2 templates)
{% if title %}
	<title>{{ title }} - microblog</title>
{% else %}
    <title>Welcome to microblog</title>
{% endif %} 



Example of for loops

Handler return statement
posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

<body>
    <h1>Hi, {{ user.nickname }}!</h1>
    {% for post in posts %}
    <div><p>{{ post.author.nickname }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
 </body>
"""

#Mappings from Routes / and /index to Python Flask handler below
@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html", messages=["hi","bye"])

#Without methods argument, defaulted to take only "GET" requests
@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	#If called when loading page, it'll render page
	"""Called as part of submission, it gathers all data(ex. open id, 
	runs all validators in forms.py (datarequired), """
	if form.validate_on_submit():
		#displays success on submission
		flash('Login requested for OAuth="%s", remember_me=%s' %
              (form.oauth.data, str(form.remember_me.data)))
		return redirect("/index")
	return render_template("login.html",
	                       title="Sign In",
	                       form=form)


