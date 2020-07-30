import discord
from discord.ext import commands
from secrets import discord_bot_token

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
@commands.has_permissions(manage_messages=True) #can only use this function if the user has the manage messages permission in the discord server
async def clear(ctx,amount : int):
    await ctx.channel.purge(limit=amount)

async def is_it_me(ctx):
    if ctx.author.id==145272316778119171: #checks if the author of the command has this id
        return True
    else:
        return False

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("you dont have permission for this command")



@client.command()
@commands.check(is_it_me) #runs check on the function in the brackets, if all true will run the function "example"
async def example(ctx):
    await ctx.send("Hi im {}".format(ctx.author))


client.run(discord_bot_token)