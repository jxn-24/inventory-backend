from flask import Blueprint, request, jsonify
from app.models import Supplier, db

suppliers_bp = Blueprint('suppliers', __name__)

@suppliers_bp.route('/', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'contact': s.contact,
        'phone': s.phone,
        'email': s.email
    } for s in suppliers])

@suppliers_bp.route('/', methods=['POST'])
def create_supplier():
    data = request.get_json()
    supplier = Supplier(
        name=data['name'],
        contact=data.get('contact'),
        phone=data.get('phone'),
        email=data.get('email')
    )
    db.session.add(supplier)
    db.session.commit()
    return jsonify({
        'id': supplier.id,
        'name': supplier.name,
        'contact': supplier.contact,
        'phone': supplier.phone,
        'email': supplier.email
    }), 201

@suppliers_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def supplier_detail(id):
    supplier = Supplier.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({
            'id': supplier.id,
            'name': supplier.name,
            'contact': supplier.contact,
            'phone': supplier.phone,
            'email': supplier.email
        })
    
    elif request.method == 'PUT':
        data = request.get_json()
        supplier.name = data.get('name', supplier.name)
        supplier.contact = data.get('contact', supplier.contact)
        supplier.phone = data.get('phone', supplier.phone)
        supplier.email = data.get('email', supplier.email)
        db.session.commit()
        return jsonify({
            'id': supplier.id,
            'name': supplier.name,
            'contact': supplier.contact,
            'phone': supplier.phone,
            'email': supplier.email
        })
    
    elif request.method == 'DELETE':
        db.session.delete(supplier)
        db.session.commit()
        return '', 204