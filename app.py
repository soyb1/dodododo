
import os
from flask import Flask, render_template, request, jsonify
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

app = Flask(__name__)

# Load config from environment variables
BOT_TOKEN = os.getenv("7564198568:AAHjuSfh3doH4HMZ2OlenfvEZk9MkSCSQC0")
WEB_APP_URL = os.getenv("WEB_APP_URL", "https://your-webapp-url.com")

# In-memory storage for balances (for demo purposes)
users = {}

# Telegram Bot Setup
bot = Bot(BOT_TOKEN)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mine", methods=["POST"])
def mine():
    user_id = request.json.get("user_id")
    if user_id not in users:
        users[user_id] = 0.0
    users[user_id] += 0.001
    return jsonify({"message": "You mined 0.001 DOD!", "balance": users[user_id]})

@app.route("/balance", methods=["POST"])
def balance():
    user_id = request.json.get("user_id")
    balance = users.get(user_id, 0.0)
    return jsonify({"balance": balance})

@app.route("/referral", methods=["POST"])
def referral():
    user_id = request.json.get("user_id")
    ref_link = f"https://t.me/{bot.username}?start={user_id}"
    return jsonify({"referral_link": ref_link})

def start_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

if __name__ == "__main__":
    start_flask()
