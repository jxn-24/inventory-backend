def validate_inventory_item(data):
    required_fields = ['name', 'quantity', 'price', 'category_id']
    for field in required_fields:
        if field not in data:
            return False, f"{field} is required"
    return True, ""

def validate_category(data):
    if 'name' not in data:
        return False, "Name is required"
    return True, ""