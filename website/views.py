from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import json
import random 

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    a=1
    b=2
    c=3
    if request.method == 'POST': 
            if current_user.Bibki < 1:
                flash('Мало бибок!', category='error') 
            else:
                a=random.randint(0,9)
                print (a)
                b=random.randint(0,9)
                print (b)
                c=random.randint(0,9)
                print (c)
                if (a==b) and (a==c):
                    current_user.Bibki=current_user.Bibki+1000
                elif (a==b) or (b==c) or (a==c):
                     current_user.Bibki=current_user.Bibki+50
                current_user.Bibki=current_user.Bibki-10  
                db.session.commit()      
                flash('Новые цыфорки!', category='success')

    return render_template("home.html", user=current_user,a1=a,b1=b,c1=c,Bibki1=current_user.Bibki)
