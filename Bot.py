# bot.py
#Import list
import os
import discord
import time
import datetime
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb")
db = cluster["discord"]
collection = db["prefix"]
#________________________________________________
#File Configs
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='%', intents=intents, owner_id=786788350160797706, Help_command=None, case_insensitive=True)
bot = client
bot.remove_command('help')
#______________________________________________________________________________________________

@bot.command()
async def load(ctx, exstension):
  client.load_extension(f'cogs.{exstension}')




@bot.command()
async def reload(ctx, extension):
  if ctx.author.id != 786788350160797706: return
  else:
    client.reload_extension(f'cogs.{extension}')
    await ctx.channel.send("Cog reloaded!")


    
client.load_extension("cogs.fun")
client.load_extension("cogs.events")
client.load_extension("cogs.commands")
client.load_extension("cogs.804864012184977438")
client.load_extension("cogs.leave")
client.load_extension("cogs.welcome")
client.run(TOKEN)