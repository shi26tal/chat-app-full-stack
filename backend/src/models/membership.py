from src.extensions import db

class RoomMembership(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("chat_room.id"),
        nullable=False
    )

    joined_at = db.Column(
        db.DateTime,
        default=db.func.now(),
        nullable=False
    )

    # to prevent same user from joining same room multiple times

    __table_args__ = (
        db.UniqueConstraint("user_id", "room_id", name="unique_user_room"),
    )