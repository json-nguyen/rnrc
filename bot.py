# bot.py
import os
import requests
import json
from random import randint
import discord 
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_SERVER = os.getenv('SERVER_NAME')
TENOR_API_KEY = os.getenv('TENOR_KEY')
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord!')

@bot.event
async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'welcome ugly: {member.name}'
        )

@bot.command(name='test')
async def test(ctx):
    response = 'TEST'
    await ctx.send(response)

@bot.command(name='rnrc')
async def rnrc(ctx):
    search_term = "assemble"
    search = "https://api.tenor.com/v1/random?q=%s&key=%s&limit=1" % (search_term, TENOR_API_KEY)

    req = requests.get(search)
    json = req.json()

    gifURL = json['results'] 
    gifURL = gifURL[0]
    gifURL = gifURL['url']

    rn = discord.utils.get(ctx.message.guild.roles, name="Real JITS")
    
    await ctx.send("{}".format(rn.mention) + " Its time. Real JITS: ASSEMBLE\n" +
                    gifURL)

@bot.command(name='spark')
async def spark(ctx):
    search_term = "hangzhou spark"
    search = "https://api.tenor.com/v1/search?q=%s&key=%s&limit=16" %(search_term, TENOR_API_KEY)

    req = requests.get(search)

    json = req.json()    
    #rn = discord.utils.get(ctx.message.guild.roles, name="RN")
    
    gifURL = json['results'] 
    gifURL = gifURL[randint(0,11)]
    gifURL = gifURL['url']

    await ctx.send(gifURL)      


bot.run(TOKEN)