import os
from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')

    # ── Configuración Gmail ──
    app.config['MAIL_SERVER']   = 'smtp.gmail.com'
    app.config['MAIL_PORT']     = 587
    app.config['MAIL_USE_TLS']  = True
    app.config['MAIL_USERNAME'] = os.getenv('CONTACT_EMAIL')
    app.config['MAIL_PASSWORD'] = os.getenv('GMAIL_PASSWORD')

    mail.init_app(app)

    from app.portfolio.routes import portfolio_bp
    app.register_blueprint(portfolio_bp)

    return app