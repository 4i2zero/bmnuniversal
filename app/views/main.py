from flask import render_template, url_for, flash, redirect, request
from . import main
from app.extensions import db, bcrypt
from app.models import User

@main.route("/")
def index():
    return render_template('main/index.html')

@main.route("/music-distribution")
def music_distribution():
    return render_template('main/music-distribution.html')

@main.route("/video-distribution")
def video_distribution():
    return render_template('main/video-distribution.html')

@main.route("/youtube-content-id")
def youtube_content_id():
    return render_template('main/youtube-content-id.html')

@main.route("/callertune-distribution")
def callertune_distribution():
    return render_template('main/callertune-distribution.html')

@main.route("/music-marketing")
def music_marketing():
    return render_template('main/music-marketing.html')

@main.route("/artist-toolkit")
def artist_toolkit():
    return render_template('main/artist-toolkit.html')

@main.route("/pricing")
def pricing():
    return render_template('main/pricing.html')

@main.route("/about")
def about():
    return render_template('main/about.html')

@main.route("/faq")
def faq():
    return render_template('main/faq.html')
