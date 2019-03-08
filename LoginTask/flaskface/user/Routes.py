from flaskface import app, db, bcrypt
from flask import render_template, redirect, request, flash, url_for, Blueprint, jsonify
from flaskface.user.Forms import RegisterForm, LoginForm, AccountForm
from flaskface.Models import User, UserSchema, Post
from flask_login import login_user, current_user, logout_user, login_required
from marshmallow import pprint
from flaskface.user.Utils import save_picture


user = Blueprint('user', __name__)


@user.route('/registers', methods=['POST', 'GET'])
def registers():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        # hashed_passeord = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.name.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        schema = UserSchema()
        result = schema.dump(user)
        pprint(result.data)
        flash('Login Successfully', 'success')
        return redirect(url_for('main.home'))

    return render_template('Register.html', title='Register', form=form)


@user.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('LoginForm.html', form=form, title='Login')


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@user.route('/account', methods=['POST', 'GET'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.name.data = current_user.name
    image_file = url_for('static', filename='profile_pic/'+current_user.image_file)
    return render_template('Account.html', title='Account', form=form, image_file=image_file)


@user.route('/user/<string:username>')
@login_required
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.create_at.desc()).paginate(page=page, per_page=5, error_out=False)
    return render_template('UserPosts.html', posts=posts, user=user)
