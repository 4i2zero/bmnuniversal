from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin


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

    def __repr__(self):
        return f"User('{self.email}', '{self.name}', '{self.is_admin}', '{self.phone}', '{self.revenue}')"


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=False, nullable=False)
    artist_name = db.Column(db.String(200), nullable=False)
    spotify_id = db.Column(db.String(250), nullable=True)
    apple_id = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"Artist('{self.name}', '{self.email}', '{self.spotify_id}', '{self.apple_id}')"


class Releaseinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=False, nullable=False)
    album_artwork = db.Column(db.String(250), nullable=False)
    release_title = db.Column(db.String(250), nullable=False)
    release_type = db.Column(db.String(250), nullable=False)
    primary_artist1 = db.Column(db.String(250), nullable=False)
    primary_artist2 = db.Column(db.String(250), nullable=True)
    primary_artist3 = db.Column(db.String(250), nullable=True)
    featuring1 = db.Column(db.String(250), nullable=True)
    featuring2 = db.Column(db.String(250), nullable=True)
    featuring3 = db.Column(db.String(250), nullable=True)
    genre = db.Column(db.String(250), nullable=False)
    sub_genre = db.Column(db.String(250), nullable=False)
    lable_name = db.Column(db.String(250), nullable=False)
    release_date = db.Column(db.String(250), nullable=False)
    p_line = db.Column(db.String(250), nullable=False)
    c_line = db.Column(db.String(250), nullable=False)
    upc_ean = db.Column(db.String(250), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Releaseinfo('{self.id}' ,'{self.email}', '{self.album_artwork}', '{self.release_title}', '{self.release_type}', '{self.primary_artist1}', '{self.primary_artist2}', '{self.primary_artist3}', '{self.featuring1}', '{self.featuring2}', '{self.featuring3}', '{self.genre}', '{self.sub_genre}', '{self.lable_name}', '{self.release_date}', '{self.p_line}', '{self.c_line}', '{self.upc_ean}', '{self.created_on}')"


class Songinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=False, nullable=False)
    release_id = db.Column(db.String(250), unique=False, nullable=False)
    audio_track = db.Column(db.String(250), nullable=False)
    track_version = db.Column(db.String(250), nullable=False)
    instrumental = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    version_subtitle = db.Column(db.String(250), nullable=False)
    primary_artist1 = db.Column(db.String(250), nullable=False)
    primary_artist2 = db.Column(db.String(250), nullable=True)
    primary_artist3 = db.Column(db.String(250), nullable=True)
    featuring1 = db.Column(db.String(250), nullable=True)
    featuring2 = db.Column(db.String(250), nullable=True)
    featuring3 = db.Column(db.String(250), nullable=True)
    author1 = db.Column(db.String(250), nullable=False)
    author2 = db.Column(db.String(250), nullable=True)
    author3 = db.Column(db.String(250), nullable=True)
    composer1 = db.Column(db.String(250), nullable=False)
    composer2 = db.Column(db.String(250), nullable=True)
    composer3 = db.Column(db.String(250), nullable=True)
    producer = db.Column(db.String(250), nullable=False)
    p_line = db.Column(db.String(250), nullable=False)
    production_year = db.Column(db.String(250), nullable=False)
    publisher = db.Column(db.String(250), nullable=False)
    isrc_yes_no = db.Column(db.String(250), nullable=False)
    isrc = db.Column(db.String(250), nullable=True)
    genre = db.Column(db.String(250), nullable=False)
    subgenre = db.Column(db.String(250), nullable=False)
    price_tier = db.Column(db.String(250), nullable=False)
    explicit_version = db.Column(db.String(250), nullable=False)
    track_title_language = db.Column(db.String(250), nullable=False)
    lyrics_language = db.Column(db.String(250), nullable=False)
    lyrics = db.Column(db.String(250), nullable=False)
    caller_tune = db.Column(db.String(250), nullable=False)
    destribute_music = db.Column(db.String(250), nullable=True)
    video_isrc = db.Column(db.String(250), nullable=True)
    download_video_link = db.Column(db.String(250), nullable=True)
    saved = db.Column(db.String(250), nullable=True)
    edit = db.Column(db.String(250), nullable=True)
    selectedSongPrimaryArtist = db.Column(db.String(250), nullable=False)
    selectedSongfeaturingArtist = db.Column(db.String(250), nullable=True)
    selectedSongAuthor = db.Column(db.String(250), nullable=True)
    selectedSongComposer = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"Songinfo('{self.id}', '{self.email}', '{self.release_id}', '{self.audio_track}', '{self.track_version}', '{self.instrumental}', '{self.title}', '{self.version_subtitle}', '{self.primary_artist1}', '{self.primary_artist2}', '{self.primary_artist3}', '{self.featuring1}', '{self.featuring2}', '{self.featuring3}', '{self.author1}', '{self.author2}', '{self.author3}', '{self.composer1}', '{self.composer2}', '{self.composer3}', '{self.producer}', '{self.p_line}', '{self.production_year}', '{self.publisher}', '{self.isrc_yes_no}', '{self.isrc}', '{self.genre}', '{self.subgenre}', '{self.price_tier}', '{self.explicit_version}', '{self.track_title_language}', '{self.lyrics_language}', '{self.lyrics}', '{self.caller_tune}', '{self.destribute_music}', '{self.video_isrc}', '{self.download_video_link}', '{self.saved}', '{self.edit}', '{self.selectedSongPrimaryArtist}', '{self.selectedSongfeaturingArtist}', '{self.selectedSongAuthor}', '{self.selectedSongComposer}')"
