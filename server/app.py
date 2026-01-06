# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    """Get a single earthquake by its ID"""
    earthquake = Earthquake.query.get(id)

    if earthquake:
        return jsonify(earthquake.to_dict()), 200
    else:
        return jsonify({'message': f'Earthquake {id} not found.'}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    """Get all earthquakes with magnitude >= the given value"""
    
    # Query for earthquakes with magnitude greater than or equal to parameter
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    # Count the results
    count = len(earthquakes)
    
    # Convert each earthquake to a dictionary
    earthquakes_list = [earthquake.to_dict() for earthquake in earthquakes]
    
    # Return count and data as JSON
    return jsonify({
        'count': count,
        'quakes': earthquakes_list
    }), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
