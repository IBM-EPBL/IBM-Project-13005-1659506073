from imp import init_builtin
from flask import Flask, render_template, url_for, redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import g

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

def create_app():
    db.init_app(app)
    return app

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)