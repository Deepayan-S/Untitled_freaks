from flask import Flask , render_template ,url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'
db = SQLAlchemy(app)

class userInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userFirstName = db.Column(db.String(1000), nullable=False)
    userLastName = db.Column(db.String(1000), nullable=False)
    userPassword = db.Column(db.String(1000), nullable=False)
    userEmail = db.Column(db.String(1000), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/',methods =['GET','POST'])
def login():
    if request.method=='POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        UserInfo = userInfo(firstName=firstName,lastName=lastName,email=email,password=password)
        try:   
            db.session.add(UserInfo)
            db.session.commit()
        except:
            return 'Error while logging'
    else:
        return render_template('login.html')

@app.route('/joblisting/')
def joblisting():
    return render_template('Jobprofile.html')

@app.route('/profile/')
def profile():
    return render_template('profile.html')

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)