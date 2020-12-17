from datetime import datetime

from flask import Blueprint, render_template, request, url_for , g , flash
from werkzeug.utils import redirect

from .. import db
from ..forms import GoalForm, AttendanceForm
from ..models import Goal

from app.views.auth_views import login_required

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
@login_required
def create():
    form = GoalForm()
    if request.method == 'POST' and form.validate_on_submit():
        goal = Goal(subject=form.subject.data, content=form.content.data, create_date=datetime.now() , user=g.user)
        db.session.add(goal)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('goal/goal_form.html', form=form)

@bp.route('/modify/<int:goal_id>', methods=('GET', 'POST'))
@login_required
def modify(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    if g.user != goal.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('goal.detail', goal_id=goal_id))
    if request.method == 'POST':
        form = GoalForm()
        if form.validate_on_submit():
            form.populate_obj(goal)
            goal.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('goal.detail', goal_id=goal_id))
    else:
        form = GoalForm(obj=goal)
    return render_template('goal/goal_form.html', form=form)

@bp.route('/delete/<int:goal_id>')
@login_required
def delete(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    if g.user != goal.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('goal.detail', goal_id=goal_id))
    db.session.delete(goal)
    db.session.commit()
    return redirect(url_for('goal._list'))