import os
import discord
import time
import datetime
import asyncio
from discord.ext import commands


class CMS2(commands.Cog):

    def __init__(self, client):
        self.client = client
# Ping command
    @commands.command(name='Ping')
    async def Ping(self, ctx):
        await ctx.channel.send(f"**pong!** That took {int(self.client.latency*1000)} ms!")


# Purge command


    @commands.command(name='Purge')
    @commands.has_permissions(manage_messages=True)
    async def Purge(self, ctx, limit: int = None):
            if not limit:
                purge_failed = discord.Embed(title='Purge [%Purge]', description=f'Successfully Purged {limit} messages. \n Command executed by {ctx.author}.', color=discord.Colour.random())
                purge_failed.set_footer(text=str(datetime.datetime.now()))
                return await ctx.send(embed=purge_failed)
            await ctx.message.delete()
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=limit)
            purge_embed = discord.Embed(title='Purge [%Purge]', description=f'Successfully Purged {limit} messages. \n Command executed by {ctx.author}.', color=discord.Colour.random())
            purge_embed.set_footer(text=str(datetime.datetime.now()))
            await ctx.send(embed=purge_embed)
    @Purge.error
    async def sendback(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.author.mention}You do not have permissions to do this command.")


# Help Command
    @commands.command(name='Help')
    async def Help(self, ctx):
        embed=discord.Embed(title='Help Page!', description=f"%Ping (To tell you if I am online or not) \n %Purge (To purge mass messages (Must have the manage message permission!!)) \n %Invite (Opens the invite page to invite me!) \n %Help (To open this page to tell you what commands I have) \n %Bal (Check you balence in the economy) \n %bag (Check your inventory to see what you have) \n %beg (Beg for money in the economy) \n %number(generates a random number for any of your needs) \n %Leave (Makes me leave the server(Note Only user <@786788350160797706> can as they are the Developer of the bot)) \n %shop (opens the shop in the economy) \n %buy (buys something from the shop) \n %Sell (sells an item from your bag) \n %use (command is not implemented yet and is in production sorry for the inconvience) \n %Slots (gamble your money)", color=0x206694)
        await ctx.channel.send(embed=embed)
#Invite command
    @commands.command(name='Invite')
    async def Invite(self, ctx):
        embed=discord.Embed(title='Invite Links!', description=f"[Invite(recommended)](https://discord.com/api/oauth2/authorize?client_id=902249858281394237&permissions=274877999168&scope=bot) \n [Invite(admin)](https://discord.com/api/oauth2/authorize?client_id=902249858281394237&permissions=8&scope=bot)", color=0x2ecc71)
        await ctx.channel.send(embed=embed)

#Leave command
    @commands.command(name='Leave')
    async def Leave(self,ctx):
        if ctx.author.id == 786788350160797706:
            await ctx.channel.send("Very well, idk why you would want me to leave but ok bye")
            await asyncio.sleep(1)
            await ctx.guild.leave()
        else:
            await ctx.channel.send("You can't use this command only the owner of the bot can!")
            


def setup(client):
     client.add_cog(CMS2(client)) 
