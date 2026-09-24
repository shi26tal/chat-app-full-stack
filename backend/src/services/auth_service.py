import bcrypt

from src.models.user import User
from src.repositories.auth_repository import AuthRepository


class AuthService:

    @staticmethod
    def register(username, email, password):

        if AuthRepository.find_by_username(username):
            raise ValueError("Username already exists")

        if AuthRepository.find_by_email(email):
            raise ValueError("Email already exists")

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        return AuthRepository.create_user(user)

    @staticmethod
    def login(username, password):

        user = AuthRepository.find_by_username(username)

        if not user:
            raise ValueError("Invalid username or password")

        if not bcrypt.checkpw(
            password.encode("utf-8"),
            user.password.encode("utf-8")
        ):
            raise ValueError("Invalid username or password")

        return user