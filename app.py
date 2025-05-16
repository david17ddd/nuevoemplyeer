# Archivo principal de la app Flask

from flask import Flask
from routes.auth import auth_bp
from routes.main import main_bp
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Inicialización
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

# Importación de modelos
def create_app():
    from models.user import User
    from models.employee import Employee
    db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    create_app()
    app.run(debug=True)
