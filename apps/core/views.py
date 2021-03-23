from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..funcionarios.models import Funcionario


# Create your views here.
@login_required(login_url='accounts/login/')
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)
