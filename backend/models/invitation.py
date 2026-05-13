from extensions import db
from datetime import datetime

class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(
        db.String(120),
        nullable=False
    )

    candidate_role = db.Column(
        db.String(50),
        nullable=False
    )

    token = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default='pending'
    )

    invited_by = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    invited_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    expires_at = db.Column(db.DateTime)