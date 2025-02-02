from wtforms import StringField, FileField, TextAreaField, validators
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, DataRequired

class Createpost(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    body  = TextAreaField('body', validators=[DataRequired()])
    img = FileField('post', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])

class Updatepost(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    body  = TextAreaField('body', validators=[DataRequired()])
    img = FileField('post', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])