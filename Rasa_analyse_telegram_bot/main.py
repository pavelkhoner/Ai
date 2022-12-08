import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start(message):
	mess =  f"Привет, <u><b>{message.from_user.first_name}</b></u>"
	bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()