class InvalidPassword(Exception):
    def __init__(self):
        self.message = {"error": "invalid password"}