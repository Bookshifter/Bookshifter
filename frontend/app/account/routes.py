from flask import render_template, redirect, url_for, session
from app.account import bp
from flask import current_app
from app.authentication import functions as auth

@bp.route('/shelf/account')
def account():
    session_active = auth.verify_session(session)
    if not session_active:
        return redirect(url_for('authentication.login'))
    return render_template('/account/account.html')