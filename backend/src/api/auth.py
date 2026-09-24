from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from src.schemas.auth import RegisterRequest,LoginRequest
from src.services.auth_service import AuthService
from flask_jwt_extended import create_access_token


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = RegisterRequest(**request.get_json())

        user = AuthService.register(
            username=data.username,
            email=data.email,
            password=data.password
        )

        return jsonify({
            "message": "User registered successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 201

    except ValidationError as error:
        return jsonify({
            "message": "Invalid input",
            "errors": error.errors()
        }), 400

    except ValueError as error:
        return jsonify({
            "message": str(error)
        }), 409


@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = LoginRequest(**request.get_json())

        user = AuthService.login(
            username=data.username,
            password=data.password
        )

        token = create_access_token(identity=str(user.id))

        return jsonify({
            "message": "Login successful",
            "access_token": token
        }), 200

    except ValidationError as error:
        return jsonify({
            "message": "Invalid input",
            "errors": error.errors()
        }), 400

    except ValueError as error:
        return jsonify({
            "message": str(error)
        }), 401