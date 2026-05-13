from extensions import db
from datetime import datetime

class TaskSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    candidate_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    task_id = db.Column(
        db.Integer,
        db.ForeignKey('task.id'),
        nullable=False
    )

    submission = db.Column(db.Text, nullable=False)

    score = db.Column(db.Float)

    feedback = db.Column(db.Text)

    time_taken = db.Column(db.Integer)

    tab_switches = db.Column(db.Integer, default=0)

    submitted_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )