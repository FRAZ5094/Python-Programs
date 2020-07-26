import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")
#use client. because client is used
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game("Fuck you bitch"))
    print("Bot is ready.")


client.run("NzM2MzUxOTA4MjQyOTE1NDA4.XxtjJw.G9RobcphGN1l26XVxYOJQTzkI30")
