# Clash Royale Top Card Tracker

Welcome to the **Clash Royale Top Card Tracker** — a web app that helps you visualize the top 10 Clash Royale cards you most frequently encounter in battles.

## Overview

This project uses **Python Flask** for the backend, serving HTML and CSS for the frontend. It integrates with the **Clash Royale API** to fetch battle data and analyzes it to identify the top 10 cards you have faced most often.

The app is deployed and hosted on [Render](https://clashroyaletopcardtracker.onrender.com).

---

## Features

- Fetches and processes Clash Royale battle data through the official API
- Displays your top 10 most commonly faced cards with visuals
- Clean and responsive UI using HTML and CSS

---

## Technologies Used

- Python 3.x
- Flask web framework
- HTML5 & CSS3
- Clash Royale API
- Render.com for deployment and hosting

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>

Install dependencies:

    pip install -r requirements.txt

Create a .env file and add your Clash Royale API key:

    API_KEY=your_api_key_here

Run the Flask app:

    flask run

Open your browser and visit http://localhost:5000

Deployment
The app is hosted on Render.com with the following setup:

Start command: gunicorn clash_tracker:app

Python environment with required packages in requirements.txt

Visit the live app here: https://clashroyaletopcardtracker.onrender.com