from flask import render_template
from app.tables import bp
from flask import current_app

@bp.route('/table-basic')
def table_basic():
    return render_template('/tables/table-basic.html')

@bp.route('/table-datatables')
def table_datatables():
    return render_template('/tables/table-datatables.html')

@bp.route('/table-export')
def table_export():
    return render_template('/tables/table-export.html')