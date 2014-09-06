from flask import render_template, request, flash, session, redirect, url_for
from . import main
from .models import db, User
from .forms import SignupForm, SigninForm


@main.route('/')
def home():
  return render_template('home.html')
 
@main.route('/about')
def about():
  return render_template('about.html')

@main.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'


@main.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  
  if 'email' in session:
    return redirect(url_for('profile'))
  
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
 
      session['email'] = newuser.email
      return redirect(url_for('profile'))
    
  elif request.method == 'GET':
    return render_template('signup.html', form=form)
  
  
@main.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
  
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
      
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@main.route('/signout')
def signout():
  
  if 'email' not in session:
    return redirect(url_for('signin'))
  
  session.pop('email', None)
  return redirect(url_for('home'))


@main.route('/profile')
def profile():
  
  if 'email' not in session:
    return redirect(url_for('signin'))
  
  user = User.query.filter_by(email = session['email']).first()
  
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')