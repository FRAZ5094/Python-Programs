import discord
from discord.ext import commands
from secrets import discord_bot_token
client = commands.Bot(command_prefix=".")
#use client. because client is used
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game("Fuck you bitch"))
    print("Bot is ready.")




client.run(discord_bot_token)