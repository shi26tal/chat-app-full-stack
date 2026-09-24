from src.models.membership import RoomMembership
from src.extensions import db


class MembershipRepository:

    @staticmethod
    def find_membership(user_id, room_id):
        return RoomMembership.query.filter_by(
            user_id=user_id,
            room_id=room_id
        ).first()

    @staticmethod
    def create(membership):
        db.session.add(membership)
        db.session.commit()

        return membership