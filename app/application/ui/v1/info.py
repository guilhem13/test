from flask import request, render_template
from .base import ui_v1


@ui_v1.route("info")
def info():
    return render_template('info.html', title='Welcome To Our Wedding')