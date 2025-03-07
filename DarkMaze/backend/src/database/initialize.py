import sqlite3

def initialize():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    # Create game_state table (with username column)
    try:
       conn.commit()
       cursor.execute("""
       CREATE TABLE IF NOT EXISTS game_state (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT,
           current_level_name TEXT,
           map_size TEXT,
           health INTEGER,
           path TEXT,
           current_position TEXT
       )
       """)
    finally:
       conn.close()
