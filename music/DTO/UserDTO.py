class UserDTO:
    def __init__(self, id, username, email, is_admin, password):
        self.id = id
        self.username = username
        self.email = email
        self.is_admin = is_admin
        self.password = password
    def __init__(self, id, username, email, is_admin):
        self.id = id
        self.username = username
        self.email = email
        self.is_admin = is_admin