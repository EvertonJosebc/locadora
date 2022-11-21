from django.shortcuts import render, redirect, get_object_or_404
from .models import Locacao, Cliente, Categoria, Filme
from .forms import locacaoForm

# Create your views here.
def locacaoList(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locacoes/lists.html', {'locacoes': locacoes})

def locacaoView(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    return render(request, 'locacoes/locacao.html', {'locacao': locacao})

def newLocacao(request):
    if request.method == 'POST':
        form = locacaoForm(request.POST)
        
        if form.is_valid():
            locacao = form.save()
            return redirect('/')
    else:     
        form = locacaoForm()
        return render(request, 'locacoes/addLocacao.html', {'form': form})