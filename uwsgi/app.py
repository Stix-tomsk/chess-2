import os

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
app = Flask(
    __name__,
    template_folder=os.path.abspath('template'),
    static_url_path=''
    )

app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import *

db.init_app(app)
with app.app_context():
    db.create_all()
    

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test')
def test():
    users = User.query.all()
    return f"{str(users[0].username)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)