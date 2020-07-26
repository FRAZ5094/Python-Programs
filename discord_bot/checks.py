import discord
from discord.ext import commands


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
@commands.has_permissions(manage_messages=True) #can only use this function if the user has the manage messages permission in the discord server
async def clear(ctx,amount : int):
    await ctx.channel.purge(limit=amount)

def is_it_me(ctx):
    return ctx.author.id==145272316778119170 #checks if the author of the command has this id


@client.command()
@commands.check(is_it_me) #runs check on the function in the brackets, if all true will run the function "example"
async def example(ctx):
    await ctx.send("Hi im {}".format(ctx.author))


client.run("NzM2MzUxOTA4MjQyOTE1NDA4.XxtjJw.G9RobcphGN1l26XVxYOJQTzkI30")