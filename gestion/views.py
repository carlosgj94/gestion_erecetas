from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

@login_required
class IndexView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'gestion/index.html', context)

class LoginView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'gestion/login.html', context)
    def post(self, request):
        print(request.POST)

