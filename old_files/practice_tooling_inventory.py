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
def inserts():
    tooling = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()

    return render_template('inserts.html', tooling=tooling)

@app.route('/<cat_url>')
def new_route(cat_url):
    tooling = Cabinet_Tooling.query.filter_by(category_url=cat_url).all()
    
    return render_template('sub_category.html', tooling=tooling)




if __name__ == '__main__':
    app.run()

