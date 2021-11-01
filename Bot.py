# bot.py
import os
import discord
import time
import datetime
import asyncio
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='%', intents=intents, owner_id=786788350160797706)


bot = client

@client.event
async def on_ready():
      for guild in client.guilds:
        print(guild.name)
        print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        )
    
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

@bot.command(name='Ping')
async def Ping(ctx):
    await ctx.channel.send("pong")

@bot.command(name='Purge')
@commands.has_permissions(manage_messages=True)
async def Purge(ctx, limit: int):
    await ctx.message.delete()
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=limit)
    purge_embed = discord.Embed(title='Purge [$purge]', description=f'Successfully Purged {limit} messages. \n Command executed by {ctx.author}.', color=discord.Colour.random())
    purge_embed.set_footer(text=str(datetime.datetime.now()))
    await ctx.channel.send(embed=purge_embed)


@client.event
async def on_member_join(member):
  #channel = client.get_channel(846525476297113610)
  channels = member.guild.channels
  for channel in channels:
    if ('welcome' in channel.name) or ('joins' in channel.name) or ('testing' in channel.name):
      embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
      embed.set_thumbnail(url=member.avatar_url)

      await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
  #channel = client.get_channel(846525476297113610)
  channels = member.guild.channels
  for channel in channels:
    if ('leave' in channel.name) or ('left' in channel.name) or ('testing' in channel.name):
      embed=discord.Embed(title=f"Goodbye, {member.name}", description=f"Bye {member.name} come again soon")
      embed.set_thumbnail(url=member.avatar_url)

      await channel.send(embed=embed)

@bot.command(name='Invite')
async def Invite(ctx):
    embed=discord.Embed(title='Invite Links!', description=f"[Invite(recommended)](https://discord.com/api/oauth2/authorize?client_id=902249858281394237&permissions=274877999168&scope=bot) \n [Invite(admin)](https://discord.com/api/oauth2/authorize?client_id=902249858281394237&permissions=8&scope=bot)", color=0x2ecc71)
    await ctx.channel.send(embed=embed)


@bot.command(name='Help')
async def Help(ctx):
  embed=discord.Embed(title='Help Page!', description=f"%Ping (To tell you if I am online or not) \n %Purge (To purge mass messages) \n %Invite (Opens the invite page to invite me!) \n %Help (To open this page to tell you what commands I have)", color=0x206694)

  await ctx.channel.send(embed=embed)


client.run(TOKEN)