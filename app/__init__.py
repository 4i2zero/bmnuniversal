from flask import Flask, redirect, url_for
from app.extensions import db, migrate, login_manager, bcrypt
from app.config import Config
from app.models import User, Artist, Album, Song, Store, Post, Report, Ticket, Message, Ugc, Profilelinking, Distributelyrics
from werkzeug.utils import secure_filename
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_required

class MyAdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # Redirect to login page if user doesn't have access
        return redirect(url_for('login'))

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

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(cms_blueprint, url_prefix='/cms')

    admin = Admin(app, name='MyAdmin', template_mode='bootstrap4') # Use 'bootstrap4' if you prefer
    admin.add_view(MyAdminModelView(User, db.session)) # Add your model to the admin interface
    admin.add_view(MyAdminModelView(Artist, db.session))
    admin.add_view(MyAdminModelView(Album, db.session))
    admin.add_view(MyAdminModelView(Song, db.session))
    admin.add_view(MyAdminModelView(Store, db.session))
    admin.add_view(MyAdminModelView(Post, db.session))
    admin.add_view(MyAdminModelView(Report, db.session))
    admin.add_view(MyAdminModelView(Ticket, db.session))
    admin.add_view(MyAdminModelView(Message, db.session))
    admin.add_view(MyAdminModelView(Ugc, db.session))
    admin.add_view(MyAdminModelView(Profilelinking, db.session))
    admin.add_view(MyAdminModelView(Distributelyrics, db.session))


    return app
