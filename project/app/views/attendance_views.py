from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from .. import db
from ..forms import AttendanceForm
from ..models import Goal, Attendance

from .auth_views import login_required

bp = Blueprint('attendance', __name__, url_prefix='/attendance')


@bp.route('/create/<int:goal_id>', methods=('POST',))
@login_required
def create(goal_id):
    form = AttendanceForm()
    goal = Goal.query.get_or_404(goal_id)
    if form.validate_on_submit():
        content = request.form['content']
        attendance = Attendance(content=content, create_date=datetime.now() , user=g.user)
        goal.attendance_set.append(attendance)
        db.session.commit()
        return redirect(url_for('goal.detail', goal_id=goal_id))
    return render_template('goal/goal_detail.html', goal=goal, form=form)
