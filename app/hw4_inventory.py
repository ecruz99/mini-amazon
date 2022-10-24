from flask import render_template
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase
from .models.inventory import Inventory

from flask import Blueprint
bp = Blueprint('hw4_inventory', __name__)

class InventoryForm(FlaskForm):
    sid_input = StringField('Seller ID')
    submit = SubmitField('Submit')

@bp.route('/sidinventory', methods = ["GET", "POST"])
def sidinventory():
    form = InventoryForm()
    
    # render the page by adding information to the index.html file
    seller_inventory = Inventory.get_seller(form.sid_input.data)
    return render_template('hw4_inventory.html',
                           sid_inventory=seller_inventory,
                           form=form
                           )