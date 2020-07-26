import discord
import json
from discord.ext import commands
from secrets import discord_bot_token

def get_prefix(client,message):
    with open("prefixes.json","r") as f:
        prefixes=json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_guild_join(guild):
    with open("prefixes.json","r") as f:
        prefixes=json.load(f)

    prefixes[str(guild.id)]="." #default value

    with open("prefixes.json","w") as f:
        json.dump(prefixes,f,indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json","r") as f:
        prefixes=json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json","w") as f:
        json.dump(prefixes,f,indent=4)

@client.command()
async def changeprefix(ctx,prefix):
    with open("prefixes.json","r") as f:
        prefixes=json.load(f)

    prefixes[str(ctx.guild.id)]=prefix

    with open("prefixes.json","w") as f:
        json.dump(prefixes,f,indent=4)

client.run(discord_bot_token)