from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request, current_app
from app.models.user_model import UserModel
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from app.exc import UserNotFound



@jwt_required()
def put_user_controller():

    data = request.get_json()
    session = current_app.db.session
    current_user = get_jwt_identity()
    user = UserModel.query.filter_by(email=current_user["email"]).first()

    try:
        if not user:
            raise UserNotFound
        for key, value in data.items():
            setattr(user, key, value)
        session.add(user)
        session.commit()
        return jsonify(user)
    
    except IntegrityError as err:
        if isinstance(err.orig, UniqueViolation):
            return {"Error": "O email informado já existe no banco de dados"},409
    
    except UserNotFound as err:
        return err.message, 400
