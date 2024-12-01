"""
__init_.py
- creates a Flask app instance
"""
import os
from dotenv import load_dotenv
load_dotenv()

from app.infrastructure.persistence.sqlalchemy.models import auto_create_table
from app.application.api import register_api
from app.application.ui import register_ui
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from distutils.util import strtobool


def create_app(app_name='Wedding_App'):

  """ 
    Instance app flask
  """
  app = Flask(app_name, template_folder='app/application/ui/templates', static_folder="app/application/ui/static")
  app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
  app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


  """"
    CORS application for api endpoint
    with orgin any
  """
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  
  """ 
    Instance app database model  
  """
  auto_create_table()

  """
    Register liste api
  """
  register_api(app)

  register_ui(app)

  return app
