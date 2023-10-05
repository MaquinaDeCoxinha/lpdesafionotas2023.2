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
        aluno_id = request.form['aluno_id']
        nota_p1 = request.form['nota_p1']
        nota_p2 = request.form['nota_p2']

        # Validar e converter nota_p1 para float
        try:
            nota_p1 = float(nota_p1)
        except ValueError:
            flash('Nota P1 deve ser um número válido', 'error')
            return render_template('cadnotas.html')

        # Validar e converter nota_p2 para float
        try:
            nota_p2 = float(nota_p2)
        except ValueError:
            flash('Nota P2 deve ser um número válido', 'error')
            return render_template('cadnotas.html')

        listas_raw = request.form['listas_raw']
        novo_aluno_nota = Nota(aluno_id=aluno_id, nota_p1=nota_p1, nota_p2=nota_p2, listas_string=listas_raw)
        mongo.db.notas_alunos.insert_one(novo_aluno_nota.__dict__)

        flash('Nota do aluno cadastrada com sucesso!', 'success')

    return render_template('cadnotas.html')

@app.route('/home', methods=['GET'])
def home():
    app.logger.info('Solicitação recebida na rota /home')
    notas = mongo.db.notas_alunos.find()
    return render_template('home.html', notas=notas)