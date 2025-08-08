import sqlite3

DB_NAME = 'artists.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS artists (
            id TEXT PRIMARY KEY,
            name TEXT,
            popularity INTEGER,
            genres TEXT,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def artist_exists(artist_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT 1 FROM artists WHERE id = ?', (artist_id,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

def save_artist(artist):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO artists (id, name, popularity, genres, url)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        artist['id'],
        artist['name'],
        artist['popularity'],
        ', '.join(artist['genres']),
        artist['url']
    ))
    conn.commit()
    conn.close()
