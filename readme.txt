    # Desafio Django - API de Usuários, Pedidos e Itens

Este projeto é uma **API RESTful** desenvolvida com **Django Rest Framework (DRF)** para gerenciar usuários, itens e pedidos. A API permite autenticação, autorização, validação de dados e gerenciamento completo das entidades envolvidas.

---

## Índice

- [Requisitos](#requisitos)  
- [Estrutura do Projeto](#estrutura-do-projeto)  
- [Instalação e Configuração](#instalação-e-configuração)  
- [Autenticação](#autenticação)  
- [Endpoints](#endpoints)  
- [Uso do Git](#uso-do-git)  
- [Critérios de Avaliação](#critérios-de-avaliação)  

---



## Requisitos

- Python 3.10+  
- Django 5.2+  
- Django Rest Framework  
- djangorestframework-simplejwt (para JWT)  
- SQLite (banco de dados padrão)  

---

## Estrutura do Projeto

project/
│
├── backend/
│ ├── usuarios/ # App de usuários
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ └── urls.py
│ │
│ ├── itens/ # App de itens
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ └── urls.py
│ │
│ ├── pedidos/ # App de pedidos
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ └── urls.py
│ │
│ ├── settings.py
│ └── urls.py
│
└── manage.py


---

## Instalação e Configuração

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd project


Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows


Instale as dependências:

pip install -r requirements.txt


Execute as migrações do banco de dados:

python manage.py makemigrations
python manage.py migrate


Crie o superusuário inicial (opcional):

python manage.py createsuperuser


Execute o servidor de desenvolvimento:

python manage.py runserver


O servidor estará disponível em http://127.0.0.1:8000/.

Autenticação

A API utiliza JWT (JSON Web Token) para autenticação.

Endpoint de login: POST /auth/login/

Recebe email e senha.

Retorna access e refresh tokens.

Para acessar rotas protegidas, inclua o token Authorization: Bearer <ACCESS_TOKEN> no header da requisição.

Endpoints Principais
Usuários

POST	/usuarios/	Cria um usuário (admin ou normal) - o camo is_admin = true cria um usuário admin.
{
  "nome": "Admin",
  "email": "gunguner123@gmail.com",
  "senha": "123",
  "is_admin": true
}



GET	/usuarios/todos/	Lista todos os usuários (admin)


PUT	/usuarios/<id>/	Atualiza dados do usuário



DELETE	/usuarios/<id>/	Remove usuário (admin)
Itens
Método	URL	Descrição
POST	/items/	Cria novo item

{
  "nome": "Livro Teste",
  "preco": 50.00
}
GET	/items/todos/	Lista todos os itens (admin apenas)
PUT	/items/<id>/	Atualiza item
{
  "nome": "Livro Atualizado",
  "preco": 55.00
}

DELETE	/items/<id>/	Remove item
Pedidos
Método	URL	Descrição
POST	/pedidos/	Cria um novo pedido para o usuário logado
{
  "itens": [
    {
      "item_id": "uuid-do-item1",
      "quantidade": 2
    },
    {
      "item_id": "uuid-do-item2",
      "quantidade": 3
    }
  ]
}

GET	/pedidos/todos/	Lista todos os pedidos do usuário logado

GET	/pedidos/<id>/	Mostra detalhes de um pedido específico
DELETE	/pedidos/<id>/	Remove um pedido


Observações

Senhas de usuários são armazenadas com hash seguro (make_password do Django)

Apenas usuários com is_admin=True podem criar novos administradores

O valor total do pedido é calculado automaticamente com base nos itens e suas quantidades