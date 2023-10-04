from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://admin:adminadmin@cluster0.dkkdm28.mongodb.net/site_calculadora'
app.config['SECRET_KEY'] = '823857g9fe0g0jj;.;.pl[ork9kh0jr98jr]'
mongo = PyMongo(app)

from view import *

if __name__ == '__main__':
    app.run(debug=True)