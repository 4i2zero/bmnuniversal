from flask import Flask
from app.extensions import db, migrate, login_manager, bcrypt
from app.config import Config
from app.models import User
from werkzeug.utils import secure_filename


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    from .views.main import main as main_blueprint
    from .views.auth import auth as auth_blueprint
    from .views.cms import cms as cms_blueprint
    from app.views.admin import admin as admin_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(cms_blueprint, url_prefix='/cms')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
