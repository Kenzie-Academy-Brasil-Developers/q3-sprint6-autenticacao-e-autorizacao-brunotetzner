
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_httpauth import HTTPTokenAuth
from flask import jsonify
from app.models.user_model import UserModel

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def verify_token(token):
    find_token = UserModel.query.filter_by(api_key=token).first()
    return find_token    
    
@auth.login_required
def get_user_controller():
    return jsonify(auth.current_user())
    