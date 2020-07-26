import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix=".")
#use client. because client is used
@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send("Pong! {}ms".format(round(client.latency*1000)))

@client.command(aliases=["8ball"]) #all aliases can be used to call this function
async def _8ball(ctx,*,question):
    responses=["bruh","not bruh"]
    await ctx.send("Question: {}\nAnswer: {}".format(question,random.choice(responses)))

@client.command()
async def clear(ctx,amount=5): #default value of 5
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx,member : discord.Member,*, reason=None): #reads in member as a discord.Member object,need to pass in @member
#* means all parameters after member and reason will be added onto reason (for using spaces in reason)
    await member.kick(reason=reason)

@client.command()
async def ban(ctx,member : discord.Member,*, reason=None):
    await member.ban(reason=reason)
    await ctx.send("banned {}".format(member.mention))

@client.command()
async def unban(ctx,*,member): #some discord usernames have spaces, hence *
    banned_users= await ctx.guild.bans()
    member_name,member_discriminator=member.split("#")# used for bruh#123, gives bruh,123

    for ban_entry in banned_users:
        user=ban_entry.user

        if (user.name,user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("unbanned {}".format(user.mention))
            return 


            
client.run("NzM2MzUxOTA4MjQyOTE1NDA4.XxtjJw.G9RobcphGN1l26XVxYOJQTzkI30")