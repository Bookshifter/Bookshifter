from flask import render_template, request, redirect, url_for, flash
from app.account import bp
from flask import current_app

from datetime import datetime

@bp.route('/account')
def account():    
    return render_template('/account/account.html')