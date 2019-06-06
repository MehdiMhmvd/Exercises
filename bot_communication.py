#https://api.telegram.org/bot853533585:AAHi7W-NeNanfTbmnsA1P5ld23Gj7zx0iLo/sendmessage?chat_id=633737114&text=salaam
import requests
import telebot
import time 
bot_token = '853533585:AAHi7W-NeNanfTbmnsA1P5ld23Gj7zx0iLo'
'''
def telegram_bot_sendtext(bot_message):
    
    
    bot_chatID = '633737114'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message +"&disable_notification=True"

    response = requests.get(send_text)

    return response.json()
test = telegram_bot_sendtext("Thi mehsun")
print(test)
'''
bot = telebot.TeleBot(token = bot_token)

@bot.message_handler(commands = ["start"])
def welcomemsg(message):
	bot.reply_to(message,"welcome!")


while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(1)
	




