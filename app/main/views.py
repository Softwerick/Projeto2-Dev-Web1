from flask import flash, redirect, render_template, session, url_for, request
from flask_login import login_required
from flask_login import login_required, login_user, logout_user
from app.models import Role, User, Produto
from app import db
from . import main
from .forms import NameForm, ProdutoForm, RegistrationForm


@main.route('/', methods=['GET', 'POST'])
def login():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.tabela'))
        flash('Invalid username or password.')
    return render_template('index.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    roles = Role.query.all()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Usuário registrado!')
        return redirect(url_for('main.login'))
    return render_template('cadastro.html', form=form, roles=roles)



@main.route('/tabela', methods=['GET', 'POST'])
@login_required
def tabela():
    roles = Role.query.all()
    produtos = Produto.query.all()
    return render_template('tabela.html', roles=roles, produtos=produtos)


@main.route('/produto', methods=['GET', 'POST'])
@login_required
def add_produto():
    form = ProdutoForm()
    roles = Role.query.all()
    if form.validate_on_submit():
        new_produto = Produto()
        new_produto.name = form.name.data
        new_produto.preco = form.preco.data
        new_produto.peso = form.peso.data
        new_produto.estoque = form.estoque.data
        db.session.add(new_produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso.')
        return redirect(url_for('main.tabela'))
    return render_template('produto.html', form=form, roles=roles)