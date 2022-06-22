from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Workstation
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


wks = Blueprint('wks', __name__)

@wks.route('/workstation')
def workstation():
    if request.method =='POST':
        wks_name = request.form.get('wks_name')

        wks_name = Workstation.query.filter_by(wks_name=wks_name).first()
        if wks_name:
            flash('Workstation already exists', category='error')
        elif len(wks_name) < 8:
            flash('Workstation name must be at least 8 characters', category='error')
        else:
            new_wks_name = Workstation(wks_name=wks_name)
            db.session.add(new_wks_name)
            db.session.commit()
            flash('Workstation added', category='success')
            return redirect(url_for('views.home'))

    return render_template("work_station.html")
