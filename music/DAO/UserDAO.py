from music.models import User
from music.DTO.UserDTO import UserDTO

class UserDAO:
    @staticmethod
    def get_all_users():
        users = User.objects.all()
        return [UserDTO(u.id, u.username, u.email, u.is_admin ) for u in users]

    @staticmethod
    def get_user_by_id(user_id):
        u = User.objects.filter(id=user_id).first()
        if u:
            return UserDTO(u.id, u.username, u.email, u.is_admin)
        return None
    @staticmethod
    def create_user(username, email,password, is_admin=False):
        user = User(username=username, email=email, is_admin=is_admin)
        user.save()
        return UserDTO(user.id, user.username, user.email, user.is_admin,password)