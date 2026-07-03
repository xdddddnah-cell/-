import telebot
import os

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# هذا السطر ضروري جداً لإنهاء أي تعليق سابق
bot.delete_webhook(drop_pending_updates=True)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تم الاستلام!")

bot.infinity_polling()
