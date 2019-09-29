import urllib.request
import base64
import cv2
import flask
import numpy as np
import requests
from matplotlib import pyplot as plt

# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
# from app import db

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import User
# Define the blueprint: 'auth', set its url prefix: app.url/auth


mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
# @mod_auth.route('/signin/', methods=['POST'])
def signin():
    if request.method=="POST":
        po=request.get_data()
        po=urllib.parse.unquote(po.decode('utf-8'))
        po=po[4:]
        po=po[:po.index('&')]
        po=base64.b64decode(po)
        img= cv2.imdecode(np.fromstring(po, dtype='uint8'),1)
        # plt.imshow(img)
        # plt.show()
        imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # print(imgray)
        # plt.imshow(imgray)
        # plt.show()
        imgEncode = cv2.imencode(".jpg", imgray)[1]
        imgstr = np.array(imgEncode).tostring()
        imgData = base64.b64encode(imgstr)
        return imgData
    # if request.method=='GET':
    #     data='已发送'
    #     return data
        # return '好的，准备发送'
#     # If sign in form is submitted
#     form = LoginForm(request.form)

#     # Verify the sign in form
#     if form.validate_on_submit():
#
#         user = User.query.filter_by(email=form.email.data).first()
#
#         if user and check_password_hash(user.password, form.password.data):
#
#             session['user_id'] = user.id
#
#             flash('Welcome %s' % user.name)
#
#             return redirect(url_for('auth.home'))
#
#         flash('Wrong email or password', 'error-message')
#
#     return render_template("auth/signin.html", form=form)
#
# # # elevateChina






