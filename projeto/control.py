# requests e rotas
from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from model import *
from view import *

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://admin:adminadmin@cluster0.dkkdm28.mongodb.net/?retryWrites=true&w=majority'
mongo = PyMongo(app)

