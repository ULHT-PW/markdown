# Usando markdownify
referencias: [[1]](https://django-markdownify.readthedocs.io/en/latest/index.html#)

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
    * utilizar o filtro nas variáveis que usarmos ou passarmos:

```html
<!-- pagina.html -->

{% load markdownify %}

<div>
   {{ texto | markdownify }}
</div>
```