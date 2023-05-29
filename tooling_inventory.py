import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update, insert
from sqlalchemy.orm import Session
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

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
    item_image = db.Column(db.String(250))
    descript = db.Column(db.String(250))
    location = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    minimum = db.Column(db.Integer, nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    edp = db.Column(db.String(100), primary_key = True, nullable=False)
    vendor = db.Column(db.String(100), nullable=False)
    purchased = db.Column(db.Date, nullable=False)
    

@auth.verify_password
def verify_password(username, password):
    user = 'sifu'
    pw = '800g3r'
    users = {
        user: generate_password_hash(pw)
    }
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
def index():
    tooling = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()
    nav_bar = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()

    return render_template('index.html', nav_bar=nav_bar, tooling=tooling)

@app.route('/<cat_url>')
def category_url(cat_url):
    tooling = Cabinet_Tooling.query.filter_by(category_url=cat_url).order_by(Cabinet_Tooling.category).all()
    nav_bar = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()

    return render_template('category.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/cat/<sub_cat_url>')
def sub_category_url(sub_cat_url):
    tooling = Cabinet_Tooling.query.filter_by(sub_category_url=sub_cat_url).order_by(Cabinet_Tooling.sub_category).all()
    nav_bar = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()

    return render_template('sub_category.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/sub/<ind_item>')
def items_url(ind_item):
    tooling = Cabinet_Tooling.query.filter_by(edp=ind_item).order_by(Cabinet_Tooling.edp).all()
    nav_bar = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()
    
    return render_template('items.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/item/<product_code>', methods=['POST'])
def remove_item(product_code):
    product = Cabinet_Tooling.query.get(product_code)
    if product.quantity > 0:
        new_quantity = product.quantity - 1
        product.quantity = new_quantity
        db.session.commit()

    tooling = Cabinet_Tooling.query.filter_by(edp=product_code).order_by(Cabinet_Tooling.edp).all()
    nav_bar = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()

    return render_template('items.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/add/update>', methods=['POST'])
def add_item():
    product_code = request.args.get('product_code')
    product_quantity = int(request.form.get('quantity'))
    if product_quantity > 0:
        product = Cabinet_Tooling.query.get(product_code)
        new_quantity = product.quantity + product_quantity
        product.quantity = new_quantity
        db.session.commit()

    tooling = Cabinet_Tooling.query.filter_by(edp=product_code).order_by(Cabinet_Tooling.edp).all()
    nav_bar = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()

    return render_template('items.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/prod/<product_code>')
@auth.login_required
def admin(product_code):
    tooling = Cabinet_Tooling.query.filter_by(edp=product_code).order_by(Cabinet_Tooling.edp).all()
    nav_bar = Cabinet_Tooling.query.order_by(Cabinet_Tooling.category).all()
    
    return render_template('update_item.html', nav_bar=nav_bar, tooling=tooling)




if __name__ == '__main__':
    app.run()

