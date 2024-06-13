from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from . import admin
from app.extensions import db

@admin.route("/")
@login_required
def admindash():
    if current_user.is_admin == True :
        return render_template('admin/dashboard.html')
    else:
        flash('You are not authorized to view this page', 'danger' )
        return redirect(url_for('main.index'))