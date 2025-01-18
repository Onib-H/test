from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'

    # Register blueprint
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
