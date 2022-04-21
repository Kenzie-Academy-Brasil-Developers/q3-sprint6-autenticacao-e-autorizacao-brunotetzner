from flask import jsonify, request
from app.models.user_model import UserModel
from app.exc import InvalidPassword, UserNotFound
from flask_jwt_extended import create_access_token

def post_signin_user_controller():
    data = request.get_json()

    try:
        found_user = UserModel.query.filter_by(email=data["email"]).first()

        if not found_user:
            raise UserNotFound
        if not found_user.verify_password(data["password"]):
            raise InvalidPassword
        
        accessToken = create_access_token(identity=found_user)
        return {"message": accessToken}

    except KeyError:
        return {"error":"They keys 'email' and 'password' are required"}, 400

    except InvalidPassword as err:
        return err.message, 400

    except UserNotFound as err:
        return err.message, 400



