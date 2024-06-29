from flask import Flask, redirect, url_for, request, render_template, Response
from source.MediaPipe.Face_Capture import face_capture
from source.LBPH.Face_Recognization import test as face_recognization
import cv2

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/checkin.html')
def checkin():
    return render_template('checkin.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/video_feed/<name>')
def video_feed(name):
    return Response(face_capture.capture(name),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(face_recognization.recognize(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/terms.html')
def terms():
    return render_template('terms.html')

@app.route('/success/<name>')
def success(name):
    return render_template('collecting.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
