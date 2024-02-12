from flask import Flask
from app.models import db
from app.routes import users_bp
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

    app.register_blueprint(users_bp, url_prefix='/users')

    if __name__ == '__main__':
        app.run(debug=True)
