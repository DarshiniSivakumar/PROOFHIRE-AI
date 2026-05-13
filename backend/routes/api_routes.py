from flask import Blueprint, jsonify, request
from flask_login import login_required
from models.user import User

api = Blueprint('api', __name__)

@api.route('/api/candidates')
def get_candidates():

    candidates = User.query.filter_by(role='candidate').all()

    result = []

    for c in candidates:
        result.append({
            "id": c.id,
            "name": c.name,
            "role": c.candidate_role,
            "overall_score": c.overall_score,
            "confidence_score": c.confidence_score,
            "status": c.status
        })

    return jsonify(result)