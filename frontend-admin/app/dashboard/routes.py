from flask import render_template, redirect, url_for, session
from app.dashboard import bp
from flask import current_app
from app.authentication import functions as auth

@bp.route('/shelf/dashboard')
def shelf():
  session_active = auth.verify_session(session)
  if not session_active:
    return redirect(url_for('authentication.login'))
  return render_template('/index/index.html')