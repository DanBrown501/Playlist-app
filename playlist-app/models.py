"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    def __repr__(self):
        """Show info about playlist."""

        p = self
        return f"<Playlist id={p.id} name={p.name}>"

    __tablename__ = "playlists"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    description = db.Column(db.Text, nullable=True)




class Song(db.Model):
    def __repr__(self):
        """Show info about song."""

        p = self
        return f"<Song id={p.id} name={p.title}>"

    playlists = db.relationship('Playlist', secondary='playlist_songs', backref='songs')

    __tablename__ = "songs"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    title = db.Column(db.Text, nullable=False)

    artist = db.Column(db.Text, nullable=False)




class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'

    def __repr__(self):
        """Show info about playlist-song table."""

        p = self
        return f"<Playlist_song playlist-id={p.playlist_id} song-id={p.song_id}>"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), primary_key=True, nullable=False)

    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True, nullable=False)



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)