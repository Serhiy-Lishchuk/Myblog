from Flaskblog.db.db import get_db


def base_entries():
    """
    Read entries from the database
    """
    db = get_db()
    content = db.execute('SELECT title, text, image, music,timestamp FROM entries ORDER BY id DESC')
    entries = content.fetchall()
    db.close()
    return entries
