from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError, IntegerField
from wtforms.validators import DataRequired
from app.models import User


class NameForm(FlaskForm):
    username = StringField('Digite seu login', validators=[DataRequired()])
    password = PasswordField('Digite sua senha', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    name = StringField('Digite seu nome', validators=[DataRequired()])
    username = StringField('Digite seu login', validators=[DataRequired()])
    email = StringField('Digite seu email', validators=[DataRequired()])
    password = PasswordField('Digite sua senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Usuário já registrado.")


class ProdutoForm(FlaskForm):
    name = StringField('Nome do produto', validators=[DataRequired()])
    preco = IntegerField('Preço do produto', validators=[DataRequired()])
    peso = IntegerField('Quantidade por embalagem', validators=[DataRequired()])
    estoque = IntegerField('Quantidade em estoque', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')


class EditProductForm(FlaskForm):
    name = StringField('Nome do produto', validators=[DataRequired()])
    preco = IntegerField('Preço do produto', validators=[DataRequired()])
    peso = IntegerField('Quantidade por embalagem', validators=[DataRequired()])
    estoque = IntegerField('Quantidade em estoque', validators=[DataRequired()])
    submit = SubmitField('Enviar')
