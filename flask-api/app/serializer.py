from flask_marshmallow import Marshmallow
from .models.table import Post

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
        include_fk = True
        include_relationships = True
