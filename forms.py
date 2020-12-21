from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, TextAreaField


class Newsform(FlaskForm):
    header = StringField('Заголовок', validators=[DataRequired(), Length(min=5, max=50)])
    body = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField("Добавить")
