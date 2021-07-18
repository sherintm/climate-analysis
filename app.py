# import Flask
from flask import Flask, jsonify

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Find the latest date and date 12 months before latest date
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
last_date = last_date[0]
start_date = datetime.strptime(last_date, '%Y-%m-%d') - timedelta(days = 365)
start_date = start_date.date()
session.close()


# Define what to do when a user hits the index route
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App!<br/><br/>"
        f"<strong>Available Routes:</strong><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

# Define what to do when a user hits the /precipitaion route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for precipitation data...")

    # create session and fetch data
    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp).\
                      filter(Measurement.date >= start_date).all()
    dictionary = dict(results)
    session.close()

    return (jsonify(dictionary))

# Define what to do when a user hits the /stations route
@app.route("/api/v1.0/stations")
def station():
    print("Server received request for station names...")

    # create session and fetch data
    session = Session(engine)
    results = session.query(Station.id,Station.name).all()
    dictionary = dict(results)
    print(results)
    session.close()

    return (jsonify(dictionary))

# Define what to do when a user hits the /tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for tobs data...")

    # create session and fetch data
    session = Session(engine)

    # Find the most active station
    active_stations = session.query(Measurement.station\
                              ,func.count(Measurement.station))\
                              .group_by(Measurement.station)\
                              .order_by(func.count(Measurement.station).desc()).all()
    active_station = active_stations[0][0]

    # Find last year temperature data of most active station
    results = session.query(Measurement.date,Measurement.tobs)\
                     .filter(Measurement.station == active_station)\
                     .filter(Measurement.date >= start_date).all()
    dictionary = dict(results)
    session.close()

    return (jsonify(dictionary))

# Define what to do when a user hits the /<start> route
@app.route("/api/v1.0/<start>")
def data_start(start):
    print("Server received request for data based on start date")

    # create session and fetch data
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs)\
                            ,func.avg(Measurement.tobs)\
                            ,func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    min_temp = results[0][0]
    avg_temp = results[0][1]
    max_temp = results[0][2]

    return (
        f"Minimum temperature: {min_temp}<br/>"
        f"Average temperature: {round(avg_temp,2)}<br/>"
        f"Maximum temperature: {max_temp}<br/>"
    )

# Define what to do when a user hits the /<start>/<end> route
@app.route("/api/v1.0/<start>/<end>")
def about(start,end):
    print("Server received request for data based on start and end dates")

    # create session and fetch data
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs)\
                            ,func.avg(Measurement.tobs)\
                            ,func.max(Measurement.tobs))\
                            .filter(Measurement.date >= start)\
                            .filter(Measurement.date<=end).all()
    session.close()

    min_temp = results[0][0]
    avg_temp = results[0][1]
    max_temp = results[0][2]

    return (
        f"Minimum temperature: {min_temp}<br/>"
        f"Average temperature: {round(avg_temp,2)}<br/>"
        f"Maximum temperature: {max_temp}<br/>"
    )

if __name__ == "__main__":
    app.run(debug=True)
