# NO ARQUIVO urls.py da pasta blog
*esse post_slug é o nome que é usado dentro das funções que são feitas na view
*elas só tão assim, pq na urls do blog_web foi feito um path que inicia com o blog/
*e depois deu um include nessas urls aqui

## SOBRE AS VIEWS
AS VIEWS SÃO USADAS PRA DIZER O QUE VAI SER MOSTRADO NA TELA, ENTÃO É LÁ QUE VC FAZ A FUNÇÃO PRA RENDERIZAR
ALGO. ELAS DEVEM NO FINAL TER ALGO ASSIM 
```return render(request, NOMEDOARQUIVO.HTML, OBJETOPRAUSARNOHTML)```

## SOBRE OS TEMPLATES
Se você olhar os templates da pasta /blog_web/src é mais fácil.
Eu tenho um base.html, ele literalmente é a base dos outros, lá dentro eu defino duas coisas que vão se alterar.
```<title>{% block head_title %} {% endblock %} </title>``` 
E ```{% block content%} {% endblock %}```
Os blocos são coisas que vc altera o contúdo deles adicionando algo no meio, assim como as tags.
Ah, no base, também tem uns ```{% include 'navbar.html' %}```
Isso é usado ao invés de ter o código ali, vc deixa em um arquivo html e só da o include aonde vc quer ter.

Aí nos arquivos que eu uso o base, tem o extends no início.

Nos forms, você vai ver que tá lá ```{{ form.as_p }}```
Isso é só pra que o formulário seja feito com tags <p>
Tem também .as_table e .as_ul das listas lá, veja qual fica melhor pra ti.

########### ADMIN.PY
Não esquece de adicionar essa linha lá no admin da pasta do teu model
```admin.site.register(<<NOMEDOMODEL>>)```