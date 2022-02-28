# bot.py
#Import list
import os
import discord
import time
import datetime
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
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
async def unload(ctx, exstension):
  client.unload_extension(f'cogs.{exstension}')


    
client.load_extension("cogs.fun")
client.load_extension("cogs.events")
client.load_extension("cogs.commands")
client.run(TOKEN)