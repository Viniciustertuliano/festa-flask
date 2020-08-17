from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)


from auth import bp as auth_bp
app.register_blueprint(auth_bp)


from festa import bp as festa_bp
app.register_blueprint(festa_bp, url_prefix='/convidados')
