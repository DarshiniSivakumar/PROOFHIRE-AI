from flask import Flask
from extensions import db, login_manager
from routes.api_routes import api

from models.user import User
from models.task import Task
from models.submission import TaskSubmission
from models.interview import Interview
from models.invitation import Invitation
from models.message import Message

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proofhire.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# HOME ROUTE
@app.route("/")
def home():
    return "ProofHire AI Backend Running"

# REGISTER API
app.register_blueprint(api)
from models.user import User
from extensions import db

@app.route("/seed")
def seed():
    u1 = User(
        name="Alex Chen",
        email="alex@test.com",
        role="candidate",
        candidate_role="frontend",
        overall_score=87,
        confidence_score=0.92,
        status="completed"
    )
    u1.set_password("123")

    u2 = User(
        name="Maria Garcia",
        email="maria@test.com",
        role="candidate",
        candidate_role="backend",
        overall_score=82,
        confidence_score=0.88,
        status="completed"
    )
    u2.set_password("123")

    db.session.add_all([u1, u2])
    db.session.commit()

    return "Seeded successfully"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)