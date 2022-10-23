from flask import render_template
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase

from flask import Blueprint
bp = Blueprint('hw4_product', __name__)

class FilterForm(FlaskForm):
    k_input = StringField('Filter Top Products')
    submit = SubmitField('Submit')

@bp.route('/topk', methods = ["GET", "POST"])
def topk():
    form = FilterForm()
    if form.validate_on_submit():
        top_k_products = Product.get_top_k(form.k_input.data)
        return render_template('hw4_product.html',
                        k_products=top_k_products,
                        form=form
                        )
    top_k_products = Product.get_top_k(form.k_input.data)
    return render_template('hw4_product.html',
                        k_products=top_k_products,
                        form=form
                        )

    # render the page by adding information to the index.html file