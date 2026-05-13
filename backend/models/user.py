from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    role = db.Column(db.String(20), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    candidate_role = db.Column(db.String(50))
    overall_score = db.Column(db.Float, default=0)
    confidence_score = db.Column(db.Float, default=0)

    status = db.Column(
        db.String(20),
        default='pending'
    )

    why_not_selected = db.Column(db.Text)

    skill_scores = db.Column(db.Text, default='{}')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_skill_scores(self):
        return json.loads(self.skill_scores) if self.skill_scores else {}

    def set_skill_scores(self, scores):
        self.skill_scores = json.dumps(scores)