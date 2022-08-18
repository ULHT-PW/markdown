from django.shortcuts import render

# Create your views here.
def index_view(request):

    texto = """
# Título

## Sub-título
Na string, as frases devem estar encostadas à esquerda, sem espaços, tal como o markdown, para que os marcadores funcionem.

## Outro Sub-título

Esta frase está num parágrafo.
Esta frase está noutro parágrafo.

Lista *não ordenada* (**garantir que há uma linha em branco antes da lista em baixo!**):

* item
* outro item
* mais outro item

Lista _ordenada_:

1. primeiro item
1. segundo item
1. terceiro item

"""

    return render (request, 'app/index.html', {'texto': texto})