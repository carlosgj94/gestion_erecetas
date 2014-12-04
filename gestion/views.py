from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from gestion.models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

class IndexView(View):

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        userObj= request.user
        context = {
            "username": userObj.username
        }
        if Medico(user=userObj):
            return render(request, 'gestion/menu_medico.html', context)
        elif Farmaceutico(user=userObj):
            return render(request, 'gestion/menu_farmeceutico.html', context)
        return render(request, 'gestion/index.html', context)

class LoginView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'gestion/login.html', context)
    def post(self, request):
        print(request.POST)
        if request.method == "POST":
            form = request.POST

            codigo = form.get('codigo')
            passwd = form.get('password')
            userObj = User(username=codigo)
            print(userObj.username)
            user = authenticate(username=userObj.username, password=passwd)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    context={"username":userObj.username}

                    login(request, user)
                    redirect_url = "/"
                    return redirect(redirect_url)

                else:
                    print("The password is valid, but the account has been disabled!")
                    context = {
                    "error" : "La cuenta ha sido deshabilitada.",
                }
                return render(request, 'gestion/login.html', context)
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
                context = {
                    "error" : "El nombre de usuario o la contraseña son incorrectas.",
                }
                return render(request, 'gestion/login.html', context)