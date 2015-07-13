#!/usr/bin/env python3

from PyRock import PyRock
from PIL import ImageFont, Image, ImageDraw

apikey = 'INSERT_KEY'
apisecret = 'INSERT_SECRET'

rock = PyRock(apikey, apisecret)
price = rock.Ticker('btceur')['last']

font = ImageFont.truetype('/home/bot/TheRockPNG/Nobile-Medium.ttf', 26)
img = Image.new('RGBA', (280, 50), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)
draw.text((0, 0), '{0:.2f} EUR/BTC'.format(price).replace('.', ','), (0, 0, 0),font=font)
draw = ImageDraw.Draw(img)
img.save('/home/bot/TheRockPNG/pricexbteur.png')

a = Image.open("/home/bot/TheRockPNG/backgroundTR.png")
b = Image.open('/home/bot/TheRockPNG/pricexbteur.png')
a.paste(b, (70, 12), b)
a.save('/var/www/html/trtlast.png')


