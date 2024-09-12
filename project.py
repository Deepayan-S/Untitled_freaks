from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
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
        passw=request.form['passw']
        Pro = pro(first_name=first_name,last_name=last_name,email=email,passw=passw)
        db.session.add(Pro)
        db.session.commit()
    allT = pro.query.all()
    print(allT)
    return render_template("login.html",allT=allT)


if __name__=="__main__":
    app.run(debug=True)

 

