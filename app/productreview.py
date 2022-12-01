from flask import render_template, request, flash, redirect
from flask_login import current_user
from werkzeug.urls import url_parse
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.product import Product
from .models.purchase import Purchase
from .models.socials import PReview
from .models.user import User

from flask import Blueprint
bp = Blueprint('productreview', __name__)

class createForm(FlaskForm):
    ratingInCreate = SelectField('Rating', choices=['1','2','3','4','5'])
    submitCreate = SubmitField('Submit')
    
class updateForm(FlaskForm):
    ratingInUpdate = SelectField('Rating', choices=['1','2','3','4','5'])
    submitUpdate = SubmitField('Update')    

class deleteForm(FlaskForm):
    submitDelete = SubmitField('Delete')

@bp.route('/productreview', methods = ["GET", "POST"])
def productreview():
    cForm = createForm()
    uForm = updateForm()
    dForm = deleteForm()
    
    req = request.args
    pid = req.get("pid")
    name = req.get("name")
    link = req.get("link")
    uid = req.get("uid")
    cat= req.get("cat")
    price = req.get("price")
    avail = req.get("avail")
    
    orderExist = PReview.orderExist(uid, pid)
    reviewExist = PReview.reviewexist(uid, pid)
    
    
    if cForm.submitCreate.data and cForm.validate():
        if PReview.createProductReview(uid, pid, cForm.ratingInCreate.data):
            flash('You have successfully added a review for this product!')
            return redirect("productreviews.html", pid=pid, uid = uid, name = name, link = link, cat = cat, price = price, avail = avail, orderExist = orderExist, reviewExist = reviewExist, cForm = cForm, uForm = uForm, dForm = dForm)
        
        return render_template("productreviews.html", pid=pid, uid = uid, name = name, link = link, cat = cat, price = price, avail = avail, orderExist = orderExist, reviewExist = reviewExist, cForm = cForm, uForm = uForm, dForm = dForm)
    elif uForm.submitUpdate.data and uForm.validate():
        if PReview.updateProductReview(uid, pid, uForm.ratingInUpdate.data):
            flash('You have successfully updated a review for this product!')
        
        return render_template("productreviews.html", pid=pid,  uid = uid, name = name, link = link, cat = cat, price = price, avail = avail, orderExist = orderExist, reviewExist = reviewExist, cForm = cForm, uForm = uForm, dForm = dForm)
    elif dForm.submitDelete.data and dForm.validate():
        if PReview.deletereview(uid, pid):
            flash('You have successfully deleted a review for this product!')
        
        return render_template("productreviews.html", pid=pid,  uid = uid, name = name, link = link, cat = cat, price = price, avail = avail, orderExist = orderExist, reviewExist = reviewExist, cForm = cForm, uForm = uForm, dForm = dForm)
    
    
    return render_template("productreviews.html", pid=pid,  uid = uid, name = name, link = link, cat = cat, price = price, avail = avail, orderExist = orderExist, reviewExist = reviewExist, cForm = cForm, uForm = uForm, dForm = dForm)