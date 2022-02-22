try:
	import shutil
	shutil.rmtree('config')
except:
	pass

from instabot import Bot
import getpass
bot = Bot()

user = '_____.___alone___._____'
passwd = getpass.getpass('Enter Password : ')

bot.login(username=user, password=passwd)

message = '''
Hello friend.

🔥...this message is sent using instabot library! ✨
'''
send_to = ["imvickykumar999"]

def sendmessage():
	bot.send_message(message, send_to)
	
sendmessage()
