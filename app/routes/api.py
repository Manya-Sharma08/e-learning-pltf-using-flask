from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Course, UserInterest

api_bp = Blueprint('api', __name__)

@api_bp.route('/recommendations')
@login_required
def recommendations():
    interests = [i.interest for i in UserInterest.query.filter_by(user_id=current_user.id).all()]
    all_courses = Course.query.all()
    recommended = [c for c in all_courses if any(interest.lower() in c.title.lower() for interest in interests)]
    if not recommended:
        recommended = all_courses[:3]
    return jsonify([{'id': c.id, 'title': c.title} for c in recommended])
