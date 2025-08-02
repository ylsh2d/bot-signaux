from flask import Flask, request
from telegram import Bot
import logging

TELEGRAM_BOT_TOKEN = ' 8327576982:AAHWLQZW3KBBVyC9Etse-1XjSAUb8bB4eXA'  # 🔁 à remplacer
TELEGRAM_CHANNEL_ID = '@tradingsignauxbot'    # 🔁 à remplacer

bot = Bot(token=TELEGRAM_BOT_TOKEN)
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        symbol = data.get('symbol', 'XAUUSD')
        side = data.get('side', 'Achat')
        entry = data.get('entry')
        sl = data.get('sl')
        tp = data.get('tp')

        message = (
            f"🔔 Signal {symbol}\n\n"
            f"➡️ {side} à {entry:.2f}\n"
            f"🛑 SL : {sl:.2f}\n"
            f"🎯 TP : {tp:.2f}"
        )

        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
        return {"status": "success"}, 200
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
