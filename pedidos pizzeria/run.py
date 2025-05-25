from flask import Flask
from models import db
from routes import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost/dengue_control'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
