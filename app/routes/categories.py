from flask import Blueprint, request, jsonify
from app.models import Category, db
from app.extensions import db

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in categories])

@categories_bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({'id': category.id, 'name': category.name}), 201

@categories_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def category_detail(id):
    category = Category.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({'id': category.id, 'name': category.name})
    
    elif request.method == 'PUT':
        data = request.get_json()
        category.name = data['name']
        db.session.commit()
        return jsonify({'id': category.id, 'name': category.name})
    
    elif request.method == 'DELETE':
        db.session.delete(category)
        db.session.commit()
        return '', 204