from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from .models.carts import Cart

from flask import Blueprint
bp = Blueprint('hw4_carts', __name__)

class CartsForm(FlaskForm):
    uid_input = StringField('User ID')
    submit = SubmitField('Submit')

@bp.route('/uidcart', methods = ["GET", "POST"])
def uidcart():
    form = CartsForm()
    
    # render the page by adding information to the index.html file
    user_cart = Cart.get_cart(form.uid_input.data)
    return render_template('hw4_carts.html',
                           cart=user_cart,
                           form=form
                           )

