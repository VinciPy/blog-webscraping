from flask import Blueprint, current_app, request, jsonify
from flask.wrappers import Request
from ..models.table import Post
from ..serializer import PostSchema

bp_posts = Blueprint('posts', __name__)


@bp_posts.route('/posts', methods=['GET'])
def mostar():
    ps = PostSchema(many=True)
    result = Post.query.all()
    return ps.jsonify(result, 200)


@bp_posts.route('/posts/add', methods=['POST'])
def cadastro():
    
    ps = PostSchema()
    post = ps.load(request.json, session=current_app.db.session)
    current_app.db.session.add(post)
    current_app.db.session.commit()
    return ps.jsonify(post), 201


@bp_posts.route('/posts/delete/<id>', methods=['GET'])
def deletar(id):
   
    Post.query.filter(Post.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado')


@bp_posts.route('/posts/modify/<id>', methods=['POST'])
def modificar(id):

    query = Post.query.filter(Post.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return jsonify('Modificado')
