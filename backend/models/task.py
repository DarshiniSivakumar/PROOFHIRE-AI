from extensions import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    task_type = db.Column(db.String(50), nullable=False)

    difficulty = db.Column(
        db.String(20),
        default='medium'
    )

    time_limit = db.Column(db.Integer, default=30)

    roles = db.Column(db.String(200))

    points = db.Column(db.Integer, default=100)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )