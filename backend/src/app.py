from dotenv import load_dotenv

load_dotenv()

from flask import Flask

from src.config import Config
from src.extensions import db,migrate,init_cassandra,jwt,socketio,cors
from src.models.user import User
from src.models.room import ChatRoom
from src.models.membership import RoomMembership
from src.api.auth import auth_bp
from src.api.room import room_bp
from src.sockets import chat_socket
from src.api.message import message_bp



def create_app():
    # create flask application
    app = Flask(__name__)
    # takes setting we made in config and loads them into flask
    app.config.from_object(Config)

    cors.init_app(
        app,
        origins=app.config["CORS_ORIGINS"]
    )

# connect that tool to this flask application
    db.init_app(app)


# flask-migrate work with this flask app and this database
    migrate.init_app(app,db)

    jwt.init_app(app)

    socketio.init_app(
        app,
        cors_allowed_origins=app.config["CORS_ORIGINS"]
    )

# connect to cassandra
    init_cassandra(app)


    app.register_blueprint(auth_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(message_bp)

    return app


if __name__ == "__main__":
    socketio.run(create_app(), debug=True)