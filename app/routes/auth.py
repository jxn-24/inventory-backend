from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # In a real app, you would create a User model
    return jsonify({"message": "User registration endpoint"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login endpoint"}), 200