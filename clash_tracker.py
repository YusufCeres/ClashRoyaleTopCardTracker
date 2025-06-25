import os
from flask import Flask, render_template, request
import requests
from collections import Counter
from dotenv import load_dotenv
from urllib.parse import quote

app = Flask(__name__)

# Load environment variables
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

def get_top_cards(player_tag):
    """Fetch battle logs and return top 10 opponent cards"""
    encoded_player_tag = quote(player_tag, safe='')
    api_url = f"https://proxy.royaleapi.dev/v1/players/{encoded_player_tag}/battlelog"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        battles = response.json()
        
        opponent_cards = []
        for battle in battles:
            opponents = battle.get("opponent", [])
            if not isinstance(opponents, list):
                opponents = [opponents]
            
            for opponent in opponents:
                cards = opponent.get("cards", [])
                opponent_cards.extend(card["name"] for card in cards)

        counter = Counter(opponent_cards)
        return counter.most_common(10)
    
    except Exception as e:
        print(f"API Error: {str(e)}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_data = None
    player_tag = ""
    error = None
    
    if request.method == 'POST':
        player_tag = request.form['player_tag'].strip()
        if player_tag:
            chart_data = get_top_cards(player_tag)
            if not chart_data:
                error = "Error fetching data. Check your player tag or try again later."
        else:
            error = "Please enter a valid player tag"
    
    return render_template('index.html', 
                          chart_data=chart_data, 
                          player_tag=player_tag, 
                          error=error)

if __name__ == '__main__':
    app.run(debug=True)