"""
intel_fetch.py · Extracción inicial de datos desde APIs públicas con enfoque ético
"""

import requests
import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# API headers
headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": os.getenv("USER_AGENT", "ATLANTYDE-API-Sync/1.0")
}

def fetch_github_repo(repo=None):
    """
    Fetches repository details from GitHub API.
    """
    repo = repo or os.getenv("GITHUB_REPO", "kabehz/atlantyde-kit")
    url = f"https://api.github.com/repos/{repo}"
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = r.json()
        logging.info(f"📦 {data['full_name']} - ⭐ {data['stargazers_count']} stars - 👁 {data['watchers_count']}")
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error fetching repo: {e}")

def fetch_medium_posts(user=None):
    """
    Placeholder for Medium API integration.
    """
    user = user or os.getenv("MEDIUM_USER", "atlante")
    logging.info(f"📘 Simulando extracción desde Medium API para el usuario '{user}' (futura integración)")

def fetch_x_posts(user=None):
    """
    Placeholder for X API integration.
    """
    user = user or os.getenv("X_USER", "atlEthical")
    logging.info(f"📘 Simulando extracción desde X API para el usuario '{user}' (futura integración)")

if __name__ == "__main__":
    logging.info("🧠 Extracción de insights API externa:")
    fetch_github_repo()
    fetch_medium_posts()
    fetch_x_posts()