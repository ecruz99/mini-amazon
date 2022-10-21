from flask import render_template
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase

from flask import Blueprint
bp = Blueprint('index', __name__)

class UserForm(FlaskForm):
    uid_input = StringField('User ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

@bp.route('/')
def index():
    # get all available products for sale:
    products = Product.get_all(True)
    # find the products current user has bought:
    if current_user.is_authenticated:
        purchases = Purchase.get_all_by_uid_since(
            current_user.id, datetime.datetime(1980, 9, 14, 0, 0, 0))
    else:
        purchases = None

    # find all purchases by given user
    form = UserForm()
    #this isn't working rn for some reason but i'll come back to it
    #purchases_by_user = Purchase.get_all_by_uid(form.uid_input.data)
    purchases_by_user = Purchase.get_all_by_uid(2)

    # render the page by adding information to the index.html file
    return render_template('index.html',
                           avail_products=products,
                           purchase_history=purchases,
                           uid_purchases=purchases_by_user,
                           form=form
                           )
