import sqlite3
conn = sqlite3.connect("game.db")
cursor = conn.cursor()
def initialize():


    # Create game_state table (with username column)
    try:
       cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_state (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        current_level_name TEXT,
        map_size TEXT,
        health INTEGER,
        path TEXT,
        current_position TEXT
    )
    """)
       conn.commit()
    finally:
       conn.close()
