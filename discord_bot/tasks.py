import discord
from discord.ext import commands,tasks
from itertools import cycle
from secrets import discord_bot_token
client = commands.Bot(command_prefix=".")
#use client. because client is used

status=cycle(["Status 1", "Status 2"])

@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready.")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



client.run(discord_bot_token)
