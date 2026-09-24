from flask_socketio import emit,join_room,leave_room
from flask_jwt_extended import decode_token
from flask import request

from src.extensions import socketio
from src.repositories.membership_repository import MembershipRepository
from src.services.message_service import MessageService

connected_users = {}

@socketio.on("connect")
def handle_connect(auth):

    if not auth or "token" not in auth:
        return False

    try:
        token = auth["token"]
        decoded = decode_token(token)

        user_id = int(decoded["sub"])
        connected_users[request.sid] = user_id

        print(f"User {user_id} connected")

        emit("connected", {
            "message": "Connected to chat server"
        })

    except Exception:
        return False


@socketio.on("join_room")
def handle_join_room(data):

    room_id = data.get("room_id")

    if not room_id:
        emit("error", {
            "message": "Room ID is required"
        })
        return

    user_id = connected_users.get(request.sid)

    if not user_id:
        emit("error", {
        "message": "User not authenticated"
         })
        return

    membership = MembershipRepository.find_membership(
        user_id,
        room_id
    )

    if not membership:
        emit("error", {
        "message": "You are not a member of this room"
        })
        return

    join_room(str(room_id))

    emit("room_joined", {
        "room_id": room_id,
        "message": "Joined room successfully"
    })  



@socketio.on("leave_room")
def handle_leave_room(data):

    room_id = data.get("room_id")

    if not room_id:
        emit("error", {
            "message": "Room ID is required"
        })
        return

    user_id = connected_users.get(request.sid)

    if not user_id:
        emit("error", {
            "message": "User not authenticated"
        })
        return

    leave_room(str(room_id))

    emit("room_left", {
        "room_id": room_id,
        "message": "Left room successfully"
    })


@socketio.on("send_message")
def handle_send_message(data):

    room_id = data.get("room_id")
    content = data.get("content")

    if not room_id or not content:
        emit("error", {
            "message": "Room ID and content are required"
        })
        return

    user_id = connected_users.get(request.sid)

    if not user_id:
        emit("error", {
            "message": "User not authenticated"
        })
        return

    membership = MembershipRepository.find_membership(
        user_id,
        room_id
    )

    if not membership:
        emit("error", {
            "message": "You are not a member of this room"
        })
        return

    message = MessageService.send_message(
        room_id=room_id,
        user_id=user_id,
        content=content
    )

    emit(
        "receive_message",
        message,
        to=str(room_id)
    )


@socketio.on("disconnect")
def handle_disconnect():

    user_id = connected_users.pop(request.sid, None)

    if user_id:
        print(f"User {user_id} disconnected")