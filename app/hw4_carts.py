from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from .models.carts import Cart

from flask import Blueprint
bp = Blueprint('hw4_carts', __name__)

class CartsForm(FlaskForm):
    uid_input = StringField('User ID')
    submit = SubmitField('Submit')

class DeleteFromCartForm(FlaskForm):
    uid_input2 = StringField('User ID', validators=[DataRequired()])
    sid_input2 = StringField('Seller ID', validators=[DataRequired()])
    pid_input2 = StringField('Product ID', validators=[DataRequired()])
    submit2 = SubmitField('Delete') 


@bp.route('/uidcart', methods = ["GET", "POST"])
def uidcart():
    form = CartsForm()
    form2 = DeleteFromCartForm()

    if form.submit.data and form.validate():
        user_cart = Cart.get_cart(form.uid_input.data)
        return render_template('hw4_carts.html',
                        cart=user_cart,
                        form=form,
                        form2=form2
                        )
    elif form2.submit2.data and form2.validate():
        Cart.delete_cart_item(form2.uid_input2.data, form2.sid_input2.data, form2.pid_input2.data)

        return render_template('hw4_carts.html',
                    form=form,
                    form2=form2
                    )
    else:
        return render_template('hw4_carts.html',
                    form=form,
                    form2=form2
                    ) 

    
    # render the page by adding information to the index.html file
    

