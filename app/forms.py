from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateField, IntegerField
from wtforms.validators import Email, DataRequired, Length

class TripAdmin(FlaskForm):
    name = StringField("Наименование тура: ", validators=[DataRequired(), Length(max=150)])
    description=StringField("Подробности: ", validators=[DataRequired(), Length(max=5000)])
    date_begin=DateField("Начало: ", format='%Y-%m-%d')
    date_end=DateField("Окончание: ", format='%Y-%m-%d')
    is_all_inc=BooleanField("All inc?")
    submit = SubmitField("Добавить")