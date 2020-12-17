import functools

from flask import Blueprint, url_for, render_template, flash, request, session , g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from sqlalchemy import or_, and_

from app import db
from app.forms import UserCreateForm, UserLoginForm , FriendRequestForm
from app.models import User, UserRelationship


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

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
                return redirect(url_for('auth.mp'))
        flash(error)
    return render_template('auth/mypage.html', form = form, friend_list = friend_list)

@bp.route('/mypage/accept/<int:relation_id>')
def request_accept(relation_id):
    relation = UserRelationship.query.get(relation_id)
    relation.Type = 1
    db.session.commit()
    return redirect(url_for('auth.mp'))

@bp.route('/mypage/deny/<int:relation_id>')
def request_deny(relation_id):
    relation = UserRelationship.query.get(relation_id)
    db.session.delete(relation)
    db.session.commit()
    return redirect(url_for('auth.mp'))

@bp.route('/mypage/delete/<int:relation_id>')
def request_delete(relation_id):
    relation = UserRelationship.query.get(relation_id)
    db.session.delete(relation)
    db.session.commit()
    return redirect(url_for('auth.mp'))