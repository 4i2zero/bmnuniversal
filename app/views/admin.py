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
    
@admin.route("/blogs")
@login_required
def blogs():
    if current_user.is_admin:
        return render_template('admin/blogs.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/blog/new")
@login_required
def new_blog():
    if current_user.is_admin:
        return render_template('admin/new_blog.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/blog/<id>")
@login_required
def blog(id):
    if current_user.is_admin:
        return render_template('admin/blog.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/users")
@login_required
def users():
    if current_user.is_admin:
        return render_template('admin/users.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/user/<id>")
@login_required
def user(id):
    if current_user.is_admin:
        return render_template('admin/user.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/releases")
@login_required
def releases():
    if current_user.is_admin:
        return render_template('admin/releases.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/releases/<id>")
@login_required
def release(id):
    if current_user.is_admin:
        return render_template('admin/release.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/tickets")
@login_required
def tickets():
    if current_user.is_admin:
        return render_template('admin/tickets.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/tickets/<id>")
@login_required
def ticket(id):
    if current_user.is_admin:
        return render_template('admin/ticket.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/lyrics")
@login_required
def request_lyrics():
    if current_user.is_admin:
        return render_template('admin/request_lyrics.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/lyrics/<id>")
@login_required
def request_lyrics_id(id):
    if current_user.is_admin:
        return render_template('admin/request_lyrics.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/playlist")
@login_required
def request_playlist():
    if current_user.is_admin:
        return render_template('admin/request_playlist.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/playlist/<id>")
@login_required
def request_playlist_id(id):
    if current_user.is_admin:
        return render_template('admin/request_playlist.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/ugc")
@login_required
def request_ugc():
    if current_user.is_admin:
        return render_template('admin/request_ugc.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/ugc/<id>")
@login_required
def request_ugc_id(id):
    if current_user.is_admin:
        return render_template('admin/request_ugc.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/profile")
@login_required
def request_profile():
    if current_user.is_admin:
        return render_template('admin/request_profile.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/request/profile/<id>")
@login_required
def request_profile_id(id):
    if current_user.is_admin:
        return render_template('admin/request_profile.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/reports")
@login_required
def reports():
    if current_user.is_admin:
        return render_template('admin/reports.html')
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))

@admin.route("/reports/song/<id>")
@login_required
def reports_song(id):
    if current_user.is_admin:
        return render_template('admin/reports_song.html', id=id)
    else:
        flash('You are not authorized to view this page', 'danger')
        return redirect(url_for('main.index'))