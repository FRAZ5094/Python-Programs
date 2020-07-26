import discord
from discord.ext import commands
from secrets import discord_bot_token
client = commands.Bot(command_prefix=".")
#use client. because client is used
@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def clear(ctx,amount : int):
    await ctx.channel.purge(limit=amount)
"""
@client.event
async def on_command_error(ctx,error): #for all errors, will overlap if you also have a function specific error function
    if isinstance(error,commands.MissingRequiredArgument): #handles missing requred arguments
        await ctx.send("Please pass in all required arguments")
"""

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Command doesn't exist")

@clear.error #only for an error with the "clear" function
async def clear_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please specify and amount of messages to delete")
            


client.run(discord_bot_token)