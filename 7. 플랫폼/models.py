from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fcuser(db.Model): 
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(64))
    useremail = db.Column(db.String(32), unique=True)
    username = db.Column(db.String(8))