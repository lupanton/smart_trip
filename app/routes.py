# -*- coding: utf-8 -*- 
from flask import *
from app import app
from app.models import Trip
from app.forms import TripAdmin
from . import db
from . import date

@app.route('/')
@app.route('/index')
def index():
    trips=db.session.query(Trip).all()
    return render_template('index.html', trips=trips)

@app.route('/get_info/<id>', methods=['POST', 'GET'])
def get_info(id):
    trip_descr=db.session.query(Trip.description).filter(Trip.id == id).first()[0]
    return render_template('get_info.html', trip_descr=trip_descr)

@app.route('/trip_admin')
def trip_admin():
    trips = db.session.query(Trip).all()
    return render_template('trip_admin.html', trips=trips)

@app.route('/add_trip', methods=['POST'])
def add_trip():
    form=TripAdmin()
    if form.validate_on_submit():
        trip=Trip(name=form.name.data, description=form.description.data, date_begin=form.date_begin.data, date_end=form.date_end.data, is_all_inc=form.is_all_inc.data)
        db.session.add(trip)
        db.session.commit()
        return redirect('/trip_admin')
    
    return render_template('add_trip.html', form=form)

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        trip = db.session.query(Trip).get(id)
        db.session.delete(trip)
        db.session.commit()
    return redirect('/trip_admin')