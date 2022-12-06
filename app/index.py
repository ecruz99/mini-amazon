from flask import render_template, session
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase
from .models.socials import PReview

from flask import Blueprint
bp = Blueprint('index', __name__)

class FilterForm(FlaskForm):
    k_input = k_input = RadioField('Sort Price', choices=['high to low', 'low to high'])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    cat_input = SelectField('Filter By Category', choices=['accessories', 'books', 'clothes', 'decor', 'electronics', 'food', 'games', 'shoes'])
    submit2 = SubmitField('Submit')

class KeyWordForm(FlaskForm):
    kw_input = StringField('Search By Keyword')
    submit3 = SubmitField('Search')

@bp.route('/', methods = ["GET", "POST"])
def index():
    # get all available products for sale:
    form = FilterForm()
    form2 = CategoryForm()
    form3 = KeyWordForm()

    
    # find the products current user has bought:
    if current_user.is_authenticated:
        purchases = Purchase.get_all_by_uid_since(
            current_user.id, datetime.datetime(1980, 9, 14, 0, 0, 0))
    else:
        purchases = None

    if form.submit.data and form.validate_on_submit():
        if form.k_input.data == "high to low":
            top_k_products = Product.order_d()[:50]
        else:
            top_k_products = Product.order_a()[:50]

        ratings = []
        for p in top_k_products:
            ratings.append(PReview.getAverage(p.id))

        length = len(top_k_products)

        return render_template('index.html',
                        products=top_k_products,
                        ratings=ratings,
                        length=length,
                        form=form,
                        form2=form2,
                        form3=form3,
                        purchases=purchases,
                        cat="in any category"
                        )
    elif form2.submit2.data and form2.validate_on_submit():
        cat = form2.cat_input.data
        cat_products = Product.get_by_cat(cat)

        ratings = []
        for p in cat_products:
            ratings.append(PReview.getAverage(p.id))

        length = len(cat_products)

        return render_template('index.html',
                        products=cat_products,
                        ratings=ratings,
                        length=length,
                        form=form,
                        form2=form2,
                        form3=form3,
                        purchases=purchases,
                        cat="in " + cat
                        )
    elif form3.submit3.data and form3.validate_on_submit():
        kw = form3.kw_input.data
        kw_products = Product.get_by_kw(kw)

        ratings = []
        for p in kw_products:
            ratings.append(PReview.getAverage(p.id))

        length = len(kw_products)

        return render_template('index.html',
                        products=kw_products,
                        ratings=ratings,
                        length=length,
                        form=form,
                        form2=form2,
                        form3=form3,
                        purchases=purchases,
                        cat="in any category"
                        )
    else:
        products = Product.get_all(True)[0:15]
    
        ratings = []
        for p in products:
            ratings.append(PReview.getAverage(p.id))
        
        length = len(products)

        return render_template('index.html',
                        products=products,
                        ratings=ratings,
                        length=length,
                        form=form,
                        form2=form2,
                        form3=form3,
                        purchases=purchases,
                        cat="in any category"
                        )

