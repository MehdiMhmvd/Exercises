import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '853533585:AAHi7W-NeNanfTbmnsA1P5ld23Gj7zx0iLo'
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    




def insert_dash(md5):
	counter = 0
	devidedMd5 = ""
	for i in md5:
		devidedMd5 += i
		counter += 1
		if counter % 4 == 0 and counter != 64:
			devidedMd5 +="-"
	return devidedMd5

def hextoInt(hexlist):
	decimallist = []
	splited = hexlist.split("-")
	#print(splited)
	for h in splited:
		d = int(h,16)
		#print(type(d))
		decimallist.append(d)
		#print(d)
	return decimallist
Y=4503599627370496  #pow(2,52)


listOfhex = insert_dash(md5)
declist = hextoInt(listOfhex)

#hash_sum = sum(hash_sum)

#print(listOfhex)
print(declist)
hash_sum= sum(declist)
print(hash_sum)

if hash_sum % 50 == 0 :
	print("You loose")
else:
	special_hash = md5[0:13]
	print(special_hash)
	X = int(special_hash,16)

	print(X)
	z = ((100 * Y) - X) / (100*(Y-X)) #correct formule
	#zz = ((X-Y) * 100)   /  (X-(Y*100)) wrong
	print(z)
	print("Result is : %.3f"%z)

	
test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

	

