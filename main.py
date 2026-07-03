import telebot
import os

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# هذا السطر هو الحل! سيقوم بحذف الـ Webhook القديم قبل بدء البوت
bot.delete_webhook(drop_pending_updates=True)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تم الاستلام!")

print("البوت يعمل الآن...")
bot.infinity_polling()
