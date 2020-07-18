from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sam123@localhost/Crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(80), unique=False)
    phone = db.Column(db.Integer, unique=False)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


@app.route('/')
def index():
    alldata = Data.query.all()
    return render_template("index.html", alldata=alldata)



@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    alldata = Data.query.get(id)
    db.session.delete(alldata)
    db.session.commit()
    flash("Deleted")
    return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        mydata = Data.query.get(request.form.get('id'))
        mydata.name=request.form['name']
        mydata.email=request.form['email']
        mydata.phone=request.form['phone']
        db.session.commit()
        flash("Updated Successfully")
        return redirect(url_for('index'))





@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        mydata = Data(name, email, phone)
        db.session.add(mydata)
        db.session.commit()
        flash("Added Successfully")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
