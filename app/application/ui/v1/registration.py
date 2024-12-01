from flask import request, render_template
from .base import ui_v1


@ui_v1.route("registration")
def registration():
    return render_template('registration.html', title='Welcome To Our Wedding')