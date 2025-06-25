import os
import requests
from collections import Counter
from dotenv import load_dotenv
from urllib.parse import quote

# --- Load .env values ---
load_dotenv()
PLAYER_TAG = os.getenv("PLAYER_TAG")
API_TOKEN = os.getenv("API_TOKEN")

# Check if environment variables are loaded
if not PLAYER_TAG or not API_TOKEN:
    print("Error: PLAYER_TAG or API_TOKEN not found in .env file")
    exit()

# URL encode the player tag (handles # symbol)
encoded_player_tag = quote(PLAYER_TAG, safe='')

API_URL = f"https://proxy.royaleapi.dev/v1/players/{encoded_player_tag}/battlelog"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

print(f"Requesting: {API_URL}")
print(f"Player tag: {PLAYER_TAG}")

# --- Get Battle Logs ---
response = requests.get(API_URL, headers=headers)
if response.status_code != 200:
    print("Error:", response.status_code, response.text)
    print("Make sure your PLAYER_TAG includes the # symbol and your API_TOKEN is valid")
    exit()

battles = response.json()

# --- Extract Opponent Cards ---
opponent_cards = []
for battle in battles:
    # Handle both single opponent and team battles
    opponents = battle.get("opponent", [])
    if not isinstance(opponents, list):
        opponents = [opponents]
    
    for opponent in opponents:
        cards = opponent.get("cards", [])
        opponent_cards.extend(card["name"] for card in cards)

# --- Count Top 3 ---
counter = Counter(opponent_cards)
top_10 = counter.most_common(10)

if not top_10:
    print("No opponent cards found in recent battles")
else:
    print("🔥 Top 10 Most Common Cards You've Faced Recently:")
    for card, count in top_10:
        print(f" - {card}: {count} times")