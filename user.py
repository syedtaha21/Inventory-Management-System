class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # Role can be 'Admin' or 'User'

    def authenticate(self, password):
        return self.password == password

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password, role):
        self.users[username] = User(username, password, role)

    def get_user(self, username):
        return self.users.get(username)