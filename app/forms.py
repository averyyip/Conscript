from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	oauth = StringField("oauth", validators=[DataRequired()])
	remember_me = BooleanField("remember_me", default=False)