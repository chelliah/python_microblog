from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	# return "Hello World
	user = {'nickname': 'Miguel'}
	posts = [ #fake array of posts
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in Boston'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'Star Wars is a good movie'
		}
	]
	# return render_template('index.html', title="Home", user = user)
	return render_template('index.html',
							title='Home', 
							user = user,
							posts = posts)

# import loginform class, instantiate an object and send it to the template
# methods argument specifies gets and posts
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm();
	if form.validate_on_submit(): 
		flash('Login requrested for openid="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
							title = 'Sign In',
							form = form,
							providers=app.config['OPENID_PROVIDERS'])