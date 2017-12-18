from flask import Flask, request
import telebot
import os

server = Flask(__name__)
TOKEN  = "491041391:AAGIzd86W4mPZDAgLRwZcweXmGDkVAJacRE"
bot = telebot.TeleBot(TOKEN)
port = int(os.environ.get("PORT", 5000))

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://glacial-peak-27915.herokuapp.com/" + TOKEN)
    return "!", 200

@server.route("/" + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "!", 200

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, "Hi")

server.run(host='0.0.0.0', port=port)
