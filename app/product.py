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
    
    id = req.get("id")
    
    products = Product.get_by_cat(cat)[:10]
    
    recentReviews = PReview.getAProductReviews(id)
    
    averageReview = PReview.getAverage(id)
    numberOfReview = PReview.numberOfReview(id)
    numberOfReviewOne = PReview.numberOfReviewOne(id)
    numberOfReviewTwo = PReview.numberOfReviewTwo(id)
    numberOfReviewThree = PReview.numberOfReviewThree(id)
    numberOfReviewFour = PReview.numberOfReviewFour(id)
    numberOfReviewFive = PReview.numberOfReviewFive(id)
    
    return render_template("product.html", name=name, cat=cat, price=price, avail=avail, link=link, products=products,
                           pid = id, recentReviews = recentReviews, averageReview = averageReview, numberOfReview = numberOfReview,
                           numberOfReviewOne = numberOfReviewOne, numberOfReviewTwo = numberOfReviewTwo, numberOfReviewThree = numberOfReviewThree,
                           numberOfReviewFour = numberOfReviewFour, numberOfReviewFive = numberOfReviewFive)