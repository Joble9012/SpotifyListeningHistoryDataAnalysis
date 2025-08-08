from spotify_client import get_random_artist
from artist_db import create_table, artist_exists, save_artist

def main():
    create_table()
    print("🎵 Welcome to the Random Music Artist Generator 🎵")

    while True:
        user_input = input("\nDo you want to generate a random artist? (yes/no): ").strip().lower()

        if user_input == "yes":
            for _ in range(10):
                artist = get_random_artist()
                if artist and not artist_exists(artist['id']):
                    save_artist(artist)
                    print(f"\n🎤 Artist: {artist['name']}")
                    print(f"🔥 Popularity: {artist['popularity']}")
                    print(f"🎧 Genres: {', '.join(artist['genres']) if artist['genres'] else 'Unknown'}")
                    print(f"🔗 Listen: {artist['url']}")
                    break
            else:
                print("❌ Couldn't find a new artist. Try again.")
        elif user_input == "no":
            print("Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
