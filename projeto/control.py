# requests e rotas
from flask import Flask, render_template, request, redirect, url_for, session
from model import *

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('view_notes'))
    return render_template('login.html')
'''
if __name__ == '__main__':
    app.run(debug=True)