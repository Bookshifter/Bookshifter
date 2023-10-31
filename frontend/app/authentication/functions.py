from flask import flash, redirect, url_for

def verify_session(usr_session):
    if not 'token' in usr_session:
        flash('Você deve estar logado para entrar nessa página!', 'warning')
        return False
    else:
        return True