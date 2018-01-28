from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), StringField])
    name = StringField('name', validators=[DataRequired(), StringField])