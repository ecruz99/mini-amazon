from flask import render_template, request
from flask_login import current_user
from werkzeug.urls import url_parse
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase
from .models.socials import PReview
from .models.user import User

from flask import Blueprint
bp = Blueprint('product', __name__)


@bp.route('/product', methods = ["GET", "POST"])
def product():
    req = request.args
    id = req.get("id")
    product = Product.get(id)

    cat = product.category
    name = product.name
    price = product.price
    avail = product.available
    link = product.link
    descr = product.descr

    
    user = User.get(id)
    sid = user.id
    sellername = user.firstname + ' ' + user.lastname
    
    products = Product.get_by_cat(cat)[:10]
    
    recentReviews = PReview.getAProductReviews(id)
    recentReviewLinks = PReview.getAPReviewLinks(id)
    
    averageReview = PReview.getAverage(id)
    numberOfReview = PReview.numberOfReview(id)
    numberOfReviewOne = PReview.numberOfReviewOne(id)
    numberOfReviewTwo = PReview.numberOfReviewTwo(id)
    numberOfReviewThree = PReview.numberOfReviewThree(id)
    numberOfReviewFour = PReview.numberOfReviewFour(id)
    numberOfReviewFive = PReview.numberOfReviewFive(id)
    
    return render_template("product.html", name=name, descr=descr, cat=cat, price=price, avail=avail, link=link, products=products, user = user,
                           pid = id, recentReviews = recentReviews, averageReview = averageReview, numberOfReview = numberOfReview,
                           numberOfReviewOne = numberOfReviewOne, numberOfReviewTwo = numberOfReviewTwo, numberOfReviewThree = numberOfReviewThree,
                           numberOfReviewFour = numberOfReviewFour, numberOfReviewFive = numberOfReviewFive, recentReviewLinks = recentReviewLinks,
                           sellername=sellername, sid=sid, )