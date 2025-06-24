from flask import Flask

def create_app():
    app = Flask(__name__)

    # Example route or register blueprints here
    @app.route('/')
    def home():
        return "Welcome to the Inventory App!"

    return app