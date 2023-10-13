from flask import render_template
from app.tables import bp
from flask import current_app

@bp.route('/form-elements')
def form_elements():
    return render_template('/forms/form-elements.html')

@bp.route('/form-validation')
def form_validation():
    return render_template('/forms/form-validation.html')

@bp.route('/form-wizards')
def form_wizards():
    return render_template('/forms/form-wizards.html')

@bp.route('/form-editors')
def form_editors():
    return render_template('/forms/form-editors.html')

@bp.route('/form-layouts-one-column')
def form_layouts_one_column():
    return render_template('/forms/form-layouts-one-column.html')

@bp.route('/form-layouts-two-column')
def form_layouts_two_column():
    return render_template('/forms/form-layouts-two-column.html')

@bp.route('/form-layouts-tabbed')
def form_layouts_tabbed():
    return render_template('/forms/form-layouts-tabbed.html')

@bp.route('/form-file-handling')
def form_file_handling():
    return render_template('/forms/form-file-handling.html')

@bp.route('/form-layouts-separated')
def form_layouts_separated():
    return render_template('/forms/form-layouts-separated.html')