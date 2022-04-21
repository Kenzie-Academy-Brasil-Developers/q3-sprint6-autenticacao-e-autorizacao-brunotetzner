class UserNotFound(Exception):
    def __init__(self):
        self.message = {"error": "user not found"}