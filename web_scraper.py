"""
Advanced Python Program: Multithreaded Web Scraper
---------------------------------------------------
This script fetches page titles from multiple URLs in parallel
using ThreadPoolExecutor (multithreading).

Author: Your Name
License: MIT
"""

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

# List of websites to scrape titles from
URLS = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org",
    "https://www.openai.com"
]

def fetch_title(url):
    """Fetch the <title> of a webpage."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No Title Found"
        return url, title
    except Exception as e:
        return url, f"Error: {e}"

def main():
    print("Fetching titles using multithreading...\n")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_title, url) for url in URLS]
        for future in as_completed(futures):
            url, title = future.result()
            print(f"{url} → {title}")

if __name__ == "__main__":
    main()

# pip install requests beautifulsoup4


  # python web_scraper.py


# Fetching titles using multithreading...

# https://www.github.com → GitHub: Let’s build from here
# https://www.python.org → Welcome to Python.org
# https://www.wikipedia.org → Wikipedia
# https://www.stackoverflow.com → Stack Overflow - Where Developers Learn, Share, & Build Careers
# https://www.openai.com → OpenAI
