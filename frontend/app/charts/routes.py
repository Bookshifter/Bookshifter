from flask import render_template
from app.charts import bp
from flask import current_app

@bp.route('/charts-morris')
def charts_morris():
    return render_template('/charts/charts-morris.html')

@bp.route('/charts-nvd3')
def charts_nvd3():
    return render_template('/charts/charts-nvd3.html')

@bp.route('/charts-rickshaw')
def charts_rickshaw():
    return render_template('/charts/charts-rickshaw.html')

@bp.route('/charts-other')
def charts_other():
    return render_template('/charts/charts-other.html')