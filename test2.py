from flask import Flask, request
import telebot
import os

server = Flask(__name__)
TOKEN  = 'token'
bot = telebot.TeleBot('491041391:AAGIzd86W4mPZDAgLRwZcweXmGDkVAJacRE') #тут мой токен
port = int(os.environ.get("PORT", 5000))

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://myapp/bot") #ссылку изменил
    return "!", 200

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "ok", 200

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, 'Hi') #вот эта часть кода исполняется два или три раза
