from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_httpauth import HTTPTokenAuth
from app.models.user_model import UserModel
from flask import current_app, session

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def verify_token(token):
    find_token = UserModel.query.filter_by(api_key=token).first()
    return find_token   

@auth.login_required
def delete_user_controller(id):
    session = current_app.db.session
    user = auth.current_user()

    session.delete(user)
    session.commit()
    return {"msg": f"user {user.name} has been deleted."},204


