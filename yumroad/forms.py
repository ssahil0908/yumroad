from flask_wtf import FlaskForm
from wtforms import PasswordField, validators
from wtforms.validators import Optional as OptionalValidator
from yumroad.models import User
from wtforms.fields import StringField, SubmitField , DecimalField
from wtforms.validators import Length
from werkzeug.security import  check_password_hash

class ProductForm(FlaskForm):
    name = StringField('Name', [Length(min=4, max=60)])
    description = StringField('Description')
    submit = SubmitField('Create')
    picture_url = StringField('Picture URL', description='Optional', validators=[ OptionalValidator() ,validators.URL()])
    price = DecimalField('Price', description='in USD, Optional')


class SignupForm(FlaskForm):
    email = StringField('Email', validators=[validators.email(), validators.InputRequired()])
    password = PasswordField('Password', validators=[validators.InputRequired(), validators.length(min=4),
                                                     validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', validators=[validators.InputRequired()])
    store_name = StringField('Store Name', validators=[validators.InputRequired(), validators.length(min=4)])

    #by default validate method runs for all the field
    # def validate(self):
    #     check_validate = super(SignupForm, self).validate()
    #     if not check_validate:
    #         return False

    #     # Does the user exist already? Must return false,
    #     # otherwise we'll allow anyone to sign in
    #     user_count = User.query.filter_by(email=self.email.data).count()
    #     if user_count > 0:
    #         self.email.errors.append('That email already has an account')
    #         return False
    #     return True

    def validate_email(self, field):
        # Does the user exist already? Must return False,
        # otherwise we'll allow anyone to sign in
        user_count = User.query.filter_by(email=field.data).count()
        if user_count > 0:
            raise validators.ValidationError('That email already has an account')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.email(), validators.InputRequired()])
    password = PasswordField('Password', validators=[validators.InputRequired()])

    def validate_user(self):
        # check_validate = super(LoginForm, self).validate()
        # if not check_validate:
        #     return False

        user = User.query.filter_by(email=self.email.data).first()

        if not user or not check_password_hash(user.password, self.password.data):
            self.email.errors.append('Invalid email or password')
            return False
        return True
