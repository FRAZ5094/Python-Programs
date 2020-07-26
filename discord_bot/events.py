import discord
from discord.ext import commands
from secrets import discord_bot_token
client = commands.Bot(command_prefix=".")
#use client. because client is used
@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print("{} has joined".format(member))

@client.event 
async def on_member_remove(member):
    print("{} has left a server".format(member))

client.run(discord_bot_token)
