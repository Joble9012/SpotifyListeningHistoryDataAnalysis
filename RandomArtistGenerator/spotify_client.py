import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_random_artist(exclude_ids=set()):
    tries = 0
    while tries < 10:
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        results = sp.search(q=letter, type='artist', limit=50)
        artists = results['artists']['items']
        popular_artists = [
            artist for artist in artists 
            if artist['popularity'] > 60 and artist['id'] not in exclude_ids
        ]

        if not popular_artists:
            tries += 1
            continue

        artist = random.choice(popular_artists)
        return {
            "id": artist['id'],
            "name": artist['name'],
            "popularity": artist['popularity'],
            "genres": artist['genres'],
            "url": artist['external_urls']['spotify']
        }

    return None

def get_available_genres(sp: spotipy.Spotify = None):
    if not sp:
        sp = get_spotify_client()
    return sp.recommendation_genre_seeds()
