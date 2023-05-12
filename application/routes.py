import json

from flask import render_template,request,url_for
from rembg import remove
from PIL import Image
import os
from application import app


@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/two')
# def home2():
#     return render_template('home.html')
@app.route('/upload',methods = ['POST'])
def upload():
    try:
        os.remove('application/static/temp_uploaded_image/output.webp')
    except:
        pass
    file = request.files['file']
    file_path = f'application/static/temp_uploaded_image/{file.filename}'
    file.save(file_path)
    input_file = Image.open(file_path)
    output = remove(input_file)
    output.save(f'application/static/temp_uploaded_image/output.webp')
    os.remove((file_path))
    image_url = url_for('static', filename = 'temp_uploaded_image/output.webp')
    with app.test_request_context():
        url = url_for('static', filename='temp_uploaded_image/output.webp')
        # return  ("{{ url_for('static',filename='temp_uploaded_image/output.png') }}")
    # return "application/static/temp_uploaded_image/output.png"
    return url



