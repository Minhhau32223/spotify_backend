from music.DAO.UserDAO import UserDAO

class UserService:
    @staticmethod
    def get_all_users():
        return UserDAO.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserDAO.get_user_by_id(user_id)
    @staticmethod
    def create_user(username, email, password,is_admin=False):
        return UserDAO.create_user(username, email, password,is_admin)
    @staticmethod
    def get_user_by_email(email):
        return UserDAO.get_user_by_email(email)