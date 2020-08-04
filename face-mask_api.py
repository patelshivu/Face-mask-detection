from flask import *  
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os

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

@app.route('/')  
def upload():  

    return render_template("demo_1.html")  
'''
@app.route('/upload',methods=['GET','POST'])
def upload_image():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #detect_and_predict_mask(frame, faceNet, maskNet)
        print("Image uploaded")
        #return detect_and_predict_mask(frame, faceNet, maskNet)

        #return "Image uploaded"
        #import pdb;pdb.set_trace()
        #return detect_mask_video(frame, faceNet, maskNet)
        return render_template("success.html", name = file.filename)  '''
@app.route('/mask_detect', methods =['GET','POST'])
def detect_mask():
    print("mask_detect")

    #return "mask detect"
    camera_open()
    return redirect('/')

if __name__ == '__main__':  
    app.run(debug = True)  
