from flask import render_template, redirect, url_for, flash, request, session
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.user import User
from .models.socials import PReview
from .models.purchase import Purchase
from .models.fulfillments import Fulfillments


from flask import Blueprint
bp = Blueprint('users', __name__)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class updateForm(FlaskForm):
    ratingInUpdate = SelectField('Rating', choices=['1','2','3','4','5'], validators=[DataRequired()])
    reviewInUpdate = StringField('Review')
    submitUpdate = SubmitField('Update')    

class deleteForm(FlaskForm):
    submitDelete = SubmitField('Delete')
    
class startForm(FlaskForm):
    submitstart = SubmitField('Start Conversation')    


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_auth(form.email.data, form.password.data)
        if user is None:
            flash('Invalid email or password')
            return redirect(url_for('users.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index.index')

        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                       EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.email_exists(email.data):
            raise ValidationError('Already a user with this email.')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.register(form.email.data,
                         form.password.data,
                         form.firstname.data,
                         form.lastname.data,
                         form.address.data):
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index.index'))

class UpdateForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                       EqualTo('password')])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if User.email_exists(email.data):
            raise ValidationError('Already a user with this email.')


@bp.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        if User.update(current_user.id, form.email.data,
                         form.password.data,
                         form.firstname.data,
                         form.lastname.data,
                         form.address.data):
            return redirect(url_for('index.index'))
    return render_template('update.html', title='Update', form=form)

class BalanceForm(FlaskForm):
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add/Subtract')

@bp.route('/balance', methods=['GET', 'POST'])
def balance():
    form = BalanceForm()
    current = None
    if session['seller'] == True:
        if form.validate_on_submit():
            if User.update_sbalance(current_user.id, form.amount.data):
                pass
        current = User.current_sbalance(current_user.id)
    else:
        if form.validate_on_submit():
            if User.update_ubalance(current_user.id, form.amount.data):
                pass
        current = User.current_ubalance(current_user.id)

    return render_template('balance.html', title='Balance', form=form, current=current)

@bp.route('/usermanage')
def user_manage():
    session['seller'] = False
    
    id = current_user.id
    
    recentReviews = PReview.getUserProductReviews(id)
    averageReview = PReview.getAverageU(id)
    numberOfReview = PReview.numberOfReviewU(id)
    numberOfReviewOne = PReview.numberOfReviewOneU(id)
    numberOfReviewTwo = PReview.numberOfReviewTwoU(id)
    numberOfReviewThree = PReview.numberOfReviewThreeU(id)
    numberOfReviewFour = PReview.numberOfReviewFourU(id)
    numberOfReviewFive = PReview.numberOfReviewFiveU(id)

    orders = Purchase.get_all_by_uid(id)

    return render_template('usermanage.html', title='Manage (User)', recentReviews = recentReviews, averageReview = averageReview, numberOfReview = numberOfReview,
                           numberOfReviewOne = numberOfReviewOne, numberOfReviewTwo = numberOfReviewTwo, numberOfReviewThree = numberOfReviewThree,
                           numberOfReviewFour = numberOfReviewFour, numberOfReviewFive = numberOfReviewFive, orders=orders)

@bp.route('/sellermanage', methods=['GET', 'POST'])
def seller_manage():
    session['seller'] = True
    
    id = current_user.id
    
    recentReviews = PReview.getSellerProductReviews(id)
    averageReview = PReview.getAverageS(id)
    numberOfReview = PReview.numberOfReviewS(id)
    numberOfReviewOne = PReview.numberOfReviewOneS(id)
    numberOfReviewTwo = PReview.numberOfReviewTwoS(id)
    numberOfReviewThree = PReview.numberOfReviewThreeS(id)
    numberOfReviewFour = PReview.numberOfReviewFourS(id)
    numberOfReviewFive = PReview.numberOfReviewFiveS(id)
    
    order_fill = Fulfillments.get_orders(id)
    
    return render_template('sellermanage.html', title='Manage (Seller)', recentReviews = recentReviews, averageReview = averageReview, numberOfReview = numberOfReview,
                           numberOfReviewOne = numberOfReviewOne, numberOfReviewTwo = numberOfReviewTwo, numberOfReviewThree = numberOfReviewThree,
                           numberOfReviewFour = numberOfReviewFour, numberOfReviewFive = numberOfReviewFive, order_fill=order_fill)

@bp.route('/userview', methods=['GET', 'POST'])
def user_view():
    req = request.args
    id = req.get("uid")

    # id = current_user.id
    
    recentReviews = PReview.getUserProductReviews(id)
    
    averageReview = PReview.getAverageU(id)
    numberOfReview = PReview.numberOfReviewU(id)
    numberOfReviewOne = PReview.numberOfReviewOneU(id)
    numberOfReviewTwo = PReview.numberOfReviewTwoU(id)
    numberOfReviewThree = PReview.numberOfReviewThreeU(id)
    numberOfReviewFour = PReview.numberOfReviewFourU(id)
    numberOfReviewFive = PReview.numberOfReviewFiveU(id)

    # user = User.get(sid)
    user = User.get(id)
    fullname = user.firstname + ' ' + user.lastname
    email = user.email
    address = user.address
    
    return render_template('userview.html', title='User View', recentReviews = recentReviews, averageReview = averageReview, numberOfReview = numberOfReview, numberOfReviewOne = numberOfReviewOne, numberOfReviewTwo = numberOfReviewTwo, numberOfReviewThree = numberOfReviewThree,
 numberOfReviewFour = numberOfReviewFour, numberOfReviewFive = numberOfReviewFive, fullname=fullname, id=id,
 email=email, address=address)
    
@bp.route('/sellerview', methods=['GET', 'POST'])
def seller_view():
    req = request.args
    id = req.get("sid")
    sForm = startForm()
    
    recentReviews = PReview.getSellerProductReviews(id)
    
    averageReview = PReview.getAverageS(id)
    numberOfReview = PReview.numberOfReviewS(id)
    numberOfReviewOne = PReview.numberOfReviewOneS(id)
    numberOfReviewTwo = PReview.numberOfReviewTwoS(id)
    numberOfReviewThree = PReview.numberOfReviewThreeS(id)
    numberOfReviewFour = PReview.numberOfReviewFourS(id)
    numberOfReviewFive = PReview.numberOfReviewFiveS(id)
    
    if current_user.is_authenticated:
        uid = current_user.id
        exist = PReview.convoExist(id, uid)
    
        if sForm.submitstart.data and sForm.validate():
            
            if not exist:
                cid = PReview.maxcid(id, uid)
                PReview.createConversations(id, uid, cid)
                flash("Conversation Created")
            else:
                flash("Please use your current conversation instead of creating a new one!")  
        
        
    # user = User.get(sid)
    user = User.get(id)
    fullname = user.firstname + ' ' + user.lastname
    
    return render_template('sellerview.html', title='Seller View', recentReviews = recentReviews, averageReview = averageReview, numberOfReview = numberOfReview,
                           numberOfReviewOne = numberOfReviewOne, numberOfReviewTwo = numberOfReviewTwo, numberOfReviewThree = numberOfReviewThree,
                           numberOfReviewFour = numberOfReviewFour, numberOfReviewFive = numberOfReviewFive, fullname=fullname, sid = id,
                           sForm = sForm)

@bp.route('/publicview', methods=['GET', 'POST'])
def public_view():
    req = request.args
    uid = req.get("uid") if req.get("uid") else None
    sid = req.get("sid") if req.get("sid") else None

    # PRODUCT REVIEWS WRITTEN
    recentPReviews = PReview.getUserProductReviews(uid)
    averagePReview = PReview.getAverageU(uid)
    numberOfPReview = PReview.numberOfReviewU(uid)
    numberOfPReviewOne = PReview.numberOfReviewOneU(uid)
    numberOfPReviewTwo = PReview.numberOfReviewTwoU(uid)
    numberOfPReviewThree = PReview.numberOfReviewThreeU(uid)
    numberOfPReviewFour = PReview.numberOfReviewFourU(uid)
    numberOfPReviewFive = PReview.numberOfReviewFiveU(uid)

    # SELLER REVIEWS WRITTEN

    # REVIEWS THAT SELLER HAS RECEIVED

    sForm = startForm()
    
    receivedReviews = PReview.getSellerProductReviews(sid)
    averageReceived = PReview.getAverageS(sid)
    numberOfReceived = PReview.numberOfReviewS(sid)
    numberOfReceivedOne = PReview.numberOfReviewOneS(sid)
    numberOfReceivedTwo = PReview.numberOfReviewTwoS(sid)
    numberOfReceivedThree = PReview.numberOfReviewThreeS(sid)
    numberOfReceivedFour = PReview.numberOfReviewFourS(sid)
    numberOfReceivedFive = PReview.numberOfReviewFiveS(sid)
    
    # CONVERSATIONS BETWEEN USER AND SELLER
    if current_user.is_authenticated:
        uid = current_user.id
        exist = PReview.convoExist(sid, uid)
    
        if sForm.submitstart.data and sForm.validate():
            
            if not exist:
                cid = PReview.maxcid(sid, uid)
                PReview.createConversations(sid, uid, cid)
                flash("Conversation Created")
            else:
                flash("Please use your current conversation instead of creating a new one!") 

    user = User.get(uid)
    user_name = user.firstname + ' ' + user.lastname

    seller, seller_name, seller_email, seller_address = None, None, None, None
    seller = User.get(sid)
    if seller != None:
        seller_name = seller.firstname + ' ' + seller.lastname
        seller_email = user.email
        seller_address = user.address

    # Haven't finished this yet
    return render_template('publicview.html', title='Public View', recentPReviews = recentPReviews, averagePReview = averagePReview, numberOfPReview = numberOfPReview,
                           numberOfPReviewOne = numberOfPReviewOne, numberOfPReviewTwo = numberOfPReviewTwo, numberOfPReviewThree = numberOfPReviewThree,
                           numberOfPReviewFour = numberOfPReviewFour, numberOfPReviewFive = numberOfPReviewFive, user_name=user_name, uid = uid, sid = sid,
                           sForm = sForm, seller_name=seller_name, seller_email=seller_email, seller_address=seller_address)
    
@bp.route('/updatereview', methods = ["GET", "POST"])
def updatereview():
    uForm = updateForm()
    dForm = deleteForm()
    
    req = request.args
    pid = req.get("pid")
    uid = int(req.get("uid"))
    name = req.get("name")
    link = req.get("link")
        
    if uForm.submitUpdate.data and uForm.validate():
        PReview.updateProductReview(uid, pid, uForm.ratingInUpdate.data, uForm.reviewInUpdate.data)
        flash('You have successfully updated a review for this product!')
        
    elif dForm.submitDelete.data and dForm.validate():
        PReview.deletereview(uid, pid)
        flash('You have successfully deleted a review for this product!')
        
   
    return render_template("updatereviewfromuserpage.html", pid=pid, name = name, link = link, uid = uid, uForm = uForm, dForm = dForm)
