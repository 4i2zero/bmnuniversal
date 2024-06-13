from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from . import cms
from app.extensions import db

@cms.route("/")
@login_required
def cmsdash():
    return render_template('cms/dashboard.html')