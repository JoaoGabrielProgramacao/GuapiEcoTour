from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_pt = db.Column(db.String(100))
    name_en = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    summary_pt = db.Column(db.String(300))
    summary_en = db.Column(db.String(300))
    description_pt = db.Column(db.Text)
    description_en = db.Column(db.Text)

    hours_pt = db.Column(db.String(100))
    hours_en = db.Column(db.String(100))
    trail_diff_pt = db.Column(db.String(50))
    trail_diff_en = db.Column(db.String(50))
    best_season_pt = db.Column(db.String(100))
    best_season_en = db.Column(db.String(100))

    history_pt = db.Column(db.Text, nullable=True)
    history_en = db.Column(db.Text, nullable=True)
    access_difficulty_pt = db.Column(db.String(50), nullable=True)
    access_difficulty_en = db.Column(db.String(50), nullable=True)
    location_details_pt = db.Column(db.String(200), nullable=True)
    location_details_en = db.Column(db.String(200), nullable=True)
    environmental_tips_pt = db.Column(db.Text, nullable=True)
    environmental_tips_en = db.Column(db.Text, nullable=True)
    contact_phone = db.Column(db.String(50), nullable=True)
    contact_email = db.Column(db.String(100), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    trail_time_min = db.Column(db.Integer, nullable=True)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    point_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('favorites', lazy=True))
    point = db.relationship('Point', backref=db.backref('favorited_by', lazy=True))