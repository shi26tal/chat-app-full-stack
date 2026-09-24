# talk with db for auth related data

from src.models.user import User

class AuthRepository:

# user khojyo
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

# email khojyo
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()

# chaina bhaney create user
    @staticmethod
    def create_user(user):
        from src.extensions import db

        db.session.add(user)
        db.session.commit()

        return user