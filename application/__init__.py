from flask import  Flask
import os

app = Flask(__name__)

cwd = os.getcwd()

temp_upload_folder = os.path.join(cwd,'application/static/temp_uploaded_image')
app.config['UPLOAD_FOLDER'] = temp_upload_folder

from application import  routes
