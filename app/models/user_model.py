from werkzeug.security import generate_password_hash, check_password_hash
from app.configs.database import db
from app.exc import InvalidPassword
from dataclasses import dataclass


@dataclass
class UserModel(db.Model):

    name: str
    last_name: str
    email: str

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=True)
    last_name = db.Column(db.String(511), nullable=True)
    email = db.Column(db.String(80), nullable=True, unique=True)
    password_hash = db.Column(db.String(511), nullable=True)
    api_key = db.Column(db.String(511), nullable=True)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        check =check_password_hash(self.password_hash, password_to_compare)
        if not check:
            raise InvalidPassword
        return check
            