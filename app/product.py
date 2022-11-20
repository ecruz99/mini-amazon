from flask import render_template, request
from flask_login import current_user
from werkzeug.urls import url_parse
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase

from flask import Blueprint
bp = Blueprint('product', __name__)


@bp.route('/product', methods = ["GET", "POST"])
def product():
    req = request.args
    cat= req.get("cat")
    name = req.get("name")
    price = req.get("price")
    avail = req.get("avail")
    link = req.get("link")
    return render_template("product.html", name=name, cat=cat, price=price, avail=avail, link=link)