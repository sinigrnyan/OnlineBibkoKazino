from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cardNumber = request.form.get('cardNumber')
        password = request.form.get('password')

        user = User.query.filter_by(cardNumber=cardNumber).first()
        if user:
            if (user.password==password):
                flash('Вход в БибАккаунт выполнен', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Неправильный пароль :(', category='error')
        else:
            flash('Сначала зарегистрируйте карточку :P', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        cardNumber = request.form.get('cardNumber')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        securityCode=request.form.get('securityCode')
        expirationDateMonth=request.form.get('expirationDateMonth')
        expirationDateYear=request.form.get('expirationDateYear')
        Bibki=1000

        user = User.query.filter_by(cardNumber=cardNumber).first()
        if user:
            flash('Карточка уже зарегистрирована, вписывайте новую.', category='error')
        elif len(cardNumber) != 16:
            flash('Номер карточки должен состоять из 16 цыфорок.', category='error')
        elif len(securityCode) != 3:
            flash('Код безопасности должен состоять из 3 цыфорок.', category='error')
        elif len(expirationDateMonth)>2:
            flash('Месяц истечения срока действия должен состоять не больше чем из двух цыфорок', category='error')
        elif int(expirationDateYear)<2024:
            flash('У вас картока просрочена, в курсе?', category='error')
        elif len(securityCode) != 3:
            flash('Код безопасности должен состоять из 3 цыфорок.', category='error')
        elif len(first_name) < 2:
            flash('Тебя одной буквой зовут что-ли? "Я" - это не имя.', category='error')
        elif len(last_name) < 2:
            flash('Тебя одной буквой зовут что-ли? "Я" - это не фамилия.', category='error')
        elif password1 != password2:
            flash('По человечески пароли набери', category='error')
        elif len(password1) < 3:
            flash('Маленький пароль, пароль должен состоять МИНИМУМ из 3 букв.', category='error')
        else:
            new_user = User(cardNumber=cardNumber, first_name=first_name,last_name=last_name, password=password1,securityCode=securityCode, expirationDateMonth=expirationDateMonth, expirationDateYear=expirationDateYear, Bibki=Bibki)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('БибАккаунт создан!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
