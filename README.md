# Markdownify

Módulo que permite no django converter markdown em HTML 😎!
* Na imagem em baixo, a variável `texto` tem texto com marcadores markdown (`#` e `##` para especificar titulos, `*` listar não ordenadamente, `1.` para lista ordenada, `**` para bold, `__` para itálico, ...)
* a variável `texto` é passada como contexto na função `render`, para o template HTML
* no ficheiro HTML a variável é renderizada, usando-se o filtro `markdownify`em `{{ texto|markdownify }}`. Super simples!
* Veja como resulta a conversão em HTML.

![image](https://user-images.githubusercontent.com/42048382/185496189-853692a2-01aa-434f-8883-d55aac8a54e8.png)

Referencia: [[django-markdownify]](https://django-markdownify.readthedocs.io/en/latest/index.html#)

## Passos

1. instalar: `pipenv install django-markdownify`

1. Na aplicação django, em `settings.py`: 
    * adicionar `markdownify`a `INSTALLED_APPS`
    * especificar os elementos HTML que queremos converter com markdownify:

```python
# settings.py

INSTALLED_APPS = [
 …
 'markdownify.apps.MarkdownifyConfig',
]


MARKDOWNIFY = {
   "default": {
      "WHITELIST_TAGS": [
        'a', 'abbr', 'acronym', 
        'strong', 'b',
        'blockquote', 'em', 'i',
        'ul', 'li', 'ol',
        'p',
        'h1', 'h2', 'h3', 'h4',
      ]
   },

   "alternative": {
      "WHITELIST_TAGS": ["a", "p"],
      "MARKDOWN_EXTENSIONS": ["markdown.extensions.fenced_code", ]
   }
}
```

3. Na página html onde queremos usar:
    * carregar o filtro
    * utilizar o filtro nas variáveis que usarmos ou [passarmos](https://github.com/ULHT-PW/markdown/blob/8f43a5d030505d46ae2c1c9c3b16d702291ed8b3/app/views.py#L6):


```html
<!-- pagina.html -->

{% load markdownify %}

<div>
   {{ texto | markdownify }}
</div>
```
