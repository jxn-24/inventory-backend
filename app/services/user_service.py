# app/services/user_service.py
from app.models import User
from app import db

def get_user_profile(user_id):
    user = User.query.get_or_404(user_id)
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }

def update_user_profile(user_id, data):
    user = User.query.get_or_404(user_id)

    if 'email' in data:
        user.email = data['email']
    if 'username' in data:
        existing = User.query.filter_by(username=data['username']).first()
        if existing and existing.id != user_id:
            raise ValueError("Username already taken.")
        user.username = data['username']

    db.session.commit()
    return get_user_profile(user_id)