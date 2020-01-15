from django.shortcuts import render
from django.http import HttpResponse
from hashlib import md5
from datetime import datetime
from .models import User
from .forms import UserForm
from sqlite3 import *

data=dict()
def get_user(request):
    global data
    if 'user' in request.session:
        user = request.session['user']
    else:
        user='Гость'
    data['user']=user

def signup(request):
    global data
    get_user(request)
    if request.method=="POST":
        # Извлечение данных:
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # Создание набора данных
        # data = dict()
        data['report'] = 'Отчёт по умолчанию'

        # Проверка совпадения паролей:
        if pass1 != pass2:
            data['report'] = 'Пароли не совпадают!'
        else:
            # Хеширование пароля:
            _byte = pass1.encode()
            _hash = md5(_byte)
            passw = _hash.hexdigest()

            # Определение времени регистрации:
            now = datetime.now()
            regdate = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
            status = 'norm'

            # Контроль данных
            """
            data['login'] = login
            data['pass1'] = pass1
            data['pass2'] = pass2
            data['email'] = email
            data['passw'] = passw
            data['regdate'] = regdate
            data['status'] = status
            """
            # Сохранение данных в базе:
            new_user = User()
            new_user.login = login
            new_user.passw = passw
            new_user.email = email
            new_user.regdate = regdate
            new_user.status = status
            new_user.save()

            # Final result:
            data['report'] = 'Регистрация успешно завершена!'

        # Отправка данных на страницу отчёта:

        return render(request, 'account/signup_res.html', context=data)
    else:

        return render(request, 'account/signup.html', context=data)


def signin(request):
    global data
    get_user(request)
    if request.method=="POST":
        _login = request.POST.get('login')
        _pass1=request.POST.get('pass1')
        # data = dict()
        data['login'] = _login
        data['passw1'] = _pass1
        #хеширование
        _byte = _pass1.encode()
        _hash = md5(_byte)
        _passw = _hash.hexdigest()

        #проверка пользователя
        try:
            user=User.objects.get(login=_login, passw=_passw)
            data['report'] = 'С возвращением '
            data['x_color']='green'
            request.session['user']=_login

        except User.DoesNotExist as err:
            data['report'] = 'Авторизация провалена '
            data['x_color']='red'

        return render(request, 'account/signin_res.html', context=data)



    else:
        return render(request, 'account/signin.html', context=data)

def signout(request):
    return render(request, 'account/signout.html')