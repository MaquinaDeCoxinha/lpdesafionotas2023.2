# o que o usuário vai ver
from flask import render_template, request, redirect, url_for, flash
import logging
from app import app, mongo
from model import User, Nota
from control import login_user

@app.route('/')
def index():
    app.logger.info('Solicitação recebida na rota /')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.info('Solicitação recebida na rota /login')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificando se o usuário existe e se a senha é correspondente
        if login_user(username=username, password=password):
            return redirect(url_for('home'))
        #Login falho
        else:
            flash('Login inválido. Tente novamente por favor.')
    
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    app.logger.info('Solicitação recebida na rota /cadastro')
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Verificando se o usuário já existe
        existing_user = mongo.db.users.find_one({'username': username})

        if existing_user:
            # Se o usuário já existe
            flash('O nome de usuário já está sendo utilizado, tente novamente por favor.')
        else:
            # Criando um novo usuário
            new_user = User(username, password)
            mongo.db.users.insert_one(new_user.__dict__)

            # Redirecionando para página de login
            return redirect(url_for('login'))
        
    return render_template('cadastro.html')

@app.route('/cadnotas', methods=['GET', 'POST'])
def cadnotas():
    app.logger.info('Solicitação recebida na rota /cadnotas')
    if request.method == 'POST':
        # Obtenha os dados do formulário de cadastro de notas de alunos
        aluno_id = request.form['aluno_id']
        nota_p1 = float(request.form['nota_p1'])
        nota_p2 = float(request.form['nota_p2'])
        quantidade_listas = int(request.form['quantidade_listas'])
        # Certifique-se de associar a nota ao aluno que a está recebendo
        # Substitua 'user_id' pelo ID do usuário autenticado
        user_id = 'user_id'  # Substitua pelo ID do usuário autenticado
        new_aluno_nota = Nota(user_id, aluno_id, nota_p1, nota_p2, quantidade_listas)
        mongo.db.notas_alunos.insert_one(new_aluno_nota.__dict__)

        flash('Nota do aluno cadastrada com sucesso!', 'success')

    return render_template('cadnotas.html')

@app.route('/home', methods=['GET'])
def home():
    app.logger.info('Solicitação recebida na rota /home')
    notas = mongo.db.notas_alunos.find()
    return render_template('home.html', notas=notas)