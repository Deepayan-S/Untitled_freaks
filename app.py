from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class pro(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(500),nullable = False)
    last_name=db.Column(db.String(500),nullable = False)
    email=db.Column(db.String(500),nullable = False)
    passw=db.Column(db.String(8),nullable = False)

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def proj():
    if request.method=="POST":
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        passw=generate_password_hash(request.form['passw'])
        Pro = pro(first_name=first_name,last_name=last_name,email=email,passw=passw)
        db.session.add(Pro)
        db.session.commit()
    allT = pro.query.all()
    print(allT)
    return render_template("login.html",allT=allT)

@app.route('/login/',methods=['POST'])
def login():
    email = request.form['email']
    passw = request.form['passw']
    Pro = pro.query.filter_by(email=email).first()
    if Pro and check_password_hash(Pro.passw, passw):
        return redirect(url_for('joblisting'))
    else:
        return redirect(url_for('proj'))
    
@app.route('/check/')
def check():
    return render_template("af.html")

@app.route('/joblisting')
def joblisting():
    return render_template('jobprofile.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')   




if __name__=="__main__":
    app.run(debug=True)

 

