from .v1 import ui_v1
from app.application.http.response import Response

def register_ui(app):
    app.register_blueprint(ui_v1, url_prefix="/ui")

    @app.errorhandler(404)
    def page_not_found(e):
        return Response().notfound()