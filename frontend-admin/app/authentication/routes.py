from flask import Flask, render_template, redirect, request, flash, url_for, jsonify, make_response
from app.authentication import bp, api
from flask import current_app
import json

@bp.route('/login', methods=['GET', 'POST'])
def login():
    url_api = 'http://localhost:8080/'
    if request.method == 'POST':
        form = dict(request.form)
        url_login = url_api + 'rest-login'
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
            return render_template('/index/index.html', token=token_login['token'])
    return render_template('/authentication/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    url_api = 'http://localhost:8080/'
    if request.method == 'POST':
        form = dict(request.form)
        url_register = url_api + 'rest-register'        
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
    url_api = 'http://localhost:8080/'
    url_enable_account = url_api + f'rest-register/rest-enableAccount?token={token}'
    params = {
            'url': url_enable_account,
            'method': 'GET'
        }
    print(url_enable_account)
    response, message = api.api_register(params=params)
    flash('Sua conta foi ativada com sucesso!' if 'success' in message else message['error'], 'success' if 'success' in message else 'danger')
    return redirect(url_for('authentication.login'))

@bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    url_api = 'http://localhost:8080/'
    if request.method == 'POST':
        form = dict(request.form)
        url_register = url_api + 'rest-forgot-password'        
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
    url_api = 'http://localhost:8080/'
    if request.method == 'POST':
        form = dict(request.form)
        url_reset_password = url_api + f'rest-forgot-password/password-reset?token={token}'
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
