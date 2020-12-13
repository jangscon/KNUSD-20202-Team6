from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.utils import redirect
from sqlalchemy import or_, and_

from app import db

from app.forms import FriendRequestForm
from app.models import User, UserRelationship

bp = Blueprint('mypage', __name__, url_prefix='/mypage')

@bp.route('/mypage/', methods=('GET', 'POST'))
def mp():
    form = FriendRequestForm()
    user_id = session.get('user_id')
    friend_list = UserRelationship.query.filter(or_(UserRelationship.Related == user_id, UserRelationship.Relating == user_id))
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자 입니다."
        if error is None:
            for friend in friend_list:
                if friend.Related == user_id and friend.Relating == user.id:
                    error = "이미 보낸 요청입니다."
                    break
                elif friend.Related == user.id and friend.Relating == user_id:
                    error = "이미 받은 요청입니다."
                    break
            if error is None:
                new_r = UserRelationship(Relating = user_id,
                                         Related = user.id,
                                         Relating_name = User.query.get(user_id).username,
                                         Related_name = User.query.get(user.id).username,
                                         Type = 0)
                db.session.add(new_r)
                db.session.commit()
                return redirect(url_for('mypage.mp'))
        flash(error)
    return render_template('mypage/mypage.html', form = form, friend_list = friend_list)

@bp.route('/mypage/accept/<int:relation_id>')
def request_accept(relation_id):
    relation = UserRelationship.query.get(relation_id)
    relation.Type = 1
    db.session.commit()
    return redirect(url_for('mypage.mp'))

@bp.route('/mypage/deny/<int:relation_id>')
def request_deny(relation_id):
    relation = UserRelationship.query.get(relation_id)
    db.session.delete(relation)
    db.session.commit()
    return redirect(url_for('mypage.mp'))

@bp.route('/mypage/delete/<int:relation_id>')
def request_delete(relation_id):
    relation = UserRelationship.query.get(relation_id)
    db.session.delete(relation)
    db.session.commit()
    return redirect(url_for('mypage.mp'))