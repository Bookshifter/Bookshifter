from flask import render_template
from app.admin import bp
from flask import current_app

@bp.route('/history')
def history():
    return render_template('admin/history.html')

@bp.route('/logs')
def logs():
    return render_template('admin/logs.html')