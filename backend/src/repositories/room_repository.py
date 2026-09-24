from src.models.room import ChatRoom
from src.extensions import db


class RoomRepository:

    @staticmethod
    def get_all():
        return ChatRoom.query.order_by(ChatRoom.created_at.desc()).all()

    @staticmethod
    def find_by_id(room_id):
        return ChatRoom.query.get(room_id)

    @staticmethod
    def find_by_name(name):
        return ChatRoom.query.filter_by(name=name).first()

    @staticmethod
    def create(room):
        db.session.add(room)
        db.session.commit()

        return room