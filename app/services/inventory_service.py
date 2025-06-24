from app.models import InventoryItem, Category, Supplier
from app import db
from utils.validators import validate_inventory_item, validate_category

class InventoryService:
    # Inventory Items
    def get_inventory_items(self):
        items = InventoryItem.query.all()
        return {'items': [item.to_dict() for item in items]}
    
    def create_inventory_item(self, data):
        is_valid, message = validate_inventory_item(data)
        if not is_valid:
            return {'message': message}, 400
            
        new_item = InventoryItem(
            name=data['name'],
            description=data.get('description', ''),
            quantity=data['quantity'],
            price=data['price'],
            category_id=data['category_id'],
            supplier_id=data.get('supplier_id')
        )
        db.session.add(new_item)
        db.session.commit()
        return {'message': 'Item created successfully'}, 201
    
    # Categories
    def get_categories(self):
        categories = Category.query.all()
        return {'categories': [cat.to_dict() for cat in categories]}
    
    def create_category(self, data):
        is_valid, message = validate_category(data)
        if not is_valid:
            return {'message': message}, 400
            
        new_category = Category(name=data['name'], description=data.get('description', ''))
        db.session.add(new_category)
        db.session.commit()
        return {'message': 'Category created successfully'}, 201
    
    # Suppliers
    def get_suppliers(self):
        suppliers = Supplier.query.all()
        return {'suppliers': [sup.to_dict() for sup in suppliers]}