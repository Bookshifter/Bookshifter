from flask import Flask, render_template, redirect, request, flash, url_for, make_response, session
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.authentication import bp, api
from flask import current_app
import json

# insert a /admin prefix in my routes.
# app.register_blueprint(admin_bp, url_prefix='/admin')
@bp.route('/login', methods=['GET', 'POST'])
def login():
    backend_url = current_app.config.get('BACKEND_API_URL')
    if request.method == 'POST':
        form = dict(request.form)
        url_login = backend_url + 'login'
        params = {
            'url': url_login,
            'data': form,
            'method': 'POST'
        }
        response, message = api.api_register(params)
        if 'error' in message:
            flash('Usuário ou senha errados! Tente novamente.', 'danger')
            return redirect(url_for('authentication.login'))
        else:
            token_string= f'{response}'
            token_login = json.loads(token_string)
            session['token'] = token_login['token']
            logged = make_response(redirect(url_for('dashboard.dashboard')))
            logged.headers['Authorization'] = f"Bearer {token_login['token']}"
            logged.set_cookie('Authorization', f"{token_login['token']}")
            logged.set_cookie('access_token_cookie', f"{token_login['token']}")
            
            # access_token = create_access_token(identity=form['email'])
            return logged
        
    return render_template('/authentication/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    backend_url = current_app.config.get('BACKEND_API_URL')
    if request.method == 'POST':
        form = dict(request.form)
        url_register = backend_url + 'register'        
        params = {
            'url': url_register,
            'data': form,
            'method': 'POST'
        }
        response, message = api.api_register(params=params)
        flash('Verifique sua conta via email para ativá-la!' if 'success' in message else message['error'], 'success' if 'success' in message else 'danger')
        return redirect(url_for('authentication.register'))
    
    return render_template('/authentication/register.html')

@bp.route('/register/enable', methods=['GET', 'POST'])
def register_enable():
    token = request.args.get('token')
    backend_url = current_app.config.get('BACKEND_API_URL')
    url_enable_account = backend_url + f'register/account?token={token}'
    params = {
            'url': url_enable_account,
            'method': 'GET'
        }
    response, message = api.api_register(params=params)
    flash('Sua conta foi ativada com sucesso!' if 'success' in message else message['error'], 'success' if 'success' in message else 'danger')
    return redirect(url_for('authentication.login'))

@bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    backend_url = current_app.config.get('BACKEND_API_URL')
    if request.method == 'POST':
        form = dict(request.form)
        url_register = backend_url + 'forgot-password'        
        params = {
            'url': url_register,
            'data': form,
            'method': 'POST'
        }
        response, message = api.api_register(params=params)
        flash('Verifique seu email para redefinir sua senha!' if 'success' in message else message['error'], 'success' if 'success' in message else 'danger')
        return redirect(url_for('authentication.forgot_password'))
    return render_template('/authentication/forgot-password.html')

@bp.route('/password-reset', methods=['GET', 'POST'])
def password_reset():
    token = request.args.get('token')
    backend_url = current_app.config.get('BACKEND_API_URL')
    if request.method == 'POST':
        form = dict(request.form)
        url_reset_password = backend_url + f'forgot-password/password-reset?token={token}'
        params = {
            'url': url_reset_password,
            'data': form,
            'method': 'POST'
        }
        response, message = api.api_register(params=params)
        if not 'success' in message:
            flash('Ocorreu um erro, tente novamente!', 'danger')
            return redirect(url_for('authentication.password_reset', token=token))
        
        flash('Redefinição de senha concluída!', 'success')
        return redirect(url_for('authentication.login'))
    return render_template('/authentication/reset-password.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Deslogado com sucesso!', 'success')
    return redirect(url_for('authentication.login'))