from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, "hello/index.html")


def about_view(request):
    name = "Lucio"
    ano = 2022
    amigos = ['Bruno']
    quantidade_amigos = len(amigos)

    context = {
        'name': name,
        'ano': ano,
        'amigos': amigos,
        'quantidade_amigos': quantidade_amigos
    }

    return render(request, "hello/about.html", context)