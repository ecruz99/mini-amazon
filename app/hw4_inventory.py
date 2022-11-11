from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from .models.inventory import Inventory
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask import Blueprint

bp = Blueprint('hw4_inventory', __name__)

class InventoryForm(FlaskForm):
    sid_input = StringField('Seller ID')
    submit = SubmitField('Submit')
    
class delete_invForm(FlaskForm):
    sid_input2 = StringField('Seller ID', validators=[DataRequired()])
    pid_input2 = StringField('Product ID', validators=[DataRequired()])
    submit2 = SubmitField('Delete')
    
class add_invForm(FlaskForm):
    sid_input3 = StringField('Seller ID', validators=[DataRequired()])
    pid_input3 = StringField('Product ID', validators=[DataRequired()])
    productname3 = StringField('Product Name', validators=[DataRequired()])
    quantity3 = StringField('Quantity', validators=[DataRequired()])
    submit3 = SubmitField('Add')

@bp.route('/sidinventory', methods = ["GET", "POST"])
def sidinventory():
    form = InventoryForm()
    form2 = delete_invForm()
    form3 = add_invForm()
    
    
     # render the page by adding information to the index.html file
    if form.submit.data and form.validate():
        seller_inventory = Inventory.get_seller(form.sid_input.data)
        
        return render_template('hw4_inventory.html',
                           sid_inventory=seller_inventory,
                           form=form,
                           form2=form2,
                           form3 = form3
                           )
    elif form2.submit2.data and form2.validate():
        Inventory.delete_inventory(form2.sid_input2.data, form2.pid_input2.data)
        
        return render_template('hw4_inventory.html',
                    form=form,
                    form2=form2,
                    form3=form3
                    )
    elif form3.submit3.data and form3.validate():
        Inventory.add_inventory(form3.sid_input3.data, form3.pid_input3.data, form3.productname3.data, form3.quantity3.data)
        return render_template('hw4_inventory.html',
                    form=form,
                    form2=form2,
                    form3=form3
                    )
    else:
        return render_template('hw4_inventory.html',
                    form=form,
                    form2=form2,
                    form3=form3
                    )  
    