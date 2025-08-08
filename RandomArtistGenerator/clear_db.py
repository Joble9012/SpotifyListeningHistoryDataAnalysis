import sqlite3

DB_NAME = 'artists.db'

confirm = input("⚠️  This will delete all artist records. Continue? (yes/no): ").strip().lower()
if confirm == "yes":
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM artists')
    conn.commit()
    conn.close()
    print("✅ Database cleared.")
else:
    print("❌ Operation cancelled.")
