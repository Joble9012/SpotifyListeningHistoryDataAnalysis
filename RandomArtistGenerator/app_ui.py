import tkinter as tk
from tkinter import messagebox, scrolledtext
import webbrowser

from spotify_client import get_random_artist
from artist_db import create_table, artist_exists, save_artist

# Initialize DB
create_table()

# UI App
class ArtistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Music Artist Generator 🎵")

        # Generate Button
        self.generate_btn = tk.Button(root, text="🎧 Generate Artist", command=self.generate_artist)
        self.generate_btn.pack(pady=10)

        # Artist Display Box
        self.artist_box = tk.Text(root, height=8, width=60, wrap=tk.WORD)
        self.artist_box.pack(padx=10, pady=5)

        # View All Button
        self.view_btn = tk.Button(root, text="📃 View All Saved Artists", command=self.view_artists)
        self.view_btn.pack(pady=5)

        # Clear DB Button
        self.clear_btn = tk.Button(root, text="🗑️ Clear Database", command=self.clear_database)
        self.clear_btn.pack(pady=5)

        # Quit Button
        self.quit_btn = tk.Button(root, text="❌ Quit", command=root.quit)
        self.quit_btn.pack(pady=10)

    def generate_artist(self):
        self.artist_box.delete(1.0, tk.END)
        for _ in range(10):  # Try 10 times to get a new artist
            artist = get_random_artist()
            if artist and not artist_exists(artist["id"]):
                save_artist(artist)
                self.show_artist_info(artist)
                return
        self.artist_box.insert(tk.END, "❌ No new artist found. Try again.")

    def show_artist_info(self, artist):
        info = f"🎤 Name: {artist['name']}\n"
        info += f"🔥 Popularity: {artist['popularity']}\n"
        info += f"🎧 Genres: {', '.join(artist['genres']) or 'Unknown'}\n"
        info += f"🔗 Link: {artist['url']}\n"
        self.artist_box.insert(tk.END, info)

        # Make URL clickable
        def open_link(event):
            webbrowser.open(artist['url'])

        self.artist_box.tag_config("url", foreground="blue", underline=1)
        self.artist_box.insert(tk.END, "\nClick to open artist page", "url")
        self.artist_box.tag_bind("url", "<Button-1>", open_link)

    def view_artists(self):
        import sqlite3
        conn = sqlite3.connect('artists.db')
        c = conn.cursor()
        c.execute('SELECT name, popularity FROM artists')
        rows = c.fetchall()
        conn.close()

        view_window = tk.Toplevel(self.root)
        view_window.title("All Saved Artists")
        text_area = scrolledtext.ScrolledText(view_window, wrap=tk.WORD, width=60, height=20)
        text_area.pack(padx=10, pady=10)

        if not rows:
            text_area.insert(tk.END, "No artists saved yet.")
        else:
            for idx, (name, popularity) in enumerate(rows, 1):
                text_area.insert(tk.END, f"{idx}. {name} (🔥 {popularity})\n")

    def clear_database(self):
        answer = messagebox.askyesno("Clear Database", "⚠️ Are you sure you want to delete all saved artists?")
        if answer:
            import sqlite3
            conn = sqlite3.connect('artists.db')
            c = conn.cursor()
            c.execute('DELETE FROM artists')
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "✅ Database cleared.")

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ArtistApp(root)
    root.mainloop()
