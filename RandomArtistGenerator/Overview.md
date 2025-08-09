# 🎵 Random Artist Generator  

Lately, I noticed I kept listening to the same handful of songs over and over. It became repetitive, uninspiring, and—frankly—a little boring.  

I wanted an easy way to break out of that routine, discover new artists, and keep my playlists feeling fresh—without spending extra time deciding what to play each day.  

That’s what inspired me to create the **Random Artist Generator**—a fun Python application that uses the Spotify Web API to suggest new artists, show their details, and save them in a local database. It’s like a personal music discovery assistant that removes the guesswork from daily listening.  

---

## ✨ Features  

- **Random Artist Generation** – Pulls a random artist from Spotify with a popularity score above 60.  
- **Artist Details** – Shows the artist’s name, popularity, genres, and a clickable Spotify link.  
- **Database Storage** – Saves every discovered artist in a local SQLite database.  
- **Duplicate Prevention** – Ensures no artist is repeated.  
- **View All Artists** – Displays all saved artists with their details.  
- **Clear Database** – Wipe stored artists in one click (or command).  

---

## 🖥️ Two Modes of Use  

- **GUI** (`app_ui.py`) – A simple Tkinter interface with buttons and a scrollable display.  
- **CLI** (`main.py`) – A lightweight, interactive terminal-based version.  

---

## 🛠️ Tech Stack  

- **Python** – Core programming language  
- **Tkinter** – GUI framework  
- **SQLite** – Local database storage  
- **Spotipy** – Python wrapper for the Spotify Web API  
- **dotenv** – Loads API credentials from `.env`  

---

## 🚀 How It Works  

1. **Spotify API Connection** – Uses the Spotipy library with your Spotify API credentials.  
2. **Random Search** – Selects a random letter, fetches 50 artists, and filters for popularity > 60.  
3. **Display & Save** – Shows the artist’s details and saves them to `artists.db`.  
4. **Avoid Repeats** – Skips any artist already stored in the database.  

---

## 🔧 Setup & Run  

### 1. Install dependencies:
  pip install spotipy python-dotenv

### 2. Create a .env file with your Spotify API credentials:
SPOTIPY_CLIENT_ID=your_client_id  
SPOTIPY_CLIENT_SECRET=your_client_secret  
SPOTIPY_REDIRECT_URI=your_redirect_uri

### 3. Run the GUI version:
python app_ui.py

### 4. Run the CLI version:
python main.py

---

## 🚧 Future Plans  

This project is still in its early stages, and I’m excited to expand its capabilities.  
Some upcoming ideas include:  

- [ ] Genre filter with checkboxes to discover artists from specific styles  
- [ ] Album randomizer mode  
- [ ] Improved and more polished UI  
- [ ] Mobile-friendly version  
- [ ] Integration with my Spotify listening history to make personalized suggestions 


