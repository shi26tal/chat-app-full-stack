from src.models.room import ChatRoom
from src.repositories.room_repository import RoomRepository

class RoomService:

    @staticmethod
    def get_all_rooms():
        return RoomRepository.get_all()

    @staticmethod
    def create_room(name):
        if RoomRepository.find_by_name(name):
            raise ValueError("Room already exists")

        room = ChatRoom(name=name)

        return RoomRepository.create(room)