from flask import render_template, url_for, flash, redirect, request
from . import main
from app.extensions import db, bcrypt
from app.models import User

@main.route("/")
def index():
    return render_template('main/index.html')