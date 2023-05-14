import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "tarfu"

app.config["SQLALCHEMY_DATABASE_URI"] = 'mariadb+mariadbconnector://mysqluser:K0m84t@127.0.0.1:3306/tooling'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Cabinet_Tooling(db.Model):
    __tablename__ = "cabinet_tooling"
    category = db.Column(db.String(250), nullable=False)
    category_url = db.Column(db.String(50), nullable=False)
    category_image = db.Column(db.String(250))
    sub_category = db.Column(db.String(250), nullable=False)
    sub_category_url = db.Column(db.String(50), nullable=False)
    sub_category_image = db.Column(db.String(250))
    item = db.Column(db.String(250), nullable=False)
    item_url = db.Column(db.String(50), nullable=False)
    item_image = db.Column(db.String(250))
    descript = db.Column(db.String(250))
    location = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    minimum = db.Column(db.Integer, nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    edp = db.Column(db.String(100), primary_key = True, nullable=False)
    vendor = db.Column(db.String(100), nullable=False)
    purchased = db.Column(db.Date, nullable=False)

   



@app.route('/')
def index():
    tooling = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()

    return render_template('index.html', tooling=tooling)


@app.route('/milling')
def milling():
    tooling = Cabinet_Tooling.query.filter_by(category='Milling').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/drills')
def drills():
    tooling = Cabinet_Tooling.query.filter_by(category='Drills').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/inserts')
def inserts():
    tooling = Cabinet_Tooling.query.filter_by(category='Inserts').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/countersinks')
def countersinks():
    tooling = Cabinet_Tooling.query.filter_by(category='Countersinks').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/carbide_id')
def carbide_id():
    tooling = Cabinet_Tooling.query.filter_by(category='Internal Tools').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/taps')
def taps():
    tooling = Cabinet_Tooling.query.filter_by(category='Taps').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/reamers')
def reamers():
    tooling = Cabinet_Tooling.query.filter_by(category='Reamers').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/deburring')
def deburring():
    tooling = Cabinet_Tooling.query.filter_by(category='Deburring/Grinding').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/supplies')
def supplies():
    tooling = Cabinet_Tooling.query.filter_by(category_url='supplies').all()

    return render_template('sub_category.html', tooling=tooling)

@app.route('/tools')
def tools():
    tooling = Cabinet_Tooling.query.filter_by(sub_category='Tools').all()

    return render_template('items.html', tooling=tooling)

@app.route('/collets')
def collets():
    tooling = Cabinet_Tooling.query.filter_by(sub_category='Collets').all()

    return render_template('items.html', tooling=tooling)





if __name__ == '__main__':
    app.run()

