import os
import discord
import time
import datetime
import asyncio
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status= discord.Status.online, activity=discord.Game(f'%help Learning how to add more commands to my library of commands!'))
        for guild in self.client.guilds:
            print(guild.name)
            print(guild.me.guild_permissions)
            print(
            f'{self.client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id}) \n'
            )
    
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}') 
#Client Events

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.member):
        if member.guild.id == 804864012184977438 : return
        channels = member.guild.channels
        for channel in channels:
            if ('welcome' in channel.name.lower()) or ('joins' in channel.name.lower()): #or ('testing' in channel.name)
                 embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
                 embed.set_thumbnail(url=member.avatar_url)
                 if isinstance(channel, discord.TextChannel):
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.member):
        if member.guild.id == 804864012184977438 : return
        channels = member.guild.channels
        for channel in channels:
            if ('leave' in channel.name.lower()) or ('goodbye' in channel.name.lower()): #or ('testing' in channel.name):
                embed=discord.Embed(title=f"Goodbye, {member.name}", description=f"Bye {member.name} come again soon")
                embed.set_thumbnail(url=member.avatar_url)
                if isinstance(channel, discord.TextChannel):
                    await channel.send(embed=embed)


def setup(client):
    client.add_cog(Events(client))      
