import os
from flask import render_template, redirect, url_for, flash, request, jsonify, session, send_from_directory
from flask_login import login_required, current_user
from . import cms
from app.extensions import db
from werkzeug.utils import secure_filename
from app.models import Artist, User, Album, Song, Store, Report, Ticket, Message, Ugc, Profilelinking, Distributelyrics
import os

# Get the directory of the current file (api.py) within the views folder
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up to the parent directory (where views folder is located)
parent_dir = os.path.dirname(current_dir)

# Construct the path to the uploads folder, which is at the same level as views
path = os.path.join(parent_dir, 'uploads')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp3', 'wav', 'flac'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@cms.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(path,filename)


@cms.route("/")
@login_required
def cmsdash():
    user = current_user
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    catlogs = Album.query.filter_by(user_id=user.id).count()
    artists = Artist.query.filter_by(user_id=user.id).count()
    flash(f'Welcome {name}!', 'success')
    return render_template('cms/dashboard.html', user=user, name=name, email=email, revenue=revenue, artists=artists, catlogs=catlogs , nav_id="dashboard")

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
            session['filename'] = filename
            file.save(os.path.join(path, filename))
            return jsonify({'message': 'File uploaded successfully!', 'filename': filename}), 200
        return jsonify({'message': 'Invalid file type!'}), 400

@cms.route("/create-release", methods=['GET', 'POST'])
@login_required
def create_release():
    if request.method == 'POST':
        user = current_user
        filename = session.get('filename')

        if 'upcEan' not in request.form['upcEan']:
            upc = "--"
        else:
            upc = request.form['upcEan']

        if 'featuringArtists' not in request.form['featuringArtists']:
            featuring = "--"
        else:
            featuring = request.form['featuringArtists']

    
        title = request.form['title']
        type = request.form['type']
        primary_artist1 = request.form['primaryArtists']
        featuring_artist1 = featuring
        genre = request.form['genre']
        sub_genre = request.form['subGenre']
        label_name = request.form['labelName']
        release_date = request.form['releaseDate']
        p_line = request.form['pLine']
        c_line = request.form['cLine']
        upc_ean = upc
        album = Album(user_id=user.id, artwork=filename, title=title, type=type, primary_artist1=primary_artist1, featuring_artist1=featuring_artist1, genre=genre, sub_genre=sub_genre, label_name=label_name, release_date=release_date, p_line=p_line, c_line=c_line, upc_ean=upc_ean)
        db.session.add(album)
        db.session.commit()
        session["album_id"] = album.id
        return redirect(url_for('cms.add_track'))
    user = current_user
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    artists = Artist.query.filter_by(user_id=user.id).all()
    return render_template('cms/create-release.html',name=name, email=email, revenue=revenue , artists=artists, nav_id="release")

@cms.route("/create-artist", methods=['POST'])
@login_required
def create_artist():
    if request.method == 'POST':
        user = current_user
        artist_name = request.json['name']
        if 'spotify'in request.json:
            spotify_id = request.json['spotify']
        else:
            spotify_id = "--"
        if 'apple'in request.json:
            apple_id = request.json['apple']
        else:
            apple_id = "--"
        artist = Artist(user_id=user.id, name=artist_name, spotify_id=spotify_id, apple_id=apple_id)
        db.session.add(artist)
        db.session.commit()
        return jsonify({'message': 'Artist created successfully!'}), 200
    
@cms.route("/add-track", methods=['GET','POST'])
@login_required
def add_track():
    if request.method == 'POST':
        album_id = int(request.form['albumId'])
        tracl_File = session.get('filename')
        version = request.form['version']
        instrumental = request.form['instrumental']
        title = request.form['title']
        subtitle = request.form['subtitle']
        primary_artist = request.form['primaryArtists']
        featuring_artists = request.form['featuringArtists']
        author = request.form['author']
        producer = request.form['producer']
        composer = request.form['composer']
        p_line = request.form['pLine']
        production_year = request.form['productionYear']
        publisher = request.form['publisher']
        genre = request.form['genre']
        sub_genre = request.form['subGenre']
        explicit = request.form['explicit']
        if explicit == 'True':
            explicit = True
        else:
            explicit = False
        title_language = request.form['titleLanguage']
        lyrics_language = request.form['lyricsLanguage']
        lyrics = request.form['lyrics']
        callertune = request.form['callertune']
        song = Song(album_id=album_id, track=tracl_File, version=version, instrumental=instrumental, title=title, subtitle=subtitle, primary_artist1=primary_artist, featuring_artist1=featuring_artists, author=author, composer=composer, producer=producer, p_line=p_line, production_year=production_year, publisher=publisher, genre=genre, subgenre=sub_genre, explicit=explicit, title_language=title_language, lyrics_language=lyrics_language, lyrics=lyrics, caller_tune=callertune)
        db.session.add(song)
        db.session.commit()
        stores = [
            '7 Digital',
            'Adaptr',
            'Air India (Curated)',
            'Air Vanuatu (Curated)',
            'AirAsia (Curated)',
            'AirAsiaX (Curated)',
            'Alibaba Music',
            'Amazon',
            'AMI Entertainment',
            'Anghami',
            'Apple Music',
            'Artcore (Curated)',
            'Audible Magic',
            'AudioClub',
            'Audiomack',
            'AWA',
            'Beatport (Curated)',
            'Beatsource (Curated)',
            'Beeline Music',
            'Bmat',
            'Boomplay',
            'Bubuka Audio',
            'Bugs',
            'China Airlines (Curated)',
            'ClicknClear (Licensing)',
            'COOLVOX',
            'Damroo',
            'Deezer',
            'Facebook,Instagram',
            'Fizy',
            'FLO Music',
            'FonMix',
            'Gaana',
            'Genie Music',
            'GMF AeroAsia (Curated)',
            'Gracenote',
            'Grandpad',
            'HUAWEI Music',
            'Hungama',
            'iHeartRadio',
            'iMusica',
            'iTune',
            'Jaxsta',
            'Jetstar (Curated)',
            'JioSaavn',
            'JOOX',
            'Kanijan',
            'KK Box',
            'Kuack Media',
            'Kuaishou',
            'Kugou',
            'Kuwo',
            'Kwai',
            'LICKD',
            'Line Music',
            'Lyricfind',
            'Mdundo (Curated)',
            'Melon',
            'MePlaylist',
            'Migu Music',
            'Mixcloud',
            'MobiMusic (KZ) Audio',
            'Mood Media',
            'MOOV',
            'Music Worx',
            'Muska',
            'Muztube',
            'Napster',
            'Naver Vibe',
            'NEC',
            'NetEase Cloud Music',
            'Nile Air (Curated)',
            'Nuuday',
            'Pandora',
            'Peloton',
            'Philippine Airlines (Curated)',
            'Phonographic Performance Limited India',
            'Phononet',
            'Pretzel Rocks',
            'Psonar',
            'Qantas (Curated)',
            'Qisum',
            'Qobuz',
            'QQ Music',
            'Raku',
            'Resso',
            'ROXI (via 7Digital)',
            'Shazam',
            'Snack Video',
            'Snapchat',
            'Songtrust (Publishing)',
            'Sonos',
            'Soundcloud',
            'Soundtrack Your Brand',
            'Spotify',
            'Stellar Entertainment (Curated)',
            'SunExpress (Curated)',
            'Telmore Musik',
            'Tencent Music',
            'Thai Airways (Curated)',
            'Tidal',
            'Tiktok',
            'TIM Music (Curated)',
            'TouchTunes',
            'Traxsource (Curated)',
            'Trebel',
            'Tuned Global',
            'United Media Agency',
            'UtaPass',
            'Virgin Australia (Curated)',
            'Volumo (Curated)',
            'WeSing',
            'Wynk Music',
            'Yandex',
            'YouSee Musik',
            'Youtube Music',
            'Zaycev.net',
            'ZingMP3',
            'Airtel',
            'Belgacom / Tango',
            'BSNL',
            'Celcom',
            'Deutsche Telekom Austria and Netherlands',
            'DiGi',
            'Fastweb',
            'FETnet',
            'iMUSIC (China Telecom)',
            'JIO',
            'Orange France',
            'Swisscom',
            'TELE2',
            'Tigo',
            'U-Mobile',
            'Vi',
        ]     
        song_id = song.id
        session["song_id"] = song_id
        for store in stores:
            newstore = Store(song_id=song_id, store_name=store)
            db.session.add(newstore)
            db.session.commit()
        user = current_user
        songs = Song.query.filter_by(album_id=album_id).all()
        album_id = album_id
        name = session.get('name')
        email = session.get('email')
        revenue = session.get('revenue')
        artists = Artist.query.filter_by(user_id=user.id).all()
        album = Album.query.filter_by(id=album_id).first()
        flash('Track Added successfully!', 'success')
        return render_template('cms/add-song.html', name=name, email=email, revenue=revenue, album=album ,artists=artists, album_id=album_id, songs=songs, nav_id="release")
    else:
        album_id = session.get('album_id')
        user = current_user
        songs = Song.query.filter_by(album_id=album_id).all()
        name = session.get('name')
        email = session.get('email')
        revenue = session.get('revenue')
        artists = Artist.query.filter_by(user_id=user.id).all()
        album = Album.query.filter_by(id=album_id).first()
        flash('Album created successfully!', 'success')
        return render_template('cms/add-song.html', name=name, email=email, revenue=revenue, album=album ,artists=artists, album_id=album_id, songs=songs, nav_id="release")
    

@cms.route("/add-store", methods=['GET','POST'])
@login_required
def add_store():
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    stores = Store.query.filter_by(song_id=session.get('song_id')).all()
    return render_template('cms/add-store.html', name=name, email=email, revenue=revenue, stores=stores, nav_id="release")

@cms.route("/submission")
@login_required
def submission():
    album_id = session.get('album_id')
    user = current_user
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    album = Album.query.filter_by(id=album_id).first()
    songs_number = Song.query.filter_by(album_id=album_id).count()
    return render_template('cms/submission.html', name=name, email=email, revenue=revenue, album=album, songs_number=songs_number, nav_id="release")

@cms.route("/catalog")
@login_required
def catalog():
    user = current_user
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    albums = Album.query.filter_by(user_id=user.id).all()
    total_albums = Album.query.filter_by(user_id=user.id).count()
    return render_template('cms/catalog.html', name=name, email=email, revenue=revenue, albums=albums, total_albums=total_albums, nav_id="catalog")

@cms.route("/album/<int:album_id>")
@login_required
def album(album_id):
    user = current_user
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    album = Album.query.filter_by(id=album_id).first()
    songs = Song.query.filter_by(album_id=album_id).all()
    return render_template('cms/album.html', name=name, email=email, revenue=revenue, album=album, songs=songs, nav_id="catalog")

@cms.route("/stores")
@login_required
def stores():
    user = current_user
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    stores = Store.query.all()
    return render_template('cms/stores.html', name=name, email=email, revenue=revenue, stores=stores, nav_id="dashboard")

@cms.route("/reports", methods=['GET','POST'])
@cms.route("/report", methods=['GET','POST'])
@login_required
def report():
    user = current_user
    if request.method == 'POST':
        report_for = request.form['reportFor']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        report = Report(user_id=user.id, report_for=report_for, start_date=start_date, end_date=end_date)
        db.session.add(report)
        db.session.commit()
        flash('Report Requested successfully!', 'success')
        return redirect(url_for('cms.report'))
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    reports = Report.query.filter_by(user_id=user.id).all()
    return render_template('cms/report.html', name=name, email=email, revenue=revenue,reports=reports, nav_id="reports")


@cms.route("/tickets", methods=['GET','POST'])
@cms.route("/ticket", methods=['GET','POST'])
@login_required
def tickets():
    user = current_user
    if request.method == 'POST':
        reason = request.form['reason']
        ticket = Ticket(user_id=user.id, reason=reason)
        db.session.add(ticket)
        db.session.commit()
        if 'attachment' in request.files:
            file = request.files['attachment']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(path, filename))
                message = request.form['message']
                attachment = filename
                ticket_id = ticket.id
                newmessage = Message(ticket_id=ticket_id,author_id=user.id, message=message, attachment=attachment)
                db.session.add(newmessage)
                db.session.commit()
                flash('Ticket created successfully!', 'success')
                return redirect(url_for('cms.tickets'))
            else:
                message = request.form['message']
                ticket_id = ticket.id
                newmessage = Message(ticket_id=ticket_id,author_id=user.id, message=message)
                db.session.add(newmessage)
                db.session.commit()
                flash('Ticket created successfully!', 'success')
                return redirect(url_for('cms.tickets'))

        else:
            message = request.form['message']
            ticket_id = ticket.id
            newmessage = Message(ticket_id=ticket_id, author_id=user.id , message=message)
            db.session.add(newmessage)
            db.session.commit()
            flash('Ticket created successfully!', 'success')
            return redirect(url_for('cms.tickets'))
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    tickets = Ticket.query.filter_by(user_id=user.id).all()
    return render_template('cms/tickets.html', name=name, email=email, revenue=revenue, tickets=tickets, nav_id="ticket")


@cms.route("/ticket/<int:ticket_id>", methods=['GET','POST'])
@login_required
def ticket(ticket_id):
    if request.method == 'POST':
        message = request.form['message']
        ticket_id = ticket_id
        user = current_user
        newmessage = Message(ticket_id=ticket_id, author_id=user.id , message=message)
        db.session.add(newmessage)
        db.session.commit()
        flash('Message Sent successfully!', 'success')
        return redirect(f'/cms/ticket/{ticket_id}')
    user = current_user
    user_id= user.id
    name = session.get('name')
    email = session.get('email')
    revenue = session.get('revenue')
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    messages = Message.query.filter_by(ticket_id=ticket_id).all()
    return render_template('cms/ticket.html', user_id=user_id,name=name, email=email, revenue=revenue,messages=messages, ticket=ticket, nav_id="ticket")

@cms.route('/withdrawal', methods=['GET','POST'])
@login_required
def withdraw():
    user = current_user
    user_id = user.id
    name = session.get('name')
    email = session.get('email')
    revenue = int(session.get('revenue'))
    return render_template('cms/withdrawal.html',user=user, user_id=user_id , name=name, email=email, revenue=revenue, nav_id="withdrawal")

@cms.route('/ugc-claims', methods=['GET','POST'])
@login_required
def ugc():
    user = current_user
    user_id = user.id
    name = session.get('name')
    email = session.get('email')
    revenue = int(session.get('revenue'))
    ugcs = Ugc.query.filter_by(user_id=user_id).all()
    releases= Album.query.filter_by(user_id=user_id).all()
    if request.method == 'POST':
        release_title = request.form['releaseTitle']
        audio_title = request.form['audioTitle']
        policy = request.form['policy']
        url = request.form['url']
        ugc = Ugc(user_id=user_id, release_title=release_title, audio_title=audio_title, policy=policy, url=url)
        db.session.add(ugc)
        db.session.commit()
        flash('UGC Claimed successfully!', 'success')
        return redirect(url_for('cms.ugc'))
    return render_template('cms/ugc.html', user=user, user_id=user_id, name=name, email=email, releases=releases , revenue=revenue, ugcs=ugcs, nav_id="ugc-claims")

@cms.route('/profile-linking', methods=['GET','POST'])
@login_required
def profilelinking():
    user = current_user
    user_id = user.id
    name = session.get('name')
    email = session.get('email')
    revenue = int(session.get('revenue'))
    profilelinkings = Profilelinking.query.filter_by(user_id=user_id).all()
    releases= Album.query.filter_by(user_id=user_id).all()
    if request.method == 'POST':
        release_title = request.form['releaseTitle']
        audio_title = request.form['audioTitle']
        artist = request.form['artist']
        fb = request.form['fb']
        ig = request.form['ig']
        profilelinking = Profilelinking(user_id=user_id, release_title=release_title, audio_title=audio_title, artist=artist, fb=fb, ig=ig)
        db.session.add(profilelinking)
        db.session.commit()
        flash('Profile Linking Requested Successfully!', 'success')
        return redirect(url_for('cms.profilelinking'))
    return render_template('cms/profilelinking.html', user=user, user_id=user_id, name=name, email=email, releases=releases , revenue=revenue, profilelinkings=profilelinkings, nav_id="profile-linking")


@cms.route('/distributelyrics', methods=['GET','POST'])
@login_required
def distributelyrics():
    user = current_user
    user_id = user.id
    name = session.get('name')
    email = session.get('email')
    revenue = int(session.get('revenue'))
    distributelyricss = Distributelyrics.query.filter_by(user_id=user_id).all()
    releases= Album.query.filter_by(user_id=user_id).all()
    if request.method == 'POST':
        release_title = request.form['releaseTitle']
        audio_title = request.form['audioTitle']
        language = request.form['language']
        lyrics = request.form['lyrics']
        distributelyrics = Distributelyrics(user_id=user_id, release_title=release_title, audio_title=audio_title, language=language, lyrics=lyrics)
        db.session.add(distributelyrics)
        db.session.commit()
        flash('UGC Claimed successfully!', 'success')
        return redirect(url_for('cms.distributelyrics'))
    return render_template('cms/distributelyrics.html', user=user, user_id=user_id, name=name, email=email, releases=releases , revenue=revenue, distributelyricss=distributelyricss, nav_id="distribute-lyrics")
