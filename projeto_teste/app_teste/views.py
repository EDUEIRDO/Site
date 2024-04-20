from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FuncionarioForm

def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teste.html')
    else:
        form = FuncionarioForm()
    return render(request, 'index.html', {'form': form})

def pagina_sucesso(request):
    return render('teste.html')