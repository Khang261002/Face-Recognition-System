from flask import Flask, redirect, url_for, request, render_template, Response, jsonify
from source.MediaPipe.Face_Capture import face_capture
from source.FaceRecognition.Face_Recognize import face_recognize
import json
import os

app = Flask(__name__)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

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
    return Response(face_recognize.recognize(),
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

@app.route('/update_streaming_status', methods=['POST'])
def update_streaming_status():
    data = request.json
    if 'stopped' in data:
        # Update streaming_data.json file with the new stopped value
        with open(os.path.join(__location__, 'static/json/streaming_data.json'), 'r+') as file:
            json_data = json.load(file)
            json_data['stopped'] = data['stopped']
            file.seek(0)
            json.dump(json_data, file)
            file.truncate()
        return jsonify({'status': 'success', 'stopped': data['stopped']})
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
