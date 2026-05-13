from extensions import db
from datetime import datetime

class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    candidate_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    recruiter_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    interview_type = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default='scheduled'
    )

    scheduled_at = db.Column(
        db.DateTime,
        nullable=False
    )

    duration = db.Column(
        db.Integer,
        default=60
    )

    meeting_link = db.Column(db.String(500))

    location = db.Column(db.String(200))

    notes = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )