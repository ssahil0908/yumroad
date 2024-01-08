from flask import Blueprint, render_template, redirect, url_for , flash
from flask_login import login_user,current_user , logout_user



from yumroad.extensions import login_manager
from yumroad.models import User, db , Store
from yumroad.forms import SignupForm , LoginForm 
from yumroad.email import send_pretty_welcome_message

user_bp = Blueprint('user', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@user_bp.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in", 'warning')
        return redirect(url_for("products.index"))
    form = SignupForm()
    if form.validate_on_submit():
        user = User.create(form.email.data, form.password.data)
        db.session.add(user)
        store = Store(name=form.store_name.data, user=user)
        db.session.add(store)
        db.session.commit()
        login_user(user)
        # send_pretty_welcome_message(user)
        flash("Registered successfully.", "success")
        return redirect(url_for("products.index"))

    return render_template("users/register.html", form=form)

@user_bp.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in", "warning")
        return redirect(url_for('products.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("products.index"))
        else:
            flash("Invalid email or password. Please try again.", "danger")

    return render_template("users/login.html", form=form)

@user_bp.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("landing.index"))