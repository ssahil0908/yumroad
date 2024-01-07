from flask import Flask, render_template , redirect , url_for

from yumroad.blueprints.products import products
from yumroad.blueprints.users import user_bp
from yumroad.blueprints.stores import store_bp
from yumroad.blueprints.landing import landing_bp

from yumroad.config import configurations
from yumroad.extensions import db , csrf , login_manager , migrate , mail , assets_env
from webassets.loaders import PythonLoader as PythonAssetsLoader

from yumroad import assets

def create_app(environment_name='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])
    #app.config['SECRET_KEY'] = 'any_secret_string'         #Without a secret key you can't use many features such as flash, flask-login and of course, as you have experienced, CSRF protection.
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    mail.init_app(app)
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    app.register_blueprint(products, url_prefix="/product")
    app.register_blueprint(user_bp)
    app.register_blueprint(store_bp, url_prefix='/store')
    app.register_blueprint(landing_bp)
    

    @app.route('/')
    def home():
        return redirect(url_for('store.index'))

    return app


