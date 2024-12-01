from flask import request, render_template
from .base import ui_v1


@ui_v1.route("home")
def home():
    return render_template('home2.html', title='Welcome To Our Wedding')