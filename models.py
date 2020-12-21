from datetime import datetime

from main import db

"""
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(32), nullable=False)
    image_name = db.Column(db.String(20), nullable=False, default="default_pic.jpg")
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, header, description, price, category, image_name, location, user_id):
        self.header = header
        self.price = price
        self.description = description
        self.category = category
        self.image_name = image_name
        self.location = location
        self.user_id = user_id
        self.active = True


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), default="Имярек Имярекович")
    self_info = db.Column(db.String(256), default="Я не такой как все")
    avatar_file = db.Column(db.String(20), default='default_avatar.jpg')
    regiser_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    active_posts = db.Column(db.Integer, nullable=True)
    unactive_posts = db.Column(db.Integer, nullable=True)
    posts = db.relationship(Post, backref='author', lazy=True)

    def __init__(self, login, password):
        self.login = login
        self.password = password
"""

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, header, body):
        self.header = header
        self.body = body

db.create_all()