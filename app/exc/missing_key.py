class MissingKey(Exception):
    def __init__(self):
        self.message = {"Error": "Your request needs to have the keys email, name, last_name and password"}