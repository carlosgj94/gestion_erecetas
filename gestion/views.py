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
        try:
            medico = Medico.objects.get(user=userObj)
        except Medico.DoesNotExist:
            medico=None
        try:
            farmaceutico = Farmaceutico.objects.get(user= userObj)
        except Farmaceutico.DoesNotExist:
            farmaceutico=None
        if medico != None:
            return render(request, 'gestion/menu_medico.html', context)
        if farmaceutico!=None:
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

class NuevaRecetaView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
         userObj= request.user

         try:
            medico = Medico.objects.get(user=userObj)
         except Medico.DoesNotExist:
            medico=None
         try:
            farmaceutico = Farmaceutico.objects.get(user= userObj)
         except Farmaceutico.DoesNotExist:
            farmaceutico=None

         if medico!=None:
             context = {
                 "username": userObj.username
             }

         elif farmaceutico!=None:
             context = {
                 "username": userObj.username,
                 "error":"Acceso no permitido"
             }
         return render(request, 'gestion/nueva_receta.html', context)
    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        userObj= request.user

        try:
            medico = Medico.objects.get(user=userObj)
        except Medico.DoesNotExist:
            medico=None
        try:
            farmaceutico = Farmaceutico.objects.get(user= userObj)
        except Farmaceutico.DoesNotExist:
            farmaceutico=None
        if farmaceutico!=None:
             context = {
                 "username": userObj.username,
                 "error":"Acceso no permitido"
             }
             return render(request, 'gestion/nueva_receta.html', context)
        if medico!=None:
            form = request.POST
            dni = form.get('dni')
            farmacos = form.get('farmacos')
            duracion = form.get('duracionDias')
            unidades = form.get("unidades")
            cadaCuantasHoras = form.get('cadaCuantasHoras')

            #HAY QUE COMPROBAR AQUI QUE EL FORMULARIO NO ESTA VACIO!
            pacienteObj = Paciente.objects.get(dni=dni)
            user = request.user
            medicoObj = Medico.objects.get(user=user)
            Receta.objects.create(medico=medicoObj,paciente=pacienteObj, farmacos=farmacos, duracionDias=duracion, unidades=unidades, cadaCuantasHoras=cadaCuantasHoras )
            context={
                "exito": "Receta creada con exito"
            }
            return render(request, 'gestion/nueva_receta.html', context)