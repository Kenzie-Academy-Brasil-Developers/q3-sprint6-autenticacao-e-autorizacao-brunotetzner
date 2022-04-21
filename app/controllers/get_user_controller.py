
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify

@jwt_required()
def get_user_controller():
    current_user = get_jwt_identity()
    return jsonify(current_user)
    