try:
	import shutil
	shutil.rmtree('config')
except:
	pass

from instabot import Bot
import getpass
bot = Bot()

user = ['_____.___alone___._____', 'vix.bot']
passwd = getpass.getpass('Enter Password : ')
bot.login(username = user[1], password = passwd)


from PIL import Image

def make_square(im, min_size=256, fill_color=(255,255,255,0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

choose = 'himalayan.jpg'
path = f'to_upload/{choose}'

test_image = Image.open(path)
new_image = make_square(test_image)

path = 'to_upload/himalayan_squared.jpg'
new_image.save(path)

cap = '🔥This image is uploaded using python code ✨'
bot.upload_photo(path, caption = cap)

try:
	import shutil
	shutil.rmtree('config')
except:
	pass