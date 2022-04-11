import discord
import json
import colorama
import random
import asyncio
import datetime
import time
import os
import requests
from colorama import Fore, init
import os
from colorama import Fore as C
from discord.ext import commands

prefix = "."

client = discord.Client()
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command('help') 

init(convert=True)
clear = lambda: os.system('cls')

os.system("title [ANTI-AFK] By evil aka mbn evil")

def starter():
    clear()
print(f'''
                                  
              {Fore.BLUE}                 █████  ███    ██ ████████ ██        █████  ███████ ██   ██   
                              ██   ██ ████   ██    ██    ██       ██   ██ ██      ██  ██   
                              ███████ ██ ██  ██    ██    ██ █████ ███████ █████   █████    
                              ██   ██ ██  ██ ██    ██    ██       ██   ██ ██      ██  ██   
                              ██   ██ ██   ████    ██    ██       ██   ██ ██      ██   ██ {Fore.BLUE}
''')


print(f'''{Fore.RED}Bot will answer at 5 seconds.{Fore.RED}
''')
print(f'''{Fore.CYAN}Have fun with antiafk.{Fore.CYAN}
''')
print(f'''{Fore.YELLOW}mbn evil#9731 add me for support{Fore.YELLOW}
''')
print(f'''{Fore.LIGHTRED_EX}evil runs u{Fore.LIGHTRED_EX}
''')
print(f'''{Fore.GREEN}Status: Working!
''')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
      time.sleep(2)
      await message.channel.send(random.choice(['hi lol', 'stop pinging me and focus :duck:', 'loool', 'sup :flushed:','im bored', 'afk check 1 2 3 4 5 6 7 8 9 10', 'im sleeping now stop', 'what i tell u shitty ass nerd',':nerd:','ggs slumped','fold','spining around and around','pinged','fuck up son :duck:','what','stop pinging me negro','https://tenor.com/view/ayodascrazy-back-in-blood-pooh-shiesty-cuh-gif-21644309' ]))        

with open('./config.json')as f:
  config = json.load(f)

token = config.get('token')
client.run(token, bot=False)
