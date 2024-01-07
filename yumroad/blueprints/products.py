from flask import Blueprint, render_template ,redirect, request,url_for
from flask_login import current_user , login_required
from yumroad.models import Product
from yumroad.extensions import db 
from yumroad.forms import ProductForm

products = Blueprint('products', __name__)

@products.route('/')
def index():
    all_products = Product.query.all()
    return render_template('products/index.html', products=all_products)

@products.route('/<int:product_id>')
def details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('products/details.html', product=product)

# @products.route('/create', methods=['GET', 'POST'])
# def create():
#     # Using plain old request handling
#     if request.method == 'POST':
#         product = Product(name=request.form['name'], description=request.form['description'])
#         db.session.add(product)
#         db.session.commit()
#         return redirect(url_for('products.details', product_id=product.id))
#     return render_template('products/create.html')

@products.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, description=form.description.data,
                        creator=current_user,
                        price_cents=int(form.price.data*100),
                        picture_url=form.picture_url.data,
                        store=current_user.store)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products.details', product_id=product.id))
    return render_template('products/create.html', form=form)

@products.route('/<product_id>/edit', methods=['GET', 'POST'])
def edit(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm()

    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        db.session.commit()
        return redirect(url_for('products.details', product_id=product.id))

    # Pre-fill the form with existing data
    form.name.data = product.name
    form.description.data = product.description
    return render_template('products/edit.html', form=form, product=product)

@products.errorhandler(404)
def not_found(exception):
    return render_template('products/404.html'), 404


# @product_bp.route('/product/new', methods=['GET', 'POST'])
# @login_required
# def create():
#     form = ProductForm()
#     if form.validate_on_submit():
#         product = Product(name=form.name.data,
#                         description=form.description.data,
#                         price_cents=int(form.price.data*100),
#                         picture_url=form.picture_url.data,
#                         creator=current_user,
#                         store=current_user.store)
#         db.session.add(product)
#         db.session.commit()
#         return redirect(url_for('product.details', product_id=product.id))
#     return render_template('products/new.html', form=form)