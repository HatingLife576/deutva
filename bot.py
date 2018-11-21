import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ">>")
command_prefix = ">>"
cp = command_prefix

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.upper().startswith(cp + 'PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> pongo!" % (userID))
    if message.content.upper().startswith(cp + 'SAY'):
        args =message.content.split(" ")
        #args[0] = cp + 'SAY'
        #args[1:] = %s
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))




client.run("(token)")
