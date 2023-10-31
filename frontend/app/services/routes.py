from flask import render_template
from app.services import bp
from flask import current_app


@bp.route('/services/<asn>/<ix>')
def services(asn, ix):
    return render_template('/services/services-api.html')

@bp.route('/services')
def services_mock():
    
    return render_template('/services/services.html')