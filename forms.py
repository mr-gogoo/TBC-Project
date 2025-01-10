from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, length, equal_to


class ProductForm(FlaskForm):

    name=StringField("სათაური", validators=[DataRequired(),
                                            length(min=4, max=38)])
    text=TextAreaField("ტექსტი", validators=[DataRequired()])
    img=StringField("ფოტო", validators=[DataRequired()])


    submit = SubmitField("შენახვა")

class ItemForm(FlaskForm):

    name=StringField("სათაური", validators=[DataRequired(),
                                            length(min=4, max=38)])
    text=TextAreaField("ტექსტი", validators=[DataRequired()])
    img=StringField("ფოტო", validators=[DataRequired()])


    submit = SubmitField("შენახვა")

class ProForm(FlaskForm):

    name=StringField("სათაური", validators=[DataRequired(),
                                            length(min=4, max=38)])
    text=TextAreaField("ტექსტი", validators=[DataRequired()])
    img=StringField("ფოტო", validators=[DataRequired()
                                      ])


    submit = SubmitField("შენახვა")

class RegisterForm(FlaskForm):
    username = StringField("იუზერნეიმი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired(),length(min=8)])

    register = SubmitField("რეგისტრაცია")

class LoginForm(FlaskForm):
    username = StringField("იუზერნეიმი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired(),length(min=8)])

    login = SubmitField("ავტორიზაცია")

class LolForm(FlaskForm):

    name=StringField("სათაური", validators=[DataRequired()])
    text=TextAreaField("ტექსტი", validators=[DataRequired()])

