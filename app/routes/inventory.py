from flask import Blueprint, request, jsonify
from app.models import Inventory, Category, Supplier, db
from datetime import datetime

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    items = Inventory.query.all()
    return jsonify([{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'quantity': i.quantity,
        'price': i.price,
        'category_id': i.category_id,
        'supplier_id': i.supplier_id,
        'created_at': i.created_at.isoformat() if i.created_at else None,
        'updated_at': i.updated_at.isoformat() if i.updated_at else None
    } for i in items])

@inventory_bp.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    item = Inventory(
        name=data['name'],
        description=data.get('description'),
        quantity=data.get('quantity', 0),
        price=data.get('price'),
        category_id=data.get('category_id'),
        supplier_id=data.get('supplier_id')
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({
        'id': item.id,
        'name': item.name,
        'quantity': item.quantity,
        'price': item.price
    }), 201

@inventory_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def item_detail(id):
    item = Inventory.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'quantity': item.quantity,
            'price': item.price,
            'category_id': item.category_id,
            'supplier_id': item.supplier_id,
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'updated_at': item.updated_at.isoformat() if item.updated_at else None
        })
    
    elif request.method == 'PUT':
        data = request.get_json()
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.quantity = data.get('quantity', item.quantity)
        item.price = data.get('price', item.price)
        item.category_id = data.get('category_id', item.category_id)
        item.supplier_id = data.get('supplier_id', item.supplier_id)
        db.session.commit()
        return jsonify({
            'id': item.id,
            'name': item.name,
            'quantity': item.quantity,
            'price': item.price
        })
    
    elif request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return '', 204