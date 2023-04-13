# egi-api
EGI API é uma api desenvolvidada para um aplicativo chamado Eventos Gerenciáveis e Integrados.

## Instalação:
Obs: Preste atenção na sequência e na alternativa.

0. Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
```

Para que você tenha um ambiente de desenvolvimento o mais propício possível e não suge a sua máquina com muitas dependências que provavelmente você não irá usar em um outro projeto é importante estabelecer um ambiente de desenvolvimento para cada projeto. Um dos ambientes mais utilizados para o desenvolvimento em Django é o Virtualenv e para quem já está familiarizado com Docker pode usá-lo também.
[Virtualenv][https://virtualenv.pypa.io/en/latest/]
[Docker - Django][https://docs.docker.com/samples/django/]


1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Gere um `.env` local baseado em .env.example


3. Sincronize a base de dados:
```bash
python manage.py migrate
```

4. Crie um usuário (Administrador do sistema):
```bash
python manage.py createsuperuser
```

5. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
```bash
python manage.py runserver
```

## Instalação (Alternativa):
2. Crie um volume para o banco de dados
```bash
docker create volume egi-pgdata
```

3. Use o Docker compose
```bash
docker compose up --build
```

4. Sincronize a base de dados:
```bash
docker compose start db
docker compose exec api python manage.py migrations
docker compose exec api python manage.py migrate
```

5. Test a instalação carregando o container api
```bash
docker compose up
```

## Implementações
- Login/Logout
- Cadastro de pessoas JD / PJ
- Criação de eventos
- ...

## Tarefas para serem feitas
- Implementações de models
- Implementações de Views
- Implementações de routes

## Créditos
- [Leonardo Barros][https://github.com/LBarros77]

## Ajuda
Para relatar bugs ou fazer perguntas utilize o email leonprogramer@gmail.com
Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.

