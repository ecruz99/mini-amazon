from flask import render_template
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase

from flask import Blueprint
bp = Blueprint('hw4_product', __name__)

class FilterForm(FlaskForm):
    k_input = StringField('Filter Top Products')
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    cat_input = SelectField('Filter By Category', choices=['accessories', 'books', 'clothes', 'decor', 'electronics', 'food', 'games', 'shoes'])
    submit2 = SubmitField('Submit')

@bp.route('/products', methods = ["GET", "POST"])
def products():
    form = FilterForm()
    form2 = CategoryForm()
    if form.submit.data and form.validate_on_submit():
        top_k_products = Product.get_top_k(form.k_input.data)
        return render_template('products_category.html',
                        products=top_k_products,
                        form=form,
                        form2=form2,
                        cat="in any category"
                        )
    elif form2.submit2.data and form2.validate_on_submit():
        cat = form2.cat_input.data
        cat_products = Product.get_by_cat(cat)
        return render_template('products_category.html',
                        products=cat_products,
                        form=form,
                        form2=form2,
                        cat="in " + cat
                        )
    else:
        products = Product.get_all(True)
        return render_template('products_category.html',
                        products=products,
                        form=form,
                        form2=form2,
                        cat="in any category"
                        )