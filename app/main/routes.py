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

@main.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()

  if 'email' in session:
    return redirect(url_for('main.profile'))
  
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
 
      session['email'] = newuser.email
      return redirect(url_for('main.profile'))
    
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
      return redirect(url_for('main.profile'))
      
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@main.route('/signout')
def signout():
  
  if 'email' not in session:
    return redirect(url_for('main.signin'))
  
  session.pop('email', None)
  return redirect(url_for('main.home'))

@main.route('/profile')
def profile():
  
  if 'email' not in session:
    return redirect(url_for('main.signin'))
  
  user = User.query.filter_by(email = session['email']).first()
  
  if user is None:
    return redirect(url_for('main.signin'))
  else:
    return render_template('profile.html')