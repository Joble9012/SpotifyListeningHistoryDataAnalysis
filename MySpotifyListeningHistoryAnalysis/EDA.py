import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your cleaned CSV
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

# Extract date-related info
df['date'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()

# --- Descriptive Stats ---
print("\n📊 Descriptive Statistics for Listening Time:")
print(df['seconds_played'].describe())

# --- Top artists ---
top_artists = df['artist_name'].value_counts().head(10)
print("\n🎤 Top 10 Artists:")
print(top_artists)

# --- Top tracks ---
top_tracks = df['track_name'].value_counts().head(10)
print("\n🎵 Top 10 Tracks:")
print(top_tracks)

# --- Total listening time ---
total_hours = df['seconds_played'].sum() / 3600
print(f"\n⏱️ Total Listening Time: {total_hours:.2f} hours")

# --- Plays by Hour ---
plt.figure(figsize=(10, 4))
sns.countplot(x='hour', data=df, palette='viridis')
plt.title("Listening Activity by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Plays")
plt.tight_layout()
plt.show()

# --- Plays by Day of Week ---
plt.figure(figsize=(8, 4))
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(x='day_of_week', data=df, order=order, palette='Set2')
plt.title("Listening Activity by Day of Week")
plt.xlabel("Day")
plt.ylabel("Plays")
plt.tight_layout()
plt.show()

# --- Most played tracks by time spent ---
most_played_by_time = df.groupby('track_name')['seconds_played'].sum().sort_values(ascending=False).head(10)
print("\n🎧 Top 10 Tracks by Listening Time (seconds):")
print(most_played_by_time)

