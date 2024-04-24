from flask import Flask, redirect, url_for, request
from source.MediaPipe.Face_Capture import face_capture

app = Flask(__name__)
 
@app.route('/success/<name>')
def success(name):
    face_capture.capture(name)
    return 'welcome %s' % name
 
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