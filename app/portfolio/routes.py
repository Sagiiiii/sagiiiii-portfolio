from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from app import mail
from app.data.projects import get_all, get_featured, get_by_id, get_by_category
import os

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/')
def index():
    featured = get_featured()
    recent   = get_all()[:6]
    return render_template('portfolio/index.html', featured=featured, recent=recent)

@portfolio_bp.route('/projects')
def projects():
    category     = request.args.get('cat', '')
    all_projects = get_by_category(category) if category else get_all()
    return render_template('portfolio/projects.html',
        projects=all_projects, active_cat=category)

@portfolio_bp.route('/project/<int:id>')
def project_detail(id):
    project = get_by_id(id)
    if not project:
        return redirect(url_for('portfolio.index'))
    return render_template('portfolio/project.html', p=project)

@portfolio_bp.route('/about')
def about():
    return render_template('portfolio/about.html')

@portfolio_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name    = request.form.get('name', '').strip()
        email   = request.form.get('email', '').strip()
        subject = request.form.get('subject', 'Mensaje desde portfolio').strip()
        message = request.form.get('message', '').strip()

        try:
            msg = Message(
                subject    = f'[Portfolio] {subject}',
                sender     = os.getenv('CONTACT_EMAIL'),
                recipients = [os.getenv('CONTACT_EMAIL')],
                reply_to   = email,   # al responder va directo al visitante
                html       = f"""
                    <h2 style="color:#E8651A">
                        Nuevo mensaje desde tu portfolio 🦊
                    </h2>
                    <table style="border-collapse:collapse;width:100%;max-width:600px">
                        <tr>
                            <td style="padding:10px;font-weight:bold;
                                background:#f5f5f5;width:100px">Nombre</td>
                            <td style="padding:10px">{name}</td>
                        </tr>
                        <tr>
                            <td style="padding:10px;font-weight:bold;background:#f5f5f5">Email</td>
                            <td style="padding:10px">
                                <a href="mailto:{email}">{email}</a>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding:10px;font-weight:bold;background:#f5f5f5">Asunto</td>
                            <td style="padding:10px">{subject}</td>
                        </tr>
                        <tr>
                            <td style="padding:10px;font-weight:bold;background:#f5f5f5">Mensaje</td>
                            <td style="padding:10px">{message}</td>
                        </tr>
                    </table>
                    <p style="color:#999;font-size:12px;margin-top:20px">
                        Enviado desde tu portfolio · David.dev
                    </p>
                """
            )
            mail.send(msg)
            flash('✅ ¡Mensaje enviado! Te responderé pronto.', 'success')

        except Exception as e:
            flash(f'❌ Error: {str(e)}', 'danger')

        return redirect(url_for('portfolio.contact'))

    return render_template('portfolio/contact.html')

@portfolio_bp.route('/coming-soon')
def coming_soon():
    return render_template('portfolio/coming_soon.html')
