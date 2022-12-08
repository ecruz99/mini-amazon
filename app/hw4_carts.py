from flask import render_template, request, session
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, NumberRange
from .models.carts import Cart

from flask import Blueprint
bp = Blueprint('hw4_carts', __name__)

class DeleteFromCartForm(FlaskForm):
    pid_input = StringField('Product ID', validators=[DataRequired()])
    submit = SubmitField('Delete') 

class ChangeItemQuantity(FlaskForm):
    uid_input3 = StringField('User ID', validators=[DataRequired()])
    sid_input3 = StringField('Seller ID', validators=[DataRequired()])
    pid_input3 = StringField('Product ID', validators=[DataRequired()])
    quantity3 = StringField('Quantity', validators=[DataRequired()])
    submit3 = SubmitField('Update Quantity')

@bp.route('/uidcart', methods = ["GET", "POST"])
def uidcart():
    if current_user.is_authenticated:
        uid = current_user.id
        
        cart = Cart.get_cart(uid)

        subtotal = Cart.subtotal(uid)

        num_in_cart = Cart.num_items_in_cart(uid)
        
        deleteform = DeleteFromCartForm()
        
        if deleteform.submit.data and deleteform.validate():
            cart = Cart.delete_cart_item(uid, deleteform.pid_input.data)
            
        return render_template('hw4_carts.html',
                                deleteform=deleteform,
                                cart=cart,
                                num_in_cart=num_in_cart,
                                subtotal=subtotal
                              ) 
    else:
        return render_template('hw4_carts.html')

    
    # render the page by adding information to the index.html file
    

