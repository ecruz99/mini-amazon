from flask import Flask
from flask_login import LoginManager
from .config import Config
from .db import DB


login = LoginManager()
login.login_view = 'users.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.db = DB(app)
    login.init_app(app)

    from .index import bp as index_bp
    app.register_blueprint(index_bp)

    from .users import bp as user_bp
    app.register_blueprint(user_bp)

    from .hw4 import bp as hw4_bp
    app.register_blueprint(hw4_bp)

    from .product import bp as product_bp
    app.register_blueprint(product_bp)

    from .hw4_inventory import bp as hw4_inventory_bp
    app.register_blueprint(hw4_inventory_bp)

    from .hw4_socials import bp as hw4_socials_bp
    app.register_blueprint(hw4_socials_bp)

    from .hw4_carts import bp as hw4_carts_bp
    app.register_blueprint(hw4_carts_bp)
    
    from .productreview import bp as productreview_bp
    app.register_blueprint(productreview_bp)
    
    from .sellerreview import bp as sellerreview_bp
    app.register_blueprint(sellerreview_bp)

    return app
