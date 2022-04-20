from flask import jsonify, request
from app.models.user_model import UserModel
from app.exc import InvalidPassword

def post_signin_user_controller():
    data = request.get_json()
    try:
        found_user = UserModel.query.filter_by(email=data["email"]).first()
        found_user.verify_password(data["password"])
        return {"api_key": found_user.api_key}
   
    except InvalidPassword as err:
        return err.message, 401

    except KeyError:
        return {"error":"They keys 'email' and 'password' are required"}, 400