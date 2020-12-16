from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from ..forms import GoalForm, AttendanceForm
from ..models import Goal

bp = Blueprint('goal', __name__, url_prefix='/goal')


@bp.route('/list/')
def _list():
    goal_list = Goal.query.order_by(Goal.create_date.desc())
    return render_template('goal/goal_list.html', goal_list=goal_list)


@bp.route('/detail/<int:goal_id>/')
def detail(goal_id):
    form = AttendanceForm()
    goal = Goal.query.get_or_404(goal_id)
    return render_template('goal/goal_detail.html', goal=goal, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = GoalForm()
    if request.method == 'POST' and form.validate_on_submit():
        goal = Goal(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(goal)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('goal/goal_form.html', form=form)
