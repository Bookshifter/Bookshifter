from flask import render_template, redirect, request
from app.pages import bp
from flask import current_app

@bp.route('/pages-gallery')
def pages_gallery():
    return render_template('/pages/pages-gallery.html')

@bp.route('/pages-invoice')
def pages_invoice():
    return render_template('/pages/pages-invoice.html')

@bp.route('/pages-profile')
def pages_profile():
    return render_template('/pages/pages-profile.html')

@bp.route('/pages-address-book')
def pages_address_book():
    return render_template('/pages/pages-address-book.html')

@bp.route('/pages-timeline')
def pages_timeline():
    return render_template('/pages/pages-timeline.html')

@bp.route('/pages-timeline-simple')
def pages_timeline_simple():
    return render_template('/pages/pages-timeline-simple.html')

@bp.route('/pages-mailbox-inbox')
def pages_mailbox_inbox():
    return render_template('/pages/pages-mailbox-inbox.html')

@bp.route('/pages-mailbox-message')
def pages_mailbox_message():
    return render_template('/pages/pages-mailbox-message.html')

@bp.route('/pages-mailbox-compose')
def pages_mailbox_compose():
    return render_template('/pages/pages-mailbox-compose.html')

@bp.route('/pages-calendar')
def pages_calendar():
    return render_template('/pages/pages-calendar.html')

@bp.route('/pages-tasks')
def pages_tasks():
    return render_template('/pages/pages-tasks.html')

@bp.route('/pages-content-table')
def pages_content_table():
    return render_template('/pages/pages-content-table.html')

@bp.route('/pages-faq')
def pages_faq():
    return render_template('/pages/pages-faq.html')

@bp.route('/pages-search')
def pages_search():
    return render_template('/pages/pages-search.html')

@bp.route('/pages-blog-list')
def pages_blog_list():
    return render_template('/pages/pages-blog-list.html')

@bp.route('/pages-blog-post')
def pages_blog_post():
    return render_template('/pages/pages-blog-post.html')

@bp.route('/pages-lock-screen', methods=['GET', 'POST'])
def pages_lock_screen():
    if request.method == 'POST':
        return redirect('/')
    return render_template('/pages/pages-lock-screen.html')

@bp.route('/pages-login')
def pages_login():
    return render_template('/pages/pages-login.html')

@bp.route('/pages-login-v2')
def pages_login_v2():
    return render_template('/pages/pages-login-v2.html')

@bp.route('/pages-login-inside')
def pages_login_inside():
    return render_template('/pages/pages-login-inside.html')

@bp.route('/pages-login-website')
def pages_login_website():
    return render_template('/pages/pages-login-website.html')

@bp.route('/pages-login-website-light')
def pages_login_website_light():
    return render_template('/pages/pages-login-website-light.html')

@bp.route('/pages-registration')
def pages_registration():
    return render_template('/pages/pages-registration.html')

@bp.route('/pages-registration-login')
def pages_registration_login():
    return render_template('/pages/pages-registration-login.html')

@bp.route('/pages-forgot-password')
def pages_forgot_password():
    return render_template('/pages/pages-forgot-password.html')

@bp.route('/pages-error-404')
def pages_error_404():
    return render_template('/pages/pages-error-404.html')

@bp.route('/pages-error-404-2')
def pages_error_404_2():
    return render_template('/pages/pages-error-404-2.html')

@bp.route('/pages-error-500')
def pages_error_500():
    return render_template('/pages/pages-error-500.html')

@bp.route('/maps')
def maps():
    return render_template('/pages/maps.html')

