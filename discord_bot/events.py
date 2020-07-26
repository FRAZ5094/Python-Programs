import discord
from discord.ext import commands

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

client.run("NzM2MzUxOTA4MjQyOTE1NDA4.XxtjJw.G9RobcphGN1l26XVxYOJQTzkI30")
