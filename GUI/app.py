from flask import Flask, redirect, url_for, request, render_template
# from source.MediaPipe.Face_Capture import face_capture

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

@app.route('/success/<name>')
def success(name):
    # face_capture.capture(name)
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