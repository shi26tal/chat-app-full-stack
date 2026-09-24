import os
from datetime import timedelta 
# timedelta just a way to express 24 hours 

# class holding bunch of settings together
class Config:

    # os lets python read environment variables
    SECRET_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","postgresql://chatapp:password@localhost:5432/chatapp")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

    CASSANDRA_HOSTS = os.environ.get("CASSANDRA_HOSTS", "localhost").split(",")
    CASSANDRA_KEYSPACE = os.environ.get("CASSANDRA_KEYSPACE", "chatapp")

    REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")


    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "http://localhost:4200").split(",")


class TestConfig(Config):
    # used by pytest

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL",
        "postgresql://chatapp:password@localhost:5432/chatapp_test",
    )
    CASSANDRA_KEYSPACE = os.environ.get("TEST_CASSANDRA_KEYSPACE", "chatapp_test")
    

