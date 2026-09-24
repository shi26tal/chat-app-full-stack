import socketio

sio = socketio.Client()

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc5MDIxNzEzNiwianRpIjoiNzdhY2VlNGYtOGE5Yi00MWUxLTgyYWEtNzVhMTM3NWYyZDMyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3OTAyMTcxMzYsImNzcmYiOiI2M2RlODZlMC0zMDdjLTQxNzAtOWYzZC05OTA5YTFlNzRmNjIiLCJleHAiOjE3OTAzMDM1MzZ9.yAqfbUNQnr5ZCoUIPqvH96wydcExTWrbEbEnY1g_DZw"


@sio.event
def connect():
    print("Connected to server")

    sio.emit("join_room", {
        "room_id": 1
    })


@sio.on("connected")
def on_connected(data):
    print("Server:", data)


@sio.on("room_joined")
def on_room_joined(data):
    print("Room:", data)

    sio.emit("send_message", {
        "room_id": 1,
        "content": "Hello from WebSocket"
    })

@sio.on("receive_message")
def on_receive_message(data):
    print("Message received:", data)

    sio.emit("leave_room", {
        "room_id": 1
    })

@sio.on("room_left")
def on_room_left(data):
    print("Room left:", data)


@sio.on("error")
def on_error(data):
    print("Error:", data)


@sio.event
def disconnect():
    print("Disconnected")


sio.connect(
    "http://127.0.0.1:5000",
    auth={
        "token": TOKEN
    }
)

sio.wait()