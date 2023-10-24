from flask import render_template
from app.ui import bp
from flask import current_app

@bp.route('/icons')
def icons():
    return render_template('/ui/ui-icons.html')

@bp.route('/widgets')
def widgets():
    return render_template('/ui/ui-widgets.html')

@bp.route('/elements')
def elements():
    return render_template('/ui/ui-elements.html')

@bp.route('/buttons')
def buttons():
    return render_template('/ui/ui-buttons.html')

@bp.route('/panels')
def panels():
    return render_template('/ui/ui-panels.html')

@bp.route('/typography')
def typography():
    return render_template('/ui/ui-typography.html')

@bp.route('/portlet')
def portlet():
    return render_template('/ui/ui-portlet.html')

@bp.route('/alerts-popups')
def alerts_popups():
    return render_template('/ui/ui-alerts-popups.html')

@bp.route('/sliders')
def sliders():
    return render_template('/ui/ui-sliders.html')

@bp.route('/lists')
def lists():
    return render_template('/ui/ui-lists.html')

@bp.route('/tour')
def tour():
    return render_template('/ui/ui-tour.html')

@bp.route('/nestable')
def nestable():
    return render_template('/ui/ui-nestable.html')

@bp.route('/autocomplete')
def autocomplete():
    return render_template('/ui/ui-autocomplete.html')

@bp.route('/slide-menu')
def slide_menu():
    return render_template('/ui/ui-slide-menu.html')

