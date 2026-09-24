# descibe what user looks like in database

# flask sqlalchemy let us decribe and create table using python class

# python class -> sqlalchemy model -> user db table

# password should store hash value in db using bcrypt



# import garney tarika
from src.extensions import db

# creating python class called user , sqlalchemy lai this is db model 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime,default=db.func.now(),onupdate=db.func.now(),nullable=False)

