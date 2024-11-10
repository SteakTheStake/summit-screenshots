import os
from flask import Blueprint, Flask, render_template, redirect
from pathlib import Path

bp = Blueprint('image', __name__, static_folder='static')

@bp.route('/back')
def back_home():
  return redirect('https://summitmc.xyz')

@bp.route('/', methods=['GET'])
def index():
  image_dir = Path('static/images')
  shots = sorted([f.name for f in image_dir.glob('shot*.webp')])
  return render_template('index.html', items=shots)

@bp.app_template_filter('fileexists')
def fileexists_filter(filename):
  try:
      static_path = os.path.join('static', 'images', filename)
      return os.path.isfile(static_path)
  except Exception as e:
      return False