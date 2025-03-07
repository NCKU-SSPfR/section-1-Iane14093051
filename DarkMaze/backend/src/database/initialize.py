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
           username ,
           current_level_name ,
           map_size ,
           health ,
           path ,
           current_position 
       )
       """)
    finally:
       conn.close()
