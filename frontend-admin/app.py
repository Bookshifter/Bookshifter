from flask import Flask, render_template, redirect, request, flash, url_for, jsonify, make_response

import requests
import functions.api as api

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'dev'

# VIEWS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index-2')
def index2():
    return render_template('index-backup.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')

@app.route('/all-tickets')
def all_tickets():
    return render_template('all-tickets.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    url_api = 'http://localhost:8080/'
    if request.method == 'POST':
        form = dict(request.form)
        # url_login = f'http://localhost:8080/teste'
        # response = api.api_books(url_login, 'POST')
        flash('Login falhou!')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/register/enable', methods=['GET', 'POST'])
def register_enable():
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
    
    return redirect(url_for('register'))

@app.route('/forgot-password', methods=['GET', 'POST'])
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
        return redirect(url_for('forgot_password'))
    return render_template('forgot-password.html')

@app.route('/password-reset', methods=['GET', 'POST'])
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
            return redirect(url_for('password_reset', token=token))
        
        flash('Redefinição de senha concluída!', 'success')
        return redirect(url_for('login'))
    return render_template('reset-password.html')


# OTHER VIEWS

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/forms/join')
def join():
    return render_template('join.html')

@app.route('/forms/mac')
def mac():
    return render_template('mac.html')

@app.route('/forms/vlan')
def vlan():
    return render_template('vlan.html')

@app.route('/forms/prefix')
def prefix():
    return render_template('prefix.html')

@app.route('/forms/noc')
def noc():
    return render_template('noc.html')

@app.route('/forms/nocg')
def nocg():
    return render_template('nocg.html')

@app.route('/forms/join/review')
def review_join():
    return render_template('review-join.html')

@app.route('/forms/mac/review')
def review_mac():
    return render_template('review-mac.html')

@app.route('/forms/vlan/review')
def review_vlan():
    return render_template('review-vlan.html')

@app.route('/forms/prefix/review')
def review_prefix():
    return render_template('review-prefix.html')

@app.route('/forms/noc/review')
def review_noc():
    return render_template('review-noc.html')

@app.route('/forms/nocg/review')
def review_nocg():
    return render_template('review-nocg.html')

# UI KITS

@app.route('/icons')
def icons():
    return render_template('ui-icons.html')

@app.route('/widgets')
def widgets():
    return render_template('ui-widgets.html')

@app.route('/elements')
def elements():
    return render_template('ui-elements.html')

@app.route('/buttons')
def buttons():
    return render_template('ui-buttons.html')

@app.route('/panels')
def panels():
    return render_template('ui-panels.html')

@app.route('/typography')
def typography():
    return render_template('ui-typography.html')

@app.route('/portlet')
def portlet():
    return render_template('ui-portlet.html')

@app.route('/alerts-popups')
def alerts_popups():
    return render_template('ui-alerts-popups.html')

@app.route('/sliders')
def sliders():
    return render_template('ui-sliders.html')

@app.route('/lists')
def lists():
    return render_template('ui-lists.html')

@app.route('/tour')
def tour():
    return render_template('ui-tour.html')

@app.route('/nestable')
def nestable():
    return render_template('ui-nestable.html')

@app.route('/autocomplete')
def autocomplete():
    return render_template('ui-autocomplete.html')

@app.route('/slide-menu')
def slide_menu():
    return render_template('ui-slide-menu.html')

# FORMS

@app.route('/form-elements')
def form_elements():
    return render_template('form-elements.html')

@app.route('/form-validation')
def form_validation():
    return render_template('form-validation.html')

@app.route('/form-wizards')
def form_wizards():
    return render_template('form-wizards.html')

@app.route('/form-editors')
def form_editors():
    return render_template('form-editors.html')

@app.route('/form-layouts-one-column')
def form_layouts_one_column():
    return render_template('form-layouts-one-column.html')

@app.route('/form-layouts-two-column')
def form_layouts_two_column():
    return render_template('form-layouts-two-column.html')

@app.route('/form-layouts-tabbed')
def form_layouts_tabbed():
    return render_template('form-layouts-tabbed.html')

@app.route('/form-file-handling')
def form_file_handling():
    return render_template('form-file-handling.html')

@app.route('/form-layouts-separated')
def form_layouts_separated():
    return render_template('form-layouts-separated.html')

# TABLES

@app.route('/table-basic')
def table_basic():
    return render_template('table-basic.html')

@app.route('/table-datatables')
def table_datatables():
    return render_template('table-datatables.html')

@app.route('/table-export')
def table_export():
    return render_template('table-export.html')

# CHARTS

@app.route('/charts-morris')
def charts_morris():
    return render_template('charts-morris.html')

@app.route('/charts-nvd3')
def charts_nvd3():
    return render_template('charts-nvd3.html')

@app.route('/charts-rickshaw')
def charts_rickshaw():
    return render_template('charts-rickshaw.html')

@app.route('/charts-other')
def charts_other():
    return render_template('charts-other.html')

# MAPS

@app.route('/maps')
def maps():
    return render_template('maps.html')

# PAGES

@app.route('/pages-gallery')
def pages_gallery():
    return render_template('pages-gallery.html')

@app.route('/pages-invoice')
def pages_invoice():
    return render_template('pages-invoice.html')

@app.route('/pages-profile')
def pages_profile():
    return render_template('pages-profile.html')

@app.route('/pages-address-book')
def pages_address_book():
    return render_template('pages-address-book.html')

@app.route('/pages-timeline')
def pages_timeline():
    return render_template('pages-timeline.html')

@app.route('/pages-timeline-simple')
def pages_timeline_simple():
    return render_template('pages-timeline-simple.html')

@app.route('/pages-mailbox-inbox')
def pages_mailbox_inbox():
    return render_template('pages-mailbox-inbox.html')

@app.route('/pages-mailbox-message')
def pages_mailbox_message():
    return render_template('pages-mailbox-message.html')

@app.route('/pages-mailbox-compose')
def pages_mailbox_compose():
    return render_template('pages-mailbox-compose.html')

@app.route('/pages-calendar')
def pages_calendar():
    return render_template('pages-calendar.html')

@app.route('/pages-tasks')
def pages_tasks():
    return render_template('pages-tasks.html')

@app.route('/pages-content-table')
def pages_content_table():
    return render_template('pages-content-table.html')

@app.route('/pages-faq')
def pages_faq():
    return render_template('pages-faq.html')

@app.route('/pages-search')
def pages_search():
    return render_template('pages-search.html')

@app.route('/pages-blog-list')
def pages_blog_list():
    return render_template('pages-blog-list.html')

@app.route('/pages-blog-post')
def pages_blog_post():
    return render_template('pages-blog-post.html')

@app.route('/pages-lock-screen', methods=['GET', 'POST'])
def pages_lock_screen():
    if request.method == 'POST':
        return redirect('/')
    return render_template('pages-lock-screen.html')

@app.route('/pages-login')
def pages_login():
    return render_template('pages-login.html')

@app.route('/pages-login-v2')
def pages_login_v2():
    return render_template('pages-login-v2.html')

@app.route('/pages-login-inside')
def pages_login_inside():
    return render_template('pages-login-inside.html')

@app.route('/pages-login-website')
def pages_login_website():
    return render_template('pages-login-website.html')

@app.route('/pages-registration-login')
def pages_registration_login():
    return render_template('pages-registration-login.html')

@app.route('/pages-error-404')
def pages_error_404():
    return render_template('pages-error-404.html')

@app.route('/pages-error-404-2')
def pages_error_404_2():
    return render_template('pages-error-404-2.html')

@app.route('/pages-error-500')
def pages_error_500():
    return render_template('pages-error-500.html')
    

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)