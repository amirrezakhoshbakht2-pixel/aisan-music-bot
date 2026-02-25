import os
from flask import Flask, request
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

BOT_TOKEN = "8424780818:AAGxKFvQ-Bk7RKYvwhgSk193n2cQHnarwPI"
API_ID = 24097731
API_HASH = "ce9ad8ae9c0a901364d618517ad697fc"
OWNER_ID = 123456789  # اینو بعداً عوض کن

app = Flask(__name__)
bot = Client("aisan_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
FORCE_CHANNEL = None

@app.route('/')
def home():
    return "ربات آیسان روشن است"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    asyncio.create_task(bot.process_update(update))
    return 'OK'

@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("🎵 سلام! ربات موزیک پلیر آیسان روشن است!")

def setup_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url=https://{os.environ.get('RENDER_EXTERNAL_URL', '')}/webhook"
    requests.get(url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    setup_webhook()
    app.run(host="0.0.0.0", port=port)
