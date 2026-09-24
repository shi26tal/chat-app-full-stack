from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from flask_jwt_extended import jwt_required,get_jwt_identity

from src.schemas.room import CreateRoomRequest
from src.services.room_service import RoomService
from src.services.membership_service import MembershipService

room_bp = Blueprint("room",__name__,url_prefix="/rooms")

@room_bp.route("", methods=["GET"])
def get_rooms():
    rooms = RoomService.get_all_rooms()

    return jsonify([
        {
            "id": room.id,
            "name": room.name,
            "created_at": room.created_at.isoformat()
        }
        for room in rooms
    ]), 200


@room_bp.route("/create", methods=["POST"])
def create_room():
    try:
        data = CreateRoomRequest(**request.get_json())

        room = RoomService.create_room(data.name)

        return jsonify({
            "message": "Room created successfully",
            "room": {
                "id": room.id,
                "name": room.name,
                "created_at": room.created_at.isoformat()
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


@room_bp.route("/<int:room_id>/join", methods=["POST"])
@jwt_required()
def join_room(room_id):
    try:
        user_id = int(get_jwt_identity())

        MembershipService.join_room(
            user_id=user_id,
            room_id=room_id
        )

        return jsonify({
            "message": "Joined room successfully"
        }), 200

    except ValueError as error:
        return jsonify({
            "message": str(error)
        }), 400