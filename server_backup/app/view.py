from flask import *
from templates import *
from control import app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')