from src.models.membership import RoomMembership
from src.repositories.membership_repository import MembershipRepository
from src.repositories.room_repository import RoomRepository


class MembershipService:

    @staticmethod
    def join_room(user_id, room_id):

        room = RoomRepository.find_by_id(room_id)

        if not room:
            raise ValueError("Room not found")

        existing_membership = MembershipRepository.find_membership(
            user_id,
            room_id
        )

        if existing_membership:
            raise ValueError("User already joined this room")

        membership = RoomMembership(
            user_id=user_id,
            room_id=room_id
        )

        return MembershipRepository.create(membership)