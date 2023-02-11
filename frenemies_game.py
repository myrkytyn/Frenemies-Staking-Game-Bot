import requests
import telebot
import schedule
import time


# Telegram Bot part
# If you don't need Telegram notifications - just comment this part with #
bot = telebot.TeleBot("{PUT_BOT_TOKEN_HERE}", parse_mode=None)


def send_message(status_code, response_text):
    bot.send_message(
        chat_id="{PUT_CHAT_ID_HERE}", text=f"Status code: {status_code}, \nServer response: {response_text}")


# Discord part
url = "https://discord.com/api/v9/channels/1037811694564560966/messages"
auth = {
    "Authorization": "{PUT_AUTHORIZATION_TOKEN_HERE}"
}
msg = {
    "content": "!faucet {PUT_SUI_WALLET_HERE}"
}


def get_sui():
    response = requests.post(url, headers=auth, data=msg)
    print(response.status_code)
    #If you don't need Telegram notifications - just comment the next line with #
    send_message(response.status_code, response.text)


get_sui()
schedule.every(125).minutes.do(get_sui)

while True:
    schedule.run_pending()
    time.sleep(1)
