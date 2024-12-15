import os

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(
    __name__,
    template_folder=os.path.abspath('template'),
    static_url_path=''
    )
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)