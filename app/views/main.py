from flask import render_template, url_for, flash, redirect, request
from . import main
from app.extensions import db, bcrypt
from app.models import User

@main.route("/")
def index():
    return render_template('main/index.html')

@main.route("/our-services")
def our_services():
    return render_template('main/our_services.html')

@main.route("/our-services/digital-stores")
def digital_stores():
    return render_template('main/digital_stores.html')

@main.route("/our-services/music-distribution")
def music_distribution():
    return render_template('main/music_distribution.html')

@main.route("/our-services/video-distribution")
def video_distribution():
    return render_template('main/video_distribution.html')

@main.route("/our-services/caller-tunes-delivery")
def caller_tunes_delivery():
    return render_template('main/caller_tunes_delivery.html')

@main.route("/our-services/youtube-content-id")
def youtube_content_id():
    return render_template('main/youtube_content_id.html')

@main.route("/our-services/artist-tools")
def artist_tools():
    return render_template('main/artist_tools.html')

@main.route("/our-services/music-promotion")
def music_promotion():
    return render_template('main/music_promotion.html')

@main.route("/blog")
def blog():
    return render_template('main/blog.html')

@main.route("/blog/post")
def blog_post():
    return render_template('main/blog_post.html')

@main.route("/faq")
def faq():
    return render_template('main/faq.html')

@main.route("/about")
def about_us():
    return render_template('main/about_us.html')

@main.route("/contact-us")
def contact_us():
    return render_template('main/contact_us.html')

@main.route("/privacy-policy")
def privacy_policy():
    return render_template('main/privacy_policy.html')

@main.route("/distribution-agreement")
def distribution_agreement():
    return render_template('main/distribution_agreement.html')