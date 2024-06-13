from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from . import cms
from app.extensions import db

@cms.route("/")
@login_required
def cmsdash():
    return render_template('cms/dashboard.html')


@cms.route("/user-profile")
@login_required
def user_profile():
    return render_template('cms/user_profile.html')

@cms.route("/create-release")
@login_required
def create_release():
    return render_template('cms/create_release.html')

@cms.route("/create-release/audio")
@login_required
def create_release_audio():
    return render_template('cms/create_release_audio.html')

@cms.route("/create-release/video")
@login_required
def create_release_video():
    return render_template('cms/create_release_video.html')

@cms.route("/catalog")
@login_required
def catalog():
    return render_template('cms/catalog.html')

@cms.route("/catalog/info/<id>")
@login_required
def catalog_info(id):
    return render_template('cms/catalog_info.html', id=id)

@cms.route("/reports")
@login_required
def reports():
    return render_template('cms/reports.html')

@cms.route("/reports/info/<id>")
@login_required
def reports_info(id):
    return render_template('cms/reports_info.html', id=id)

@cms.route("/withdrawls")
@login_required
def withdrawls():
    return render_template('cms/withdrawls.html')

@cms.route("/withdrawls/request")
@login_required
def withdrawls_request():
    return render_template('cms/withdrawls_request.html')

@cms.route("/withdrawls/addbank")
@login_required
def withdrawls_addbank():
    return render_template('cms/withdrawls_addbank.html')

@cms.route("/tools/distribute/lyrics")
@login_required
def distribute_lyrics():
    return render_template('cms/distribute_lyrics.html')

@cms.route("/tools/distribute/lyrics/info/<id>")
@login_required
def distribute_lyrics_info(id):
    return render_template('cms/distribute_lyrics_info.html', id=id)

@cms.route("/tools/distribute/playlist-pitchment")
@login_required
def distribute_playlist_pitchment():
    return render_template('cms/distribute_playlist_pitchment.html')

@cms.route("/tools/distribute/playlist-pitchment/info/<id>")
@login_required
def distribute_playlist_pitchment_info(id):
    return render_template('cms/distribute_playlist_pitchment_info.html', id=id)

@cms.route("/tools/distribute/profile-link")
@login_required
def distribute_profile_link():
    return render_template('cms/distribute_profile_link.html')

@cms.route("/tools/distribute/profile-link/info/<id>")
@login_required
def distribute_profile_link_info(id):
    return render_template('cms/distribute_profile_link_info.html', id=id)

@cms.route("/tools/distribute/ugc-claims")
@login_required
def distribute_ugc_claims():
    return render_template('cms/distribute_ugc_claims.html')

@cms.route("/tools/distribute/ugc-claims/info/<id>")
@login_required
def distribute_ugc_claims_info(id):
    return render_template('cms/distribute_ugc_claims_info.html', id=id)

@cms.route("/ticket")
@login_required
def ticket():
    return render_template('cms/ticket.html')

@cms.route("/ticket/new")
@login_required
def ticket_new():
    return render_template('cms/ticket_new.html')

@cms.route("/ticket/info/<id>")
@login_required
def ticket_info(id):
    return render_template('cms/ticket_info.html', id=id)

@cms.route("/invite")
@login_required
def invite():
    return render_template('cms/invite.html')