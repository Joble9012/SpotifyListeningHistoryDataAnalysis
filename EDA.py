import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to CleanData.csv
data_path = "/Users/joblethomas/Projects/MySpotifyListeningHistoryAnalysis/CleanData.csv"

# Load the data
df = pd.read_csv(data_path)

# Basic overview
print("📌 Basic Info:")
print(df.info())
print("\n📌 First few rows:")
print(df.head())
print("\n📌 Missing Values:")
print(df.isnull().sum())

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# --- Descriptive Stats ---
print("\n📊 Descriptive Statistics for Listening Time:")
print(df['minutes_played'].describe())

# --- Top artists ---
top_artists = df['artist_name'].value_counts().head(10)
print("\n🎤 Top 10 Artists:")
print(top_artists)

# --- Top tracks ---
top_tracks = df['track_name'].value_counts().head(10)
print("\n🎵 Top 10 Tracks:")
print(top_tracks)

# --- Total listening time ---
total_hours = df['minutes_played'].sum() / 3600
print(f"\n⏱️ Total Listening Time: {total_hours:.2f} hours")

# --- Most played tracks by time spent ---
most_played_by_time = df.groupby('track_name')['minutes_played'].sum().sort_values(ascending=False).head(10)
print("\n🎧 Top 10 Tracks by Listening Time (minutes):")
print(most_played_by_time)

