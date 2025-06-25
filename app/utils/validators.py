from datetime import datetime
from flask import current_app

# Inventory-specific validators
class InventoryValidators:
    
    @staticmethod
    def validate_sku(sku):
        """Validate SKU format: AA-0000 format"""
        if len(sku) != 7:
            return False
        if not sku[:2].isalpha() or sku[2] != '-' or not sku[3:].isdigit():
            return False
        return True

    @staticmethod
    def validate_expiry_date(date_str):
        """Validate expiry date format (YYYY-MM-DD) and future date"""
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if date < datetime.now().date():
                return "Expiry date must be in the future"
        except ValueError:
            return "Invalid date format (YYYY-MM-DD required)"
        return None

    @staticmethod
    def validate_quantity(quantity):
        """Validate positive quantity with max limit"""
        if not isinstance(quantity, int) or quantity <= 0:
            return "Quantity must be a positive integer"
        if quantity > current_app.config.get('MAX_QUANTITY', 10000):
            return f"Quantity exceeds maximum allowed ({current_app.config['MAX_QUANTITY']})"
        return None

    @staticmethod
    def validate_location(location):
        """Validate warehouse location format (Aisle-Rack-Shelf)"""
        parts = location.split('-')
        if len(parts) != 3:
            return "Invalid location format (ex: A-01-2)"
        if not parts[0].isalpha() or len(parts[0]) != 1:
            return "Invalid aisle format"
        if not parts[1].isdigit() or len(parts[1]) != 2:
            return "Invalid rack format"
        if not parts[2].isdigit() or int(parts[2]) > 10:
            return "Invalid shelf number"
        return None

# Marshmallow schemas for request validation
from marshmallow import Schema, fields, validate, ValidationError

class ItemCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    sku = fields.Str(required=True, validate=lambda s: InventoryValidators.validate_sku(s))
    quantity = fields.Int(required=True)
    category = fields.Str(validate=validate.OneOf(["Electronics", "Clothing", "Food", "Other"]))
    expiry_date = fields.Str()
    location = fields.Str(required=True)

    @validates('expiry_date')
    def validate_expiry(self, value):
        if value and InventoryValidators.validate_expiry_date(value):
            raise ValidationError("Invalid expiry date")

    @validates('location')
    def validate_location(self, value):
        if InventoryValidators.validate_location(value):
            raise ValidationError("Invalid location format")

class ItemUpdateSchema(Schema):
    quantity = fields.Int(validate=validate.Range(min=0))
    location = fields.Str()
    last_restocked = fields.DateTime(format='%Y-%m-%d')