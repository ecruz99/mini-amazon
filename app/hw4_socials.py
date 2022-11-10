from flask import flash, render_template
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.socials import PReview

from flask import Blueprint
bp = Blueprint('hw4_socials', __name__)

class SocialForm(FlaskForm):
    uidInput = StringField('UID', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class updateForm(FlaskForm):
    uidInput1 = StringField('UID', validators=[DataRequired()])
    pidInput1 = StringField('PID', validators=[DataRequired()])
    ratingInput1 = StringField('Rating', validators=[DataRequired()])
    submit1 = SubmitField('Update')
    
class createForm(FlaskForm):
    uidInput2 = StringField('UID', validators=[DataRequired()])
    pidInput2 = StringField('PID', validators=[DataRequired()])
    ratingInput2 = StringField('Rating', validators=[DataRequired()])
    submit2 = SubmitField('Create')   
    
    def reviewexist(uidInput2, pidInput2):
        if PReview.reviewexist(uidInput2.data, pidInput2.data):
            raise ValidationError('Already a Review for this product')     
        
class deleteForm(FlaskForm):
    uidInput3 = StringField('UID', validators=[DataRequired()])
    pidInput3 = StringField('PID', validators=[DataRequired()])
    submit3 = SubmitField('Delete')       

@bp.route('/rr', methods = ["GET", "POST"])
def rr():
    form = SocialForm()
    form1 = updateForm()
    form2 = createForm()
    form3 = deleteForm()
    
    if form.submit.data and form.validate():
        recentFiveReviews = PReview.getUserProductReviews(form.uidInput.data)
        
        return render_template('hw4_socials.html',
                    resultReviews=recentFiveReviews,
                    form=form,
                    form1=form1,
                    form2=form2,
                    form3 = form3
                    )
    elif form1.submit1.data and form1.validate():
        PReview.updateProductReview(form1.uidInput1.data, form1.pidInput1.data, form1.ratingInput1.data)
        
        return render_template('hw4_socials.html',
                    form=form,
                    form1=form1,
                    form2=form2,
                    form3 = form3
                    )
    elif form2.submit2.data and form2.validate():  
        if form2.validate_on_submit: 
            if PReview.createProductReview(form2.uidInput2.data, form2.pidInput2.data, form2.ratingInput2.data):
                flash('Review Created')
        
        return render_template('hw4_socials.html',
                    form=form,
                    form1=form1,
                    form2=form2,
                    form3 = form3
                    ) 
    elif form3.submit3.data and form3.validate():
        PReview.deletereview(form3.uidInput3.data, form3.pidInput3.data)
        
        return render_template('hw4_socials.html',
                    form=form,
                    form1=form1,
                    form2=form2,
                    form3 = form3
                    )
    else:
        return render_template('hw4_socials.html',
                    form=form,
                    form1=form1,
                    form2=form2,
                    form3 = form3
                    )     
    