from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
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