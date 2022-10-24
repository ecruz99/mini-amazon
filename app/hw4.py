from flask import render_template
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase

from flask import Blueprint
bp = Blueprint('hw4', __name__)

class UserForm(FlaskForm):
    uid_input = StringField('User ID')
    submit = SubmitField('Submit')

@bp.route('/uidpurch', methods = ["GET", "POST"])
def uidpurch():
    form = UserForm()
    if form.validate_on_submit():
        purchases_by_user = Purchase.get_all_by_uid(form.uid_input.data)
        return render_template('hw4.html',
                           uid_purchases=purchases_by_user,
                           form=form
                           )
    # purchases_by_user = Purchase.get_all_by_uid(2)

    # render the page by adding information to the index.html file
    purchases_by_user = Purchase.get_all_by_uid(form.uid_input.data)
    return render_template('hw4.html',
                           uid_purchases=purchases_by_user,
                           form=form
                           )
