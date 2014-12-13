from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import User


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    location = StringField('location', validators=None)
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
    email = StringField('email', validators=[Email()])
    learnTeach = SelectField('learnTeach', choices=[('l', 'Learn'), ('t', 'Teach')])
    skill = StringField('skill', validators=[DataRequired()])
    phone = StringField('phone', validators=None)

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user is not None:
            self.nickname.errors.append('This nickname is already in use. '
                                        'Please choose another one.')
            return False
        return True


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])
     
class DeleteForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    confirm = StringField('confirm', validators=[DataRequired(), EqualTo('nickname', message='Nickname must match')])
                                                                        
