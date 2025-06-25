import time
import functools
from flask import request, jsonify

# Decorator for measuring function execution time
def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} executed in {(end - start):.4f}s")
        return result
    return wrapper

# Decorator for role-based access control
def role_required(*required_roles):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # In a real app, get roles from JWT or session
            user_role = request.headers.get('X-User-Role', 'guest')
            
            if user_role not in required_roles:
                return jsonify({
                    "error": "Unauthorized",
                    "message": f"Requires roles: {', '.join(required_roles)}"
                }), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Decorator for validating JSON request structure
def validate_schema(schema):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            errors = schema().validate(data)
            if errors:
                return jsonify({
                    "error": "Validation failed",
                    "details": errors
                }), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator