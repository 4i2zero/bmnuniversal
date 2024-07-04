from datetime import datetime
from .extensions import db, login_manager
from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    revenue = db.Column(db.String(20), default='0')
    is_admin = db.Column(db.Boolean, default=False)
    image_file = db.Column(db.String(20), nullable=False, default='/static/img/profile.jpg')
    artists = relationship('Artist', backref='user_artist', lazy='dynamic')
    albums = relationship('Album', backref='user_album', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.name}', '{self.is_admin}', '{self.phone}', '{self.revenue}', '{self.image_file}')"


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    spotify_id = db.Column(db.String(250), nullable=True)
    apple_id = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"Artist('{self.id}', '{self.artist_name}', '{self.spotify_id}', '{self.apple_id}')"


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    artwork = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)
    primary_artist1 = db.Column(db.String(250), nullable=False)
    primary_artist2 = db.Column(db.String(250), nullable=True)
    primary_artist3 = db.Column(db.String(250), nullable=True)
    featuring_artist1 = db.Column(db.String(250), nullable=True)
    featuring_artist2 = db.Column(db.String(250), nullable=True)
    featuring_artist3 = db.Column(db.String(250), nullable=True)
    genre = db.Column(db.String(250), nullable=False)
    sub_genre = db.Column(db.String(250), nullable=False)
    label_name = db.Column(db.String(250), nullable=False)
    release_date = db.Column(db.String(250), nullable=False)
    p_line = db.Column(db.String(250), nullable=False)
    c_line = db.Column(db.String(250), nullable=False)
    upc_ean = db.Column(db.String(250), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    songs = relationship('Song', backref='album_song', lazy=True)

    def __repr__(self):
        return f"Album('{self.id}', '{self.artwork}', '{self.title}', '{self.type}', '{self.primary_artist1}', '{self.primary_artist2}', '{self.primary_artist3}', '{self.featuring_artist1}', '{self.featuring_artist2}', '{self.featuring_artist3}', '{self.genre}', '{self.sub_genre}', '{self.label_name}', '{self.release_date}', '{self.p_line}', '{self.c_line}', '{self.upc_ean}', '{self.created_on}')"
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, ForeignKey('album.id'), nullable=False)
    track = db.Column(db.String(250), nullable=False)
    version = db.Column(db.String(250), nullable=False)
    instrumental = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    primary_artist1 = db.Column(db.String(250), nullable=False)
    primary_artist2 = db.Column(db.String(250), nullable=True)
    primary_artist3 = db.Column(db.String(250), nullable=True)
    featuring_artist1 = db.Column(db.String(250), nullable=True)
    featuring_artist2 = db.Column(db.String(250), nullable=True)
    featuring_artist3 = db.Column(db.String(250), nullable=True)
    author = db.Column(db.String(250), nullable=False)
    composer = db.Column(db.String(250), nullable=False)
    producer = db.Column(db.String(250), nullable=False)
    p_line = db.Column(db.String(250), nullable=False)
    production_year = db.Column(db.String(250), nullable=False)
    publisher = db.Column(db.String(250), nullable=False)
    isrc = db.Column(db.String(250), nullable=True)
    genre = db.Column(db.String(250), nullable=False)
    subgenre = db.Column(db.String(250), nullable=False)
    explicit = db.Column(db.Boolean, nullable=False)
    title_language = db.Column(db.String(250), nullable=False)
    lyrics_language = db.Column(db.String(250), nullable=False)
    lyrics = db.Column(db.String(250), nullable=True)
    caller_tune = db.Column(db.String(250), nullable=True)
    status = db.Column(db.String(250), default='Pending Approval')
    stores = relationship('Store', backref='song_store', lazy=True)

    def __repr__(self):
        return f"Song('{self.id}', '{self.track}', '{self.version}', '{self.instrumental}', '{self.title}', '{self.subtitle}', '{self.primary_artist1}', '{self.primary_artist2}', '{self.primary_artist3}', '{self.featuring_artist1}', '{self.featuring_artist2}', '{self.featuring_artist3}', '{self.author}', '{self.composer}', '{self.producer}', '{self.p_line}', '{self.production_year}', '{self.publisher}', '{self.isrc}', '{self.genre}', '{self.subgenre}', '{self.explicit}', '{self.title_language}', '{self.lyrics_language}', '{self.lyrics}', '{self.caller_tune}', '{self.status}')"


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, ForeignKey('song.id'), nullable=False)
    store_name = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), default='Pending Approval')
    url = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"Store('{self.id}', '{self.store_name}', '{self.status}', '{self.url}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    tags = db.Column(db.String(250), nullable=False)
    img = db.Column(db.String(250), nullable=True)
    meta_title = db.Column(db.String(100), nullable=False)
    meta_description = db.Column(db.String(250), nullable=False)
    meta_keywords = db.Column(db.String(250), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.slug}', '{self.tags}', '{self.img}', '{self.content}')"
    
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    report_for = db.Column(db.String(250), nullable=False)
    start_date = db.Column(db.String(250), nullable=False)
    end_date = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), default='Pending Approval')

    def __repr__(self):
        return f"Report('{self.id}', '{self.user_id}', '{self.report_for}', '{self.start_date}', '{self.end_date}', '{self.status}')"
    

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    reason = db.Column(db.String(250), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(250), default='Pending')
    messages = relationship('Message', backref='ticket_message', lazy=True)

    def __repr__(self):
        return f"Ticket('{self.id}', '{self.user_id}', '{self.reason}', '{self.created_on}', '{self.status}')"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    ticket_id = db.Column(db.Integer, ForeignKey('ticket.id'), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    attachment = db.Column(db.String(250), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Message('{self.id}', '{self.author_id}', '{self.ticket_id}', '{self.message}', '{self.attachment}', '{self.created_on}')"
    
class Ugc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    release_title = db.Column(db.String(250), nullable=False)
    audio_title =  db.Column(db.String(250), nullable=False)
    policy =  db.Column(db.String(250), nullable=False)
    url =  db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), default='Pending')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Ugc('{self.id}', '{self.user_id}', '{self.release_title}', '{self.audio_title}', '{self.policy}', '{self.url}', '{self.status}', '{self.date}')"

class Profilelinking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    release_title = db.Column(db.String(250), nullable=False)
    audio_title =  db.Column(db.String(250), nullable=False)
    artist =  db.Column(db.String(250), nullable=False)
    fb =  db.Column(db.String(250), nullable=False)
    ig =  db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), default='Pending')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Profilelinking('{self.id}', '{self.user_id}', '{self.release_title}', '{self.audio_title}', '{self.artist}', '{self.fb}', '{self.ig}', '{self.status}', '{self.date}')"

class Distributelyrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    release_title = db.Column(db.String(250), nullable=False)
    audio_title =  db.Column(db.String(250), nullable=False)
    language = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), default='Pending')
    lyrics = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Distributelyrics('{self.id}','{self.user_id}', '{self.release_title}', '{self.audio_title}','{self.language}','{self.status}','{self.details}','{self.date}')"

