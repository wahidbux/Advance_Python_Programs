"""
Advanced Python Program: URL Shortener with SQLite
--------------------------------------------------
This script creates a simple URL shortener using hashing
and stores the mappings in a local SQLite database.

Author: Your Name
License: MIT
"""

import sqlite3
import hashlib
import sys
import os

DB_NAME = "urls.db"

def init_db():
    """Initialize SQLite database with table."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT UNIQUE,
            short_code TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def shorten_url(long_url: str) -> str:
    """Generate a short code for the given URL and store it."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Check if already exists
    cur.execute("SELECT short_code FROM urls WHERE long_url=?", (long_url,))
    row = cur.fetchone()
    if row:
        conn.close()
        return row[0]

    # Generate hash-based short code (first 6 chars of md5)
    short_code = hashlib.md5(long_url.encode()).hexdigest()[:6]

    cur.execute("INSERT OR IGNORE INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()
    conn.close()
    return short_code

def expand_url(short_code: str) -> str:
    """Retrieve original URL from short code."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT long_url FROM urls WHERE short_code=?", (short_code,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0]
    return "No URL found for this code."

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python url_shortener.py shorten <long_url>")
        print("  python url_shortener.py expand <short_code>")
        sys.exit(1)

    command, value = sys.argv[1], sys.argv[2]
    init_db()

    if command == "shorten":
        code = shorten_url(value)
        print(f"Short code for {value} → {code}")
    elif command == "expand":
        url = expand_url(value)
        print(f"Original URL for {value} → {url}")
    else:
        print("Invalid command. Use 'shorten' or 'expand'.")

if __name__ == "__main__":
    main()
