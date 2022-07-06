from flask import Flask
from config import Config

def create_app():
    app = Flask("portfolio_website")
    app.config.from_object(Config)

    with app.app_context():
        from portfolio_website import routes

    return app