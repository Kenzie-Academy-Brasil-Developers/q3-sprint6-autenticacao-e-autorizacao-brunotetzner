from flask import Blueprint
from app.controllers import *

bp= Blueprint("bp_user", __name__, url_prefix="/api")

bp.get("")(get_user_controller)
bp.post("/signin")(post_signin_user_controller)
bp.post("/signup")(post_signup_user_controller)
bp.put("")(put_user_controller)
bp.delete("")(delete_user_controller)

