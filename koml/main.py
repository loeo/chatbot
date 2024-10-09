# main.py
from koml import KomlBot

bot = KomlBot()
bot.learn(['koml.xml'])
bot.converse()