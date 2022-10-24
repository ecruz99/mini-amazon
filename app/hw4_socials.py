from flask import render_template
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.socials import PReview

from flask import Blueprint
bp = Blueprint('hw4_socials', __name__)

class SocialForm(FlaskForm):
    uidInput = StringField('UID')
    submit = SubmitField('Submit')

@bp.route('/rr', methods = ["GET", "POST"])
def rr():
    form = SocialForm()
    
    recentFiveReviews = PReview.getTopFive(form.uidInput.data)
    return render_template('hw4_socials.html',
                    resultReviews=recentFiveReviews,
                    form=form
                    )

    # render the page by adding information to the index.html file