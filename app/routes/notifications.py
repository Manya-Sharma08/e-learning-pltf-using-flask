from flask import Blueprint
from flask_login import login_required, current_user
from app import socketio
from flask_socketio import emit

notif_bp = Blueprint('notifications', __name__)

@notif_bp.route('/notify')
@login_required
def notify():
    message = f"Hello {current_user.email}, new course available!"
    socketio.emit('notification', {'message': message}, broadcast=True)
    return 'Notification sent!'
