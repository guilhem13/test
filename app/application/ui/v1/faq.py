from flask import request, render_template
from .base import ui_v1


@ui_v1.route("faq")
def faq():
    return render_template('faq.html', title='Welcome To Our Wedding')