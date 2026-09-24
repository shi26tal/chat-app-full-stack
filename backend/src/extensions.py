from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_migrate import Migrate
from cassandra.cluster import Cluster

# create the db tool
db = SQLAlchemy()
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "http://localhost:5000",
        "http://127.0.0.1:5000"
    ], async_mode="eventlet")
cors = CORS()
migrate = Migrate()


cassandra_cluster = None
# where is cassandra -> localhost:9042
cassandra_session = None
# our active connection -> run CQL queries


# for connection

def init_cassandra(app):
    global cassandra_cluster,cassandra_session

    cassandra_cluster = Cluster(
        app.config["CASSANDRA_HOSTS"]
    )
# store connection cassandra_sesssion ma
    cassandra_session = cassandra_cluster.connect(
        app.config["CASSANDRA_KEYSPACE"]
    )