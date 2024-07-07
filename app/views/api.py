from flask import jsonify, request
from app.models import User, Artist, Album, Song, Store, Post, Report, Ticket, Message, Ugc, Profilelinking, Distributelyrics
from app.extensions import db
from . import api
from werkzeug.utils import secure_filename
import os

ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3'}
ALLOWED_PHOTO_EXTENSIONS = {'png', 'jpg'}
import os

# Get the directory of the current file (api.py) within the views folder
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up to the parent directory (where views folder is located)
parent_dir = os.path.dirname(current_dir)

# Construct the path to the uploads folder, which is at the same level as views
path = os.path.join(parent_dir, 'uploads')

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@api.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename, ALLOWED_AUDIO_EXTENSIONS):
        filename = secure_filename(file.filename)
        filepath = os.path.join(path, filename)
        file.save(filepath)
        return jsonify({'message': 'Audio file uploaded successfully!', 'filename': filename}), 201
    else:
        return jsonify({'error': 'Allowed audio file types are wav, mp3'}), 400

@api.route('/upload-photo', methods=['POST'])
def upload_photo():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename, ALLOWED_PHOTO_EXTENSIONS):
        filename = secure_filename(file.filename)
        filepath = os.path.join(path, filename)
        file.save(filepath)
        return jsonify({'message': 'Video file uploaded successfully!', 'filename': filename}), 201
    else:
        return jsonify({'error': 'Allowed video file types are mp4, mov, avi'}), 400

# User API

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users]), 200


@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200


@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'message': 'User created successfully!'}), 201


@api.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({'id': user.id, 'message': 'User updated successfully!'}), 200


@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'}), 200


# Artist API

@api.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    return jsonify([{'id': artist.id, 'user_id': artist.user_id, 'name': artist.name} for artist in artists]), 200


@api.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    return jsonify({'id': artist.id, 'user_id': artist.user_id, 'name': artist.name}), 200


@api.route('/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    artist = Artist(user_id=data['user_id'], name=data['name'])
    db.session.add(artist)
    db.session.commit()
    return jsonify({'id': artist.id, 'message': 'Artist created successfully!'}), 201


@api.route('/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    data = request.get_json()
    artist.user_id = data.get('user_id', artist.user_id)
    artist.name = data.get('name', artist.name)
    db.session.commit()
    return jsonify({'id': artist.id, 'message': 'Artist updated successfully!'}), 200


@api.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    db.session.delete(artist)
    db.session.commit()
    return jsonify({'message': 'Artist deleted successfully!'}), 200


# Album API

@api.route('/albums', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    return jsonify([{'id': album.id, 'user_id': album.user_id, 'title': album.title} for album in albums]), 200


@api.route('/albums/<int:album_id>', methods=['GET'])
def get_album(album_id):
    album = Album.query.get_or_404(album_id)
    return jsonify({'id': album.id, 'user_id': album.user_id, 'title': album.title}), 200


@api.route('/albums', methods=['POST'])
def create_album():
    data = request.get_json()
    album = Album(
        user_id=data['user_id'],
        artwork=data['artwork'],
        title=data['title'],
        type=data['type'],
        primary_artist1=data['primary_artist1'],
        primary_artist2=data.get('primary_artist2'),
        primary_artist3=data.get('primary_artist3'),
        featuring_artist1=data.get('featuring_artist1'),
        featuring_artist2=data.get('featuring_artist2'),
        featuring_artist3=data.get('featuring_artist3'),
        genre=data['genre'],
        sub_genre=data['sub_genre'],
        label_name=data['label_name'],
        release_date=data['release_date'],
        p_line=data['p_line'],
        c_line=data['c_line'],
        upc_ean=data.get('upc_ean')
    )
    db.session.add(album)
    db.session.commit()
    return jsonify({'id': album.id, 'message': 'Album created successfully!'}), 201


@api.route('/albums/<int:album_id>', methods=['PUT'])
def update_album(album_id):
    album = Album.query.get_or_404(album_id)
    data = request.get_json()
    album.user_id = data.get('user_id', album.user_id)
    album.artwork = data.get('artwork', album.artwork)
    # ... update other fields ...
    db.session.commit()
    return jsonify({'id': album.id, 'message': 'Album updated successfully!'}), 200


@api.route('/albums/<int:album_id>', methods=['DELETE'])
def delete_album(album_id):
    album = Album.query.get_or_404(album_id)
    db.session.delete(album)
    db.session.commit()
    return jsonify({'message': 'Album deleted successfully!'}), 200


# Song API

@api.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    return jsonify([{'id': song.id, 'album_id': song.album_id, 'title': song.title} for song in songs]), 200


@api.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song = Song.query.get_or_404(song_id)
    return jsonify({'id': song.id, 'album_id': song.album_id, 'title': song.title}), 200


@api.route('/songs', methods=['POST'])
def create_song():
    data = request.get_json()
    song = Song(
        album_id=data['album_id'],
        track=data['track'],
        version=data['version'],
        instrumental=data['instrumental'],
        title=data['title'],
        subtitle=data['subtitle'],
        primary_artist1=data['primary_artist1'],
        primary_artist2=data.get('primary_artist2'),
        primary_artist3=data.get('primary_artist3'),
        featuring_artist1=data.get('featuring_artist1'),
        featuring_artist2=data.get('featuring_artist2'),
        featuring_artist3=data.get('featuring_artist3'),
        author=data['author'],
        composer=data['composer'],
        producer=data['producer'],
        p_line=data['p_line'],
        production_year=data['production_year'],
        publisher=data['publisher'],
        isrc=data.get('isrc'),
        genre=data['genre'],
        subgenre=data['subgenre'],
        explicit=data['explicit'],
        title_language=data['title_language'],
        lyrics_language=data['lyrics_language'],
        lyrics=data.get('lyrics'),
        caller_tune=data.get('caller_tune')
    )
    db.session.add(song)
    db.session.commit()
    return jsonify({'id': song.id, 'message': 'Song created successfully!'}), 201


@api.route('/songs/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    song = Song.query.get_or_404(song_id)
    data = request.get_json()
    song.album_id = data.get('album_id', song.album_id)
    song.track = data.get('track', song.track)
    # ... update other fields ...
    db.session.commit()
    return jsonify({'id': song.id, 'message': 'Song updated successfully!'}), 200


@api.route('/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    db.session.delete(song)
    db.session.commit()
    return jsonify({'message': 'Song deleted successfully!'}), 200


# Store API

@api.route('/stores', methods=['GET'])
def get_stores():
    stores = Store.query.all()
    return jsonify([{'id': store.id, 'song_id': store.song_id, 'store_name': store.store_name} for store in stores]), 200


@api.route('/stores/<int:store_id>', methods=['GET'])
def get_store(store_id):
    store = Store.query.get_or_404(store_id)
    return jsonify({'id': store.id, 'song_id': store.song_id, 'store_name': store.store_name}), 200


@api.route('/stores', methods=['POST'])
def create_store():
    data = request.get_json()
    store = Store(song_id=data['song_id'], store_name=data['store_name'])
    db.session.add(store)
    db.session.commit()
    return jsonify({'id': store.id, 'message': 'Store created successfully!'}), 201


@api.route('/stores/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    store = Store.query.get_or_404(store_id)
    data = request.get_json()
    store.song_id = data.get('song_id', store.song_id)
    store.store_name = data.get('store_name', store.store_name)
    db.session.commit()
    return jsonify({'id': store.id, 'message': 'Store updated successfully!'}), 200


@api.route('/stores/<int:store_id>', methods=['DELETE'])
def delete_store(store_id):
    store = Store.query.get_or_404(store_id)
    db.session.delete(store)
    db.session.commit()
    return jsonify({'message': 'Store deleted successfully!'}), 200


# Post API

@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]), 200


@api.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content}), 200


@api.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = Post(title=data['title'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'id': post.id, 'message': 'Post created successfully!'}), 201


@api.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify({'id': post.id, 'message': 'Post updated successfully!'}), 200


@api.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully!'}), 200


# Report API

@api.route('/reports', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    return jsonify([{'id': report.id, 'user_id': report.user_id, 'report_for': report.report_for} for report in reports]), 200


@api.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    report = Report.query.get_or_404(report_id)
    return jsonify({'id': report.id, 'user_id': report.user_id, 'report_for': report.report_for}), 200


@api.route('/reports', methods=['POST'])
def create_report():
    data = request.get_json()
    report = Report(user_id=data['user_id'], report_for=data['report_for'], start_date=data['start_date'], end_date=data['end_date'])
    db.session.add(report)
    db.session.commit()
    return jsonify({'id': report.id, 'message': 'Report created successfully!'}), 201


@api.route('/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    report = Report.query.get_or_404(report_id)
    data = request.get_json()
    report.user_id = data.get('user_id', report.user_id)
    report.report_for = data.get('report_for', report.report_for)
    # ... update other fields ...
    db.session.commit()
    return jsonify({'id': report.id, 'message': 'Report updated successfully!'}), 200


@api.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    report = Report.query.get_or_404(report_id)
    db.session.delete(report)
    db.session.commit()
    return jsonify({'message': 'Report deleted successfully!'}), 200


# Ticket API

@api.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([{'id': ticket.id, 'user_id': ticket.user_id, 'reason': ticket.reason} for ticket in tickets]), 200


@api.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    return jsonify({'id': ticket.id, 'user_id': ticket.user_id, 'reason': ticket.reason}), 200


@api.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    ticket = Ticket(user_id=data['user_id'], reason=data['reason'])
    db.session.add(ticket)
    db.session.commit()
    return jsonify({'id': ticket.id, 'message': 'Ticket created successfully!'}), 201


@api.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.get_json()
    ticket.user_id = data.get('user_id', ticket.user_id)
    ticket.reason = data.get('reason', ticket.reason)
    # ... update other fields ...
    db.session.commit()
    return jsonify({'id': ticket.id, 'message': 'Ticket updated successfully!'}), 200


@api.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket deleted successfully!'}), 200


# Message API

@api.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([{'id': message.id, 'author_id': message.author_id, 'ticket_id': message.ticket_id, 'message': message.message} for message in messages]), 200


@api.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.query.get_or_404(message_id)
    return jsonify({'id': message.id, 'author_id': message.author_id, 'ticket_id': message.ticket_id, 'message': message.message}), 200


@api.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    message = Message(author_id=data['author_id'], ticket_id=data['ticket_id'], message=data['message'], attachment=data.get('attachment'))
    db.session.add(message)
    db.session.commit()
    return jsonify({'id': message.id, 'message': 'Message created successfully!'}), 201


@api.route('/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    message = Message.query.get_or_404(message_id)
    data = request.get_json()
    message.author_id = data.get('author_id', message.author_id)
    message.ticket_id = data.get('ticket_id', message.ticket_id)
    message.message = data.get('message', message.message)
    message.attachment = data.get('attachment', message.attachment)
    db.session.commit()
    return jsonify({'id': message.id, 'message': 'Message updated successfully!'}), 200


@api.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message deleted successfully!'}), 200


# Ugc API

@api.route('/ugcs', methods=['GET'])
def get_ugcs():
    ugcs = Ugc.query.all()
    return jsonify([{'id': ugc.id, 'user_id': ugc.user_id, 'release_title': ugc.release_title} for ugc in ugcs]), 200


@api.route('/ugcs/<int:ugc_id>', methods=['GET'])
def get_ugc(ugc_id):
    ugc = Ugc.query.get_or_404(ugc_id)
    return jsonify({'id': ugc.id, 'user_id': ugc.user_id, 'release_title': ugc.release_title}), 200


@api.route('/ugcs', methods=['POST'])
def create_ugc():
    data = request.get_json()
    ugc = Ugc(user_id=data['user_id'], release_title=data['release_title'], audio_title=data['audio_title'], policy=data['policy'], url=data['url'])
    db.session.add(ugc)
    db.session.commit()
    return jsonify({'id': ugc.id, 'message': 'Ugc created successfully!'}), 201


@api.route('/ugcs/<int:ugc_id>', methods=['PUT'])
def update_ugc(ugc_id):
    ugc = Ugc.query.get_or_404(ugc_id)
    data = request.get_json()
    ugc.user_id = data.get('user_id', ugc.user_id)
    ugc.release_title = data.get('release_title', ugc.release_title)
    # ... update other fields ...
    db.session.commit()
    return jsonify({'id': ugc.id, 'message': 'Ugc updated successfully!'}), 200


@api.route('/ugcs/<int:ugc_id>', methods=['DELETE'])
def delete_ugc(ugc_id):
    ugc = Ugc.query.get_or_404(ugc_id)
    db.session.delete(ugc)
    db.session.commit()
    return jsonify({'message': 'Ugc deleted successfully!'}), 200


# Profilelinking API

@api.route('/profilelinkings', methods=['GET'])
def get_profilelinkings():
    profilelinkings = Profilelinking.query.all()
    return jsonify([{'id': profilelinking.id, 'user_id': profilelinking.user_id, 'release_title': profilelinking.release_title} for profilelinking in profilelinkings]), 200


@api.route('/profilelinkings/<int:profilelinking_id>', methods=['GET'])
def get_profilelinking(profilelinking_id):
    profilelinking = Profilelinking.query.get_or_404(profilelinking_id)
    return jsonify({'id': profilelinking.id, 'user_id': profilelinking.user_id, 'release_title': profilelinking.release_title}), 200


@api.route('/profilelinkings', methods=['POST'])
def create_profilelinking():
    data = request.get_json()
    profilelinking = Profilelinking(user_id=data['user_id'], release_title=data['release_title'], audio_title=data['audio_title'], artist=data['artist'], fb=data['fb'], ig=data['ig'])
    db.session.add(profilelinking)
    db.session.commit()
    return jsonify({'id': profilelinking.id, 'message': 'Profilelinking created successfully!'}), 201


@api.route('/profilelinkings/<int:profilelinking_id>', methods=['PUT'])
def update_profilelinking(profilelinking_id):
    profilelinking = Profilelinking.query.get_or_404(profilelinking_id)
    data = request.get_json()
    profilelinking.user_id = data.get('user_id', profilelinking.user_id)
    profilelinking.release_title = data.get('release_title', profilelinking.release_title)
    # ... update other fields ...
    db.session.commit()
    return jsonify({'id': profilelinking.id, 'message': 'Profilelinking updated successfully!'}), 200


@api.route('/profilelinkings/<int:profilelinking_id>', methods=['DELETE'])
def delete_profilelinking(profilelinking_id):
    profilelinking = Profilelinking.query.get_or_404(profilelinking_id)
    db.session.delete(profilelinking)
    db.session.commit()
    return jsonify({'message': 'Profilelinking deleted successfully!'}), 200


# Distributelyrics API

@api.route('/distributelyrics', methods=['GET'])
def get_distributelyrics():
    distributelyrics = Distributelyrics.query.all()
    return jsonify([{'id': distributelyric.id, 'user_id': distributelyric.user_id, 'release_title': distributelyric.release_title} for distributelyric in distributelyrics]), 200


@api.route('/distributelyrics/<int:distributelyric_id>', methods=['GET'])
def get_distributelyric(distributelyric_id):
    distributelyric = Distributelyrics.query.get_or_404(distributelyric_id)
    return jsonify({'id': distributelyric.id, 'user_id': distributelyric.user_id, 'release_title': distributelyric.release_title}), 200


@api.route('/distributelyrics', methods=['POST'])
def create_distributelyric():
    data = request.get_json()
    distributelyric = Distributelyrics(user_id=data['user_id'], release_title=data['release_title'], audio_title=data['audio_title'], language=data['language'], lyrics=data['lyrics'])
    db.session.add(distributelyric)
    db.session.commit()
    return jsonify({'id': distributelyric.id, 'message': 'Distributelyric created successfully!'}), 201


@api.route('/distributelyrics/<int:distributelyric_id>', methods=['PUT'])
def update_distributelyric(distributelyric_id):
    distributelyric = Distributelyrics.query.get_or_404(distributelyric_id)
    data = request.get_json()
    distributelyric.user_id = data.get('user_id', distributelyric.user_id)
    distributelyric.release_title = data.get('release_title', distributelyric.release_title)
    # ... update other fields ...
    db.session.commit()
    return jsonify({'id': distributelyric.id, 'message': 'Distributelyric updated successfully!'}), 200


@api.route('/distributelyrics/<int:distributelyric_id>', methods=['DELETE'])
def delete_distributelyric(distributelyric_id):
    distributelyric = Distributelyrics.query.get_or_404(distributelyric_id)
    db.session.delete(distributelyric)
    db.session.commit()
    return jsonify({'message': 'Distributelyric deleted successfully!'}), 200