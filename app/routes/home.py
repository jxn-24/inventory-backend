from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return jsonify({
        "message": "Welcome to Inventory API",
        "status": "success",
        "endpoints": {
            "inventory": "/api/inventory",
            "suppliers": "/api/suppliers"
        }
    })