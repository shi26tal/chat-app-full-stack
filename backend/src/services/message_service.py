from datetime import datetime, timezone
from uuid import uuid1

from src.repositories.message_repository import MessageRepository


class MessageService:

    @staticmethod
    def send_message(room_id, user_id, content):

        message_id = uuid1()
        created_at = datetime.now(timezone.utc)

        MessageRepository.create(
            room_id=room_id,
            message_id=message_id,
            user_id=user_id,
            content=content,
            created_at=created_at
        )

        return {
            "room_id": room_id,
            "message_id": str(message_id),
            "user_id": user_id,
            "content": content,
            "created_at": created_at.isoformat()
        }

    @staticmethod
    def get_room_messages(room_id):
        return MessageRepository.get_by_room(room_id)