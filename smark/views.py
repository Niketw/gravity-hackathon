from flask import Blueprint, render_template

# Sample data for parking spots
parking_spots = [
    {'id': 1, 'location': 'Lot A', 'status': 'Available'},
    {'id': 2, 'location': 'Lot A', 'status': 'Occupied'},
    {'id': 3, 'location': 'Lot B', 'status': 'Available'},
    {'id': 4, 'location': 'Lot B', 'status': 'Occupied'},
    {'id': 5, 'location': 'Lot C', 'status': 'Available'},
    {'id': 6, 'location': 'Lot C', 'status': 'Occupied'},
    {'id': 7, 'location': 'Lot D', 'status': 'Available'},
    {'id': 8, 'location': 'Lot D', 'status': 'Occupied'},
    {'id': 9, 'location': 'Lot E', 'status': 'Available'},
    {'id': 10, 'location': 'Lot E', 'status': 'Occupied'},
    {'id': 11, 'location': 'Lot F', 'status': 'Available'},
]

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html', parking_spots=parking_spots)
