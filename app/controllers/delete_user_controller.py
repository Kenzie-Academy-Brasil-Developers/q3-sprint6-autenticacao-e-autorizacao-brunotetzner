from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user_model import UserModel
from flask import current_app, session
from app.exc import UserNotFound

@jwt_required()
def delete_user_controller():

    session = current_app.db.session
    current_user = get_jwt_identity()

    try:
        user = UserModel.query.filter_by(email=current_user["email"]).first()
        if not user:
            raise UserNotFound
        session.delete(user)
        session.commit()
        return {"msg": f"user {user.name} has been deleted."},204
    
    except UserNotFound as err:
        return err.message, 404

