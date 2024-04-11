from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Reservation, Order
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('logged in successfully', category= 'success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again', category = 'error')
                
    
    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('email already exists', category = 'error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstname) < 2:
            flash('firstname must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('password mismatch', category='error')
        elif len(password1) < 7:
            flash('password must be atleast 7 characters.', category='error')
        else:
            #add user to database
            new_user = User(email = email, firstname = firstname, password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('account created successfully!', category='success')
            login_user(user=current_user, remember = True)
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html", user = current_user)

@auth.route('/about_us', methods=['GET', 'POST'])
def about_us():
    return render_template('about_us.html', user=current_user)


@auth.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template('contact_us.html', user=current_user)

@auth.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user=current_user)

@auth.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        rdate= request.form.get('reservation_date')
        rtime= request.form.get('reservation_time')
        people = request.form.get('people')
        
        new_reservation = Reservation(email = email, name = name, rdate= rdate,rtime=rtime, people=people, user_id = current_user.id) #date = date, time = time
        db.session.add(new_reservation)
        db.session.commit()
        flash('Reservation was  successful!', category='success')
    return render_template('reservation.html',user=current_user)

@auth.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        item = request.form.get('item')
        quantity = request.form.get('quantity')
        destination = request.form.get('destination')
        
        if len(email) < 4:
            flash('email is too short', category='error')
        elif len(name) < 3:
            flash('name is too short', category='error')
        elif quantity == 0:
            flash('quantity should be atleast one', category='error')
        elif len(destination) < 4:
            flash('invalid destination address', category='error')
        elif len(item) < 4:
            flash('invalid item', category='error')
        else:
            new_order = Order(email=email, name= name, item=item,destination=destination, quantity=quantity, user_id = current_user.id)
            db.session.add(new_order)
            db.session.commit()
            flash('order was  successful!', category='success')
    
    return render_template('order.html',user=current_user )

@auth.route('/delete', methods=['DELETE'])
def delete(id):
    Order.query.filter(order.id == id).delete()
    
    db.session.commit()
    
    order = Order.query.all()
    return render_template('order.html',order=order)
    
    