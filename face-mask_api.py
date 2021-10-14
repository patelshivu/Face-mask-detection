from flask import *  
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import numpy as np
from detect_mask_video import camera_open
app = Flask(__name__)  

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

# Render Mask detection HTML Templates
@app.route('/')  
def upload():  
    return render_template("demo_1.html") 

# Real time Face mask detection 
@app.route('/mask_detect', methods =['GET','POST'])
def detect_mask():
    print("mask_detect")

    #Function calling real time "mask detect"
    camera_open()
    return redirect('/')

if __name__ == '__main__':  
    app.run(debug = False)  
