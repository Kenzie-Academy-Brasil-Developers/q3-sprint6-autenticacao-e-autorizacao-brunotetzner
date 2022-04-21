from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from app.models.user_model import UserModel
from flask import current_app


def post_signup_user_controller():
    session = current_app.db.session
    data = request.get_json()
    password_to_hash = data.pop("password")

    try:
        new_user = UserModel(**data)
        new_user.password = password_to_hash
        
        session.add(new_user)
        session.commit()

        return jsonify(new_user)
        
    except IntegrityError as err:
        if isinstance(err.orig, UniqueViolation):
            return {"Error": "O email informado já existe no banco de dados"},409
    