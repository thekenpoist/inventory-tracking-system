import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv()

auth = HTTPBasicAuth()
app = Flask(__name__)
app.secret_key = "tarfu"

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class CabinetTooling(db.Model):
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
    # Verify the admin username and password for table inserts and updates
    user = os.getenv('ADMIN_USERNAME')
    password = os.getenv('ADMIN_PASSWORD')
    users = {
        user: generate_password_hash(password)
    }
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
def index():
    # Render home page - route to index.html
    tooling = CabinetTooling.query.order_by(CabinetTooling.category).all()
    nav_bar = CabinetTooling.query.order_by(CabinetTooling.category).all()
    return render_template('index.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/category/<cat_url>')
def category_url(cat_url):
    # Render category page - route to category.html
    if cat_url.endswith(('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
        return "Resource not found", 404
    # print(f"category_url route accessed with cat_url: {cat_url}")
    tooling = CabinetTooling.query.filter_by(category_url=cat_url).order_by(CabinetTooling.category).all()
    nav_bar = CabinetTooling.query.order_by(CabinetTooling.category).all()
    return render_template('category.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/cat/<sub_cat_url>')
def sub_category_url(sub_cat_url):
    # Render sub category page - route to sub_category.html
    if sub_cat_url.endswith(('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
        return "Resource not found", 404
    # print(f"sub_category_url route accessed with sub_cat_url: {sub_cat_url}")
    tooling = CabinetTooling.query.filter_by(sub_category_url=sub_cat_url).order_by(CabinetTooling.sub_category).all()
    nav_bar = CabinetTooling.query.order_by(CabinetTooling.category).all()
    return render_template('sub_category.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/sub/<ind_item>')
def items_url(ind_item):
    # Render item page - route to items.html
    if ind_item.endswith(('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
        return "Resource not found", 404
    # print(f"items_url route accessed with ind_item: {ind_item}")
    tooling = CabinetTooling.query.filter_by(edp=ind_item).order_by(CabinetTooling.edp).all()
    nav_bar = CabinetTooling.query.order_by(CabinetTooling.category).all()
    return render_template('items.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/item/<product_code>', methods=['POST'])
def remove_item(product_code):
    # Remove an item from inventory and route back to items.html
    # print(f"remove item route accessed with product code: {product_code}")
    product = db.session.get(CabinetTooling, product_code)
    if product.quantity > 0:
        new_quantity = product.quantity - 1
        product.quantity = new_quantity
        db.session.commit()
    tooling = CabinetTooling.query.filter_by(edp=product_code).order_by(CabinetTooling.edp).all()
    nav_bar = CabinetTooling.query.order_by(CabinetTooling.category).all()
    return render_template('items.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/add/<update>', methods=['POST'])
def add_item():
    # Update item quantity and route back to items.html
    product_code = request.args.get('product_code')
    product_quantity = int(request.form.get('quantity'))
    if product_quantity > 0:
        product = db.session.get(CabinetTooling, product_code)
        new_quantity = product.quantity + product_quantity
        product.quantity = new_quantity
        db.session.commit()

    tooling = CabinetTooling.query.filter_by(edp=product_code).order_by(CabinetTooling.edp).all()
    nav_bar = CabinetTooling.query.order_by(CabinetTooling.category).all()
    return render_template('items.html', nav_bar=nav_bar, tooling=tooling)


@app.route('/prod/<product_code>')
@auth.login_required
def admin(product_code):
    # Render admin page to update item quantity - route to update_item.html
    if product_code.endswith(('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
        return "Resource not found", 404
    # print(f"admin route accessed with product code: {product_code}")
    tooling = CabinetTooling.query.filter_by(edp=product_code).order_by(CabinetTooling.edp).all()
    nav_bar = CabinetTooling.query.order_by(CabinetTooling.category).all()
    return render_template('update_item.html', nav_bar=nav_bar, tooling=tooling)


#@app.route('/new_product>', methods=['POST'])
#@auth.login_required
#def new_product():



if __name__ == '__main__':
    app.run()


