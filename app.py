from flask import Flask , render_template
app=Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/joblisting/')
def joblisting():
    return render_template('Jobprofile.html')

@app.route('/profile/')
def profile():
    return render_template('profile.html')