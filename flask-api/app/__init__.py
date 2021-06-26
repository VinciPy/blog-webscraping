from flask import Flask
from flask_migrate import Migrate
from .models.table import configure as config_db
from .serializer import configure as config_ma

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/blog'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .controller.posts import bp_posts
    app.register_blueprint(bp_posts)

    return app
