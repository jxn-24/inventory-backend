# app/services/auth_service.py
from app.models import User
from app import db
import bcrypt

def register_user(username, email, password):
    if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
        raise ValueError("User with this email or username already exists.")

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        raise ValueError("Invalid credentials")
    return user