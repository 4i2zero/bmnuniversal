import os
from flask import render_template, redirect, url_for, flash, request, jsonify, session, send_from_directory
from flask_login import login_required, current_user
from . import cms
from app.extensions import db
from werkzeug.utils import secure_filename
from app.models import Artist, User, Releaseinfo, Songinfo


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp3', 'wav', 'flac'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@cms.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('J:/bmn_universal_music/app/uploads',filename)


@cms.route("/")
@login_required
def cmsdash():
    user = current_user
    name = session.get('name')
    email = session.get('email')
    phone = session.get('phone')
    revenue = session.get('revenue')
    artists = Artist.query.filter_by(email=email).all()
    flash(f'Welcome {name}!', 'success')
    return render_template('cms/dashboard.html', user=user, name=name, email=email, phone=phone, revenue=revenue, artists=artists , active='dashboard')

@cms.route("/create-release")
@login_required
def create_release():
    artists = Artist.query.filter_by(email=current_user.email).all()
    return render_template('cms/create-release.html', artists=artists, active='create-release')

@cms.route("/catalog")
@login_required
def catalog():
    catalogs = Releaseinfo.query.filter_by(email=current_user.email).all()
    return render_template('cms/catalog.html', catalogs=catalogs, active='catalog')

@cms.route("/catalog/<int:releseid>")
@login_required
def catalog_details(releseid):
    release = Releaseinfo.query.filter_by(id=releseid).first()
    return render_template('cms/catalog-details.html', release=release, active='catalog')

@cms.route("/api/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part 
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return jsonify({'message': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            jsonify({'message': 'No selected file'}), 400
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('J:/bmn_universal_music/app/uploads', filename))
            return jsonify({'message': 'File uploaded successfully!', 'filename': filename}), 200
        return jsonify({'message': 'Invalid file type!'}), 400

@cms.route("/api/addArtist", methods=['POST'])
def add_artist():
    if request.method == 'POST':
        artist_name = request.json.get('artist_name')
        spotify_id = request.json.get('spotify_id')
        apple_id = request.json.get('apple_id')
        user = current_user
        email = user.email
        new_artist = Artist(email=email, artist_name=artist_name, spotify_id=spotify_id, apple_id=apple_id)
        db.session.add(new_artist)
        db.session.commit()
        return jsonify({'message': 'Artist added successfully!'}), 200

@cms.route("/api/createReleaseInfo", methods=['POST'])
def create_release_info():
    if request.method == 'POST':
        album_artwork = request.json.get('album_artwork')
        release_title = request.json.get('release_title')
        release_type = request.json.get('release_type')
        primary_artist1 = request.json.get('primary_artist1')
        primary_artist2 = request.json.get('primary_artist2')
        primary_artist3 = request.json.get('primary_artist3')
        featuring1 = request.json.get('featuring1')
        featuring2 = request.json.get('featuring2')
        featuring3 = request.json.get('featuring3')
        genre = request.json.get('genre')
        sub_genre = request.json.get('sub_genre')
        lable_name = request.json.get('lable_name')
        release_date = request.json.get('release_date')
        p_line = request.json.get('p_line')
        c_line = request.json.get('c_line')
        upc_ean = request.json.get('upc_ean')
        email = current_user.email
        new_release = Releaseinfo(email=email, album_artwork=album_artwork, release_title=release_title, release_type=release_type, primary_artist1=primary_artist1, primary_artist2=primary_artist2, primary_artist3=primary_artist3, featuring1=featuring1, featuring2=featuring2, featuring3=featuring3, genre=genre, sub_genre=sub_genre, lable_name=lable_name, release_date=release_date, p_line=p_line, c_line=c_line, upc_ean=upc_ean)
        db.session.add(new_release)
        db.session.commit()
        latest_release_id = new_release.id
        return jsonify({'message': 'Release info created successfully!', 'release_id': latest_release_id}), 200

@cms.route("/api/addSongInfo", methods=['POST'])
def add_song_info():
    if request.method == 'POST':
        release_id = request.json.get('release_id')
        audio_track = request.json.get('audio_track')
        track_version = request.json.get('track_version')
        instrumental = request.json.get('instrumental')
        title = request.json.get('title')
        version_subtitle = request.json.get('version_subtitle')
        primary_artist1 = request.json.get('primary_artist1')
        primary_artist2 = request.json.get('primary_artist2')
        primary_artist3 = request.json.get('primary_artist3')
        featuring1 = request.json.get('featuring1')
        featuring2 = request.json.get('featuring2')
        featuring3 = request.json.get('featuring3')
        author1 = request.json.get('author1')
        author2 = request.json.get('author2')
        author3 = request.json.get('author3')
        composer1 = request.json.get('composer1')
        composer2 = request.json.get('composer2')
        composer3 = request.json.get('composer3')
        producer = request.json.get('producer')
        p_line = request.json.get('p_line')
        production_year = request.json.get('production_year')
        publisher = request.json.get('publisher')
        isrc_yes_no = request.json.get('isrc_yes_no')
        isrc = request.json.get('isrc')
        genre = request.json.get('genre')
        subgenre = request.json.get('subgenre')
        price_tier = request.json.get('price_tier')
        explicit_version = request.json.get('explicit_version')
        track_title_language = request.json.get('track_title_language')
        lyrics_language = request.json.get('lyrics_language')
        lyrics = request.json.get('lyrics')
        caller_tune = request.json.get('caller_tune')
        destribute_music = request.json.get('destribute_music')
        video_isrc = request.json.get('video_isrc')
        download_video_link = request.json.get('download_video_link')
        saved = request.json.get('saved')
        edit = request.json.get('edit')
        primary_artist1 = Artist.query.filter_by(id=primary_artist1).first()
        selectedSongPrimaryArtist = [{'artist_id': primary_artist1.id,'artist_name': primary_artist1.artist_name, 'apple_id': primary_artist1.apple_id, 'spotify_id': primary_artist1.spotify_id}]
        selectedSongfeaturingArtist = request.json.get('selectedSongfeaturingArtist')
        selectedSongAuthor = request.json.get('selectedSongAuthor')
        selectedSongComposer = request.json.get('selectedSongComposer')
        email = current_user.email
        new_songinfo = Songinfo(email=email, release_id=release_id, audio_track=audio_track, track_version=track_version, instrumental=instrumental, title=title, version_subtitle=version_subtitle, primary_artist1=primary_artist1.artist_name, primary_artist2=primary_artist2, primary_artist3=primary_artist3, featuring1=featuring1, featuring2=featuring2, featuring3=featuring3, author1=author1, author2=author2, author3=author3, composer1=composer1, composer2=composer2, composer3=composer3, producer=producer, p_line=p_line, production_year=production_year, publisher=publisher, isrc_yes_no=isrc_yes_no, isrc=isrc, genre=genre, subgenre=subgenre, price_tier=price_tier, explicit_version=explicit_version, track_title_language=track_title_language, lyrics_language=lyrics_language, lyrics=lyrics, caller_tune=caller_tune, destribute_music=destribute_music, video_isrc=video_isrc, download_video_link=download_video_link, saved=saved, edit=edit, selectedSongPrimaryArtist=selectedSongPrimaryArtist, selectedSongfeaturingArtist=selectedSongfeaturingArtist, selectedSongAuthor=selectedSongAuthor, selectedSongComposer=selectedSongComposer)
        db.session.add(new_songinfo)
        db.session.commit()
        latest_song_id = new_songinfo.id
        return jsonify({'message': 'Song info added successfully!', 'song_id': latest_song_id}), 200

@cms.route("/api/SubmissionData/<int:releseid>", methods=['GET'])
def submission_data(releseid):
    if request.method == 'POST':
        release_id = releseid
        release = Releaseinfo.query.filter_by(id=release_id).first()
        album_artwork = release.album_artwork
        release_title = release.release_title
        genre = release.genre
        sub_genre = release.sub_genre
        lable_name = release.lable_name
        primary_artist1 = release.primary_artist1
        tracks = Songinfo.query.filter_by(release_id=release_id).all()
        number_of_tracks = len(tracks)
        return jsonify({'album_artwork': album_artwork, 'release_title': release_title, 'genre': genre, 'sub_genre': sub_genre, 'lable_name': lable_name, 'primary_artist1': primary_artist1, 'number_of_tracks': number_of_tracks}), 200


@cms.route("/catalog", methods=['GET'])
def get_catalog():
    return render_template('cms/catalog.html', active='catalog')



'''
GET Logos:
    URL : /api/getLogos
    Method : GET
    Response :
    [
        {
            "logo_id": 1,
            "type": "1",
            "name": "7 Digital",
            "logo": "https://backend.fronicmedia.com/17.png"
        },
        {
            "logo_id": 2,
            "type": "1",
            "name": "Adaptr",
            "logo": "https://backend.fronicmedia.com/59.png"
        },
        {
            "logo_id": 3,
            "type": "1",
            "name": "Amazon",
            "logo": "https://backend.fronicmedia.com/3.png"
        },
        {
            "logo_id": 4,
            "type": "1",
            "name": "AMI Entertainment",
            "logo": "https://backend.fronicmedia.com/60.png"
        },
        {
            "logo_id": 5,
            "type": "1",
            "name": "Anghami",
            "logo": "https://backend.fronicmedia.com/18.png"
        },
        {
            "logo_id": 6,
            "type": "1",
            "name": "Apple Music",
            "logo": "https://backend.fronicmedia.com/2.png"
        },
        {
            "logo_id": 7,
            "type": "1",
            "name": "Artcore (Curated)",
            "logo": "https://backend.fronicmedia.com/91.png"
        },
        {
            "logo_id": 8,
            "type": "1",
            "name": "Audible Magic",
            "logo": "https://backend.fronicmedia.com/20.png"
        },
        {
            "logo_id": 9,
            "type": "1",
            "name": "Audiomack",
            "logo": "https://backend.fronicmedia.com/49.png"
        },
        {
            "logo_id": 10,
            "type": "1",
            "name": "AWA",
            "logo": "https://backend.fronicmedia.com/61.png"
        },
        {
            "logo_id": 11,
            "type": "1",
            "name": "Beatport (Curated)",
            "logo": "https://backend.fronicmedia.com/19.png"
        },
        {
            "logo_id": 12,
            "type": "1",
            "name": "Beatsource (Curated)",
            "logo": "https://backend.fronicmedia.com/24.png"
        },
        {
            "logo_id": 13,
            "type": "1",
            "name": "Bmat",
            "logo": "https://backend.fronicmedia.com/25.png"
        },
        {
            "logo_id": 14,
            "type": "1",
            "name": "Boomplay",
            "logo": "https://backend.fronicmedia.com/30.jpg"
        },
        {
            "logo_id": 15,
            "type": "1",
            "name": "ClicknClear (Licensing)",
            "logo": "https://backend.fronicmedia.com/58.png"
        },
        {
            "logo_id": 16,
            "type": "1",
            "name": "Damroo",
            "logo": "https://backend.fronicmedia.com/92.png"
        },
        {
            "logo_id": 17,
            "type": "1",
            "name": "Deezer",
            "logo": "https://backend.fronicmedia.com/10.png"
        },
        {
            "logo_id": 18,
            "type": "1",
            "name": "Facebook,Instagram",
            "logo": "https://backend.fronicmedia.com/9.png"
        },
        {
            "logo_id": 19,
            "type": "1",
            "name": "Fizy",
            "logo": "https://backend.fronicmedia.com/27.png"
        },
        {
            "logo_id": 20,
            "type": "1",
            "name": "FLO Music",
            "logo": "https://backend.fronicmedia.com/63.png"
        },
        {
            "logo_id": 21,
            "type": "1",
            "name": "Gaana",
            "logo": "https://backend.fronicmedia.com/8.png"
        },
        {
            "logo_id": 22,
            "type": "1",
            "name": "Genie Music",
            "logo": "https://backend.fronicmedia.com/64.png"
        },
        {
            "logo_id": 23,
            "type": "1",
            "name": "Gracenote",
            "logo": "https://backend.fronicmedia.com/28.png"
        },
        {
            "logo_id": 24,
            "type": "1",
            "name": "Hungama",
            "logo": "https://backend.fronicmedia.com/7.png"
        },
        {
            "logo_id": 25,
            "type": "1",
            "name": "iHeartRadio",
            "logo": "https://backend.fronicmedia.com/65.png"
        },
        {
            "logo_id": 26,
            "type": "1",
            "name": "iMusica",
            "logo": "https://backend.fronicmedia.com/66.png"
        },
        {
            "logo_id": 27,
            "type": "1",
            "name": "Jaxsta",
            "logo": "https://backend.fronicmedia.com/29.png"
        },
        {
            "logo_id": 28,
            "type": "1",
            "name": "JioSaavn",
            "logo": "https://backend.fronicmedia.com/4.png"
        },
        {
            "logo_id": 29,
            "type": "1",
            "name": "JOOX",
            "logo": "https://backend.fronicmedia.com/67.png"
        },
        {
            "logo_id": 30,
            "type": "1",
            "name": "KK Box",
            "logo": "https://backend.fronicmedia.com/21.png"
        },
        {
            "logo_id": 31,
            "type": "1",
            "name": "Kuack Media",
            "logo": "https://backend.fronicmedia.com/68.png"
        },
        {
            "logo_id": 32,
            "type": "1",
            "name": "LICKD",
            "logo": "https://backend.fronicmedia.com/69.png"
        },
        {
            "logo_id": 33,
            "type": "1",
            "name": "Line Music",
            "logo": "https://backend.fronicmedia.com/48.png"
        },
        {
            "logo_id": 34,
            "type": "1",
            "name": "Lyricfind",
            "logo": "https://backend.fronicmedia.com/45.png"
        },
        {
            "logo_id": 35,
            "type": "1",
            "name": "Mdundo (Curated)",
            "logo": "https://backend.fronicmedia.com/70.png"
        },
        {
            "logo_id": 36,
            "type": "1",
            "name": "MePlaylist",
            "logo": "https://backend.fronicmedia.com/71.png"
        },
        {
            "logo_id": 37,
            "type": "1",
            "name": "Mixcloud",
            "logo": "https://backend.fronicmedia.com/50.png"
        },
        {
            "logo_id": 38,
            "type": "1",
            "name": "Mood Media",
            "logo": "https://backend.fronicmedia.com/72.png"
        },
        {
            "logo_id": 39,
            "type": "1",
            "name": "Music Worx",
            "logo": "https://backend.fronicmedia.com/74.png"
        },
        {
            "logo_id": 40,
            "type": "1",
            "name": "Muska",
            "logo": "https://backend.fronicmedia.com/97.png"
        },
        {
            "logo_id": 41,
            "type": "1",
            "name": "Napster",
            "logo": "https://backend.fronicmedia.com/15.png"
        },
        {
            "logo_id": 42,
            "type": "1",
            "name": "NetEase Cloud Music",
            "logo": "https://backend.fronicmedia.com/75.png"
        },
        {
            "logo_id": 43,
            "type": "1",
            "name": "Nuuday",
            "logo": "https://backend.fronicmedia.com/76.png"
        },
        {
            "logo_id": 44,
            "type": "1",
            "name": "Pandora",
            "logo": "https://backend.fronicmedia.com/77.png"
        },
        {
            "logo_id": 45,
            "type": "1",
            "name": "Peloton",
            "logo": "https://backend.fronicmedia.com/78.png"
        },
        {
            "logo_id": 46,
            "type": "1",
            "name": "Phonographic Performance Limited India",
            "logo": "https://backend.fronicmedia.com/94.png"
        },
        {
            "logo_id": 47,
            "type": "1",
            "name": "Phononet",
            "logo": "https://backend.fronicmedia.com/79.png"
        },
        {
            "logo_id": 48,
            "type": "1",
            "name": "Pretzel Rocks",
            "logo": "https://backend.fronicmedia.com/80.png"
        },
        {
            "logo_id": 49,
            "type": "1",
            "name": "Qisum",
            "logo": "https://backend.fronicmedia.com/98.png"
        },
        {
            "logo_id": 50,
            "type": "1",
            "name": "Qobuz",
            "logo": "https://backend.fronicmedia.com/51.png"
        },
        {
            "logo_id": 51,
            "type": "1",
            "name": "Resso",
            "logo": "https://backend.fronicmedia.com/46.png"
        },
        {
            "logo_id": 52,
            "type": "1",
            "name": "ROXI (via 7Digital)",
            "logo": "https://backend.fronicmedia.com/81.png"
        },
        {
            "logo_id": 53,
            "type": "1",
            "name": "Shazam",
            "logo": "https://backend.fronicmedia.com/13.png"
        },
        {
            "logo_id": 54,
            "type": "1",
            "name": "Snapchat",
            "logo": "https://backend.fronicmedia.com/82.png"
        },
        {
            "logo_id": 55,
            "type": "1",
            "name": "Songtrust (Publishing)",
            "logo": "https://backend.fronicmedia.com/56.png"
        },
        {
            "logo_id": 56,
            "type": "1",
            "name": "Soundcloud",
            "logo": "https://backend.fronicmedia.com/14.png"
        },
        {
            "logo_id": 57,
            "type": "1",
            "name": "Spotify",
            "logo": "https://backend.fronicmedia.com/1.png"
        },
        {
            "logo_id": 58,
            "type": "1",
            "name": "Stellar Entertainment (Curated)",
            "logo": "https://backend.fronicmedia.com/87.png"
        },
        {
            "logo_id": 59,
            "type": "1",
            "name": "Tencent Music",
            "logo": "https://backend.fronicmedia.com/52.png"
        },
        {
            "logo_id": 60,
            "type": "1",
            "name": "Tidal",
            "logo": "https://backend.fronicmedia.com/11.png"
        },
        {
            "logo_id": 61,
            "type": "1",
            "name": "Tiktok",
            "logo": "https://backend.fronicmedia.com/12.png"
        },
        {
            "logo_id": 62,
            "type": "1",
            "name": "TIM Music (Curated)",
            "logo": "https://backend.fronicmedia.com/83.png"
        },
        {
            "logo_id": 63,
            "type": "1",
            "name": "TouchTunes",
            "logo": "https://backend.fronicmedia.com/84.png"
        },
        {
            "logo_id": 64,
            "type": "1",
            "name": "Traxsource (Curated)",
            "logo": "https://backend.fronicmedia.com/85.png"
        },
        {
            "logo_id": 65,
            "type": "1",
            "name": "Trebel",
            "logo": "https://backend.fronicmedia.com/87.png"
        },
        {
            "logo_id": 66,
            "type": "1",
            "name": "Tuned Global",
            "logo": "https://backend.fronicmedia.com/99.png"
        },
        {
            "logo_id": 67,
            "type": "1",
            "name": "United Media Agency",
            "logo": "https://backend.fronicmedia.com/23.png"
        },
        {
            "logo_id": 68,
            "type": "1",
            "name": "Volumo (Curated)",
            "logo": "https://backend.fronicmedia.com/55.png"
        },
        {
            "logo_id": 69,
            "type": "1",
            "name": "Wynk Music",
            "logo": "https://backend.fronicmedia.com/6.png"
        },
        {
            "logo_id": 70,
            "type": "1",
            "name": "Yandex",
            "logo": "https://backend.fronicmedia.com/22.png"
        },
        {
            "logo_id": 71,
            "type": "1",
            "name": "Youtube Music",
            "logo": "https://backend.fronicmedia.com/5.png"
        },
        {
            "logo_id": 72,
            "type": "1",
            "name": "ZingMP3",
            "logo": "https://backend.fronicmedia.com/47.png"
        },
        {
            "logo_id": 80,
            "type": "2",
            "name": "BSNL",
            "logo": "https://backend.fronicmedia.com/54.png"
        },
        {
            "logo_id": 81,
            "type": "2",
            "name": "JIO",
            "logo": "https://backend.fronicmedia.com/53.png"
        },
        {
            "logo_id": 82,
            "type": "2",
            "name": "Airtel",
            "logo": "https://backend.fronicmedia.com/33.png"
        },
        {
            "logo_id": 83,
            "type": "2",
            "name": "Vi",
            "logo": "https://backend.fronicmedia.com/32.png"
        },
        {
            "logo_id": 93,
            "type": "3",
            "name": "AMI Entertainment",
            "logo": "https://backend.fronicmedia.com/60.png"
        },
        {
            "logo_id": 94,
            "type": "3",
            "name": "Apple Music (Paid)",
            "logo": "https://backend.fronicmedia.com/36.png"
        },
        {
            "logo_id": 95,
            "type": "3",
            "name": "Boomplay",
            "logo": "https://backend.fronicmedia.com/30.jpg"
        },
        {
            "logo_id": 96,
            "type": "3",
            "name": "Facebook PMV",
            "logo": "https://backend.fronicmedia.com/88.png"
        },
        {
            "logo_id": 97,
            "type": "3",
            "name": "Fizy",
            "logo": "https://backend.fronicmedia.com/27.png"
        },
        {
            "logo_id": 98,
            "type": "3",
            "name": "Gogopix (Curated)",
            "logo": "https://backend.fronicmedia.com/89.png"
        },
        {
            "logo_id": 99,
            "type": "3",
            "name": "Hungama",
            "logo": "https://backend.fronicmedia.com/37.png"
        },
        {
            "logo_id": 100,
            "type": "3",
            "name": "Line Music",
            "logo": "https://backend.fronicmedia.com/48.png"
        },
        {
            "logo_id": 101,
            "type": "3",
            "name": "ROXi Video",
            "logo": "https://backend.fronicmedia.com/90.png"
        },
        {
            "logo_id": 102,
            "type": "3",
            "name": "Tencent",
            "logo": "https://backend.fronicmedia.com/52.png"
        },
        {
            "logo_id": 103,
            "type": "3",
            "name": "Tidal",
            "logo": "https://backend.fronicmedia.com/40.png"
        },
        {
            "logo_id": 104,
            "type": "3",
            "name": "TikTok Music\n",
            "logo": "https://backend.fronicmedia.com/96.png"
        },
        {
            "logo_id": 105,
            "type": "3",
            "name": "VI",
            "logo": "https://backend.fronicmedia.com/32.png"
        },
        {
            "logo_id": 106,
            "type": "3",
            "name": "Xite",
            "logo": "https://backend.fronicmedia.com/42.png"
        },
        {
            "logo_id": 107,
            "type": "3",
            "name": "ZingMP3",
            "logo": "https://backend.fronicmedia.com/47.png"
        }
    ]
'''