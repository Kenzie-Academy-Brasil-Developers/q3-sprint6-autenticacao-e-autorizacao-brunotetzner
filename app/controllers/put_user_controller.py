from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_httpauth import HTTPTokenAuth
from flask import jsonify, request, current_app
from app.models.user_model import UserModel
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation


auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def verify_token(token):
    find_token = UserModel.query.filter_by(api_key=token).first()
    return find_token   

@auth.login_required
def put_user_controller():

    data = request.get_json()
    session = current_app.db.session
    user = auth.current_user()
          
    try:
        for key, value in data.items():
            setattr(user, key, value)
        session.add(user)
        session.commit()
        return jsonify(user)
    
    except IntegrityError as err:
        if isinstance(err.orig, UniqueViolation):
            return {"Error": "O email informado já existe no banco de dados"},409