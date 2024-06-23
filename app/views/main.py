from flask import render_template, url_for, flash, redirect, request
from . import main
from app.extensions import db, bcrypt
from app.models import User

@main.route("/")
def index():
    return render_template('main/index.html')


@main.route("/AshiBawana", methods=['GET'])
def AshiBawana():
    return redirect("https://www.instagram.com/ashibawana.official")

@main.route("/4i2zero", methods=['GET'])
def jerry():
    return redirect("https://www.instagram.com/4i2zero")

@main.route("/AB01-spotify", methods=['GET'])
def ab_spotify():
    return redirect("https://open.spotify.com/track/2bQ2EexyavY52HwounFaWJ")

@main.route("/AB01-wynk", methods=['GET'])
def ab_wynk():
    return redirect("https://wynk.in/u/sQUAOpNTa")

@main.route("/AB01-jiosaavan", methods=['GET'])
def ab_jiosaavan():
    return redirect("https://www.jiosaavn.com/song/chori-haryanvi/AlktACdnblo")

@main.route("/AB01-hungama", methods=['GET'])
def ab_hungama():
    return redirect("https://www.hungama.com/song/chori-haryanvi/102494206/") 

@main.route("/AB01-primemusic", methods=['GET'])
def ab_primemusic():
    return redirect("https://music.amazon.in/albums/B0C4K1GRYS")

@main.route("/AB01-soundcloud", methods=['GET'])
def ab_soundcloud():
    return redirect("https://on.soundcloud.com/GP8sSaheVVPTsKcE6")

@main.route("/AB01-reel", methods=['GET'])
def ab_reel():
    return redirect("https://www.instagram.com/reels/audio/251509907463238/")

@main.route("/AB01-gaana", methods=['GET'])
def ab_gaana():
    return redirect("https://gaana.com/album/chori-haryanvi")