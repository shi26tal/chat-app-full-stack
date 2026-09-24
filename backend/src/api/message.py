from flask import Blueprint, jsonify
from src.services.message_service import MessageService

message_bp = Blueprint(
    "message",
    __name__,
    url_prefix="/rooms"
)


@message_bp.route("/<int:room_id>/messages", methods=["GET"])
def get_messages(room_id):

    messages = MessageService.get_room_messages(room_id)

    return jsonify([
        {
            "room_id": message.room_id,
            "message_id": str(message.message_id),
            "user_id": message.user_id,
            "content": message.content,
            "created_at": message.created_at.isoformat()
        }
        for message in messages
    ]), 200