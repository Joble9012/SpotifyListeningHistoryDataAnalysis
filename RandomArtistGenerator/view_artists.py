import sqlite3

DB_NAME = 'artists.db'

def list_all_artists():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT name, popularity, genres, url FROM artists')
    rows = c.fetchall()
    conn.close()

    if not rows:
        print("No artists found in the database.")
        return

    print("\n🎼 Saved Artists:")
    for idx, row in enumerate(rows, 1):
        name, popularity, genres, url = row
        print(f"{idx}. {name}")
        print(f"   🔥 Popularity: {popularity}")
        print(f"   🎧 Genres: {genres}")
        print(f"   🔗 Link: {url}\n")

if __name__ == "__main__":
    list_all_artists()
