import discord
import ast
import asyncio
import json
import datetime
import logging
from bs4 import BeautifulSoup
import urllib.request
import re
import os
from boto.s3.connection import S3Connection
import re
import datetime, time
from discord.ext.commands import Bot
from discord.ext import commands
import time
import random
from keep_alive import keep_alive
import asyncio
from asyncio import sleep
from discord.utils import get
from random import randint
import datetime
import sys
import os
from discord.ext.commands import (Bot, BotMissingPermissions, bot_has_permissions)
from discord import *
import pprint
import random
import asyncio
import datetime
import time
import paginator
from disputils import BotEmbedPaginator
import keep_alive
from keep_alive import keep_alive
import praw
import sys
import subprocess
import ast
import json
import praw
import traceback
import platform
import psutil
import base64
import json
import os
import random
from random import randint
import signal
import sys
import urllib.parse
import datetime

from PIL import Image
import requests
      


client = discord.Client
client = commands.Bot(
    command_prefix=[
        "Van ",
    ],
    owner_id=552492140270452736,
    status=discord.Status.idle,
    activity=discord.Activity(
        type=discord.ActivityType.playing,
        name=f"With Thomas Brodie |Tetsurou help",
        url="https://www.twitch.tv/pkidz2123"))  #Set the command prefix to what you prefer
        
bot = client
async def statuschange():
	while not client.is_closed():
		await bot.wait_until_ready(
		)  # Makes the bot wait until it's fully ready before the stuff below are ran
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.watching,
		        name=f"{len(bot.guilds)} Guild's | Find bug? Dm owner!",
		        url="https://www.twitch.tv/pkidz2123")
		)  
		await asyncio.sleep(15)  # Makes it wait another 8 seconds and then it'll go back to the top on playing because we used "while" which makes it look
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.watching,
		        name=f"Owner: Minho Newt Uwu#2144",
		        url="https://www.twitch.tv/pkidz2123")
		)  
		await asyncio.sleep(15) 
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.streaming,
		        name=f"With Thomas Brodie | Py!help",
		        url="https://www.twitch.tv/pkidz2123"))
		await asyncio.sleep(15)

async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    for Cogs in Cogs:
        bot.load_extension(Cogs)
    return


extensions = ['Cogs.user','Cogs.Search','Cogs.commands','Cogs.Encoding','Cogs.misc commands', 'Cogs.membercount','Cogs.Members','Cogs.utility','Cogs.Owner']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

playingBlackJack = False
dealerValue = 0
playerValue = 0
dealerCards = []
playerCards = []
dealerNumAces = 0
playerNumAces = 0
cardNames = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
             10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
cardValues = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10, 14: 11}

# Rock paper scissors variables (1 == rock, 2 == paper, 3 == scissors)
playingRPS = False
aiChoice = 0
playerChoice = 0
aiPoints = 0
playerPoints = 0

# Riddle variables
answering = False
riddle = ""
riddleAnswer = ""
riddleLine = 0
riddleGuessesLeft = 3
prevRiddleLine = 0

# Good Morning variable
gmOptionEnabled = False

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    

bot.remove_command('help')

@bot.command()
async def on_guild_join(guild, message, ctx):
  await ctx.send('Thanks For Invite Me') 
    
@bot.command()
async def modcmd(ctx):
    embed = discord.Embed(color=ctx.author.top_role.colour)
    embed.add_field(name="<a:swiperight:713234344705261680> MODERATION", value="```channelmem, warn, clearwarnings, checkwarn, softban, addrole, removerole, poll, ban, clear, cl, ban, clear, clears, kick, lock, mute, roleinfo, setupmute, slowmode, stats, unlock, unmute, updates, userroles, listban, rolecolor, nick```", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def membercmd(ctx):
    embed = discord.Embed(color=ctx.author.top_role.colour)
    embed.add_field(name="<a:swiperight:713234344705261680> MEMBER", value="```afk, lmgtfy, emojify, findrole, finduser, members, channelinfo, translate, about, pp, asciify, testmemory, counting, pypi, tinyurl, ava, suggest, report, invite, 8ball, bigemoji, calculator, division, memo, characters, cointoss, counteach, github, magic, reverse, twitter, wordcount, video, avatar, setup, cat, serverinfo, updates, wiki, getHelp, googling, greet, info, membercount, minecraft, slap, image, meme, rps, supreme, drakememe```", inline=False)
    await ctx.send(embed=embed)
    
    
@bot.command()
@commands.is_owner()
async def devcmd(ctx):
    embed = discord.Embed(color=ctx.author.top_role.colour)
    embed.add_field(name="<a:swiperight:713234344705261680> OWNER BOT", value="```eval, servers, Myserver, cog```", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def ecocmd(ctx):
    embed = discord.Embed(color=ctx.author.top_role.colour)
    embed.add_field(name="<a:swiperight:713234344705261680> ECONOMY", value="```bal, work, rob, give```", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def infocmd(ctx):
    embed = discord.Embed(color=ctx.author.top_role.colour)
    embed.add_field(name="<a:swiperight:713234344705261680> INFORMATION BADGES", value="```nitroBadge, staffBadge, partnerBadge, hypeventBadge```", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def levelcmd(ctx):
    embed = discord.Embed(color=ctx.author.top_role.colour)
    embed.add_field(name="<a:swiperight:713234344705261680> LEVEL COMMAND", value="```level, leaderboard````", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=ctx.author.top_role.colour)
    embed.add_field(name="<a:swiperight:713234344705261680> MODERATION", value="```Type Py!modcmd for see, this command just for administration```", inline=False)
    embed.add_field(name="<a:swiperight:713234344705261680> MEMBER", value="```Type Py!membercmd for see, this command can use for all members```", inline=False)
    embed.add_field(name="<a:swiperight:713234344705261680> JUST ME", value="```Type Py!devcmd for see, this commmand just for Owner Bot!```", inline=False)
    embed.add_field(name="<a:swiperight:713234344705261680> ECONOMY", value="```Type Py!ecocmd for see, this command for economy user!```", inline=False)
    embed.add_field(name="<a:swiperight:713234344705261680> INFO", value="```Type Py!infocmd for see, this command for information about discord badge```", inline=False)
    embed.add_field(name="<a:swiperight:713234344705261680> LEVEL", value="```Type Py!levelcmd for see, this command for information about your level and XP!```")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/714330708365148190/0e8b28cd2c24b72bb6593998f237e133.webp?size=1024")
    embed.set_footer(text=f"Help Command! | {datetime.datetime.now()}")
    await ctx.send(embed=embed)

@bot.command(helpinfo='Looks up a sequence of numbers', aliases=['numbers', 'integers'])
async def oeis(ctx, *, number: str):
    '''
    Looks up a sequence of numbers
    '''
    req=requests.get('https://oeis.org/search?q={}&fmt=json'.format(number)).json()['results'][0]
    numid = 'A'+str(req['number']).zfill(6)
    embed = discord.Embed(title='**'+numid+'**', url='https://oeis.org/{}'.format(numid), description='**'+req['name']+'**', color=0xFF0000)
    embed.add_field(name="Numbers:", value=str(req['data']), inline=False)
    embed.set_image(url='https://oeis.org/{}/graph?png=1'.format(numid))
    embed.set_thumbnail(url='https://oeis.org/oeis_logo.png')
    embed.set_footer(text='OEIS', icon_url='https://oeis.org/oeis_logo.png')
    embed.set_author(name='OEIS.org', url='https://oeis.org/', icon_url='https://oeis.org/oeis_logo.png')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send('**Search result for:** ***{}...***'.format(number), embed=embed)
    
@bot.command(helpinfo='For when plain text just is not enough')
async def emojify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into emoji
    '''
    author = ctx.message.author
    emojified = '⬇ Copy and paste this: ⬇\n'
    formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in formatted:
            if i == ' ':
                emojified += '     '
            else:
                emojified += ':regional_indicator_{}: '.format(i)
        if len(emojified) + 2 >= 2000:
            await ctx.send('Your message in emojis exceeds 2000 characters!')
        if len(emojified) <= 25:
            await ctx.send('Your message could not be converted!')
        else:
            await author.send('`'+emojified+'`')

@bot.command(helpinfo='Shows MC account info, skin and username history', aliases=['skin', 'mc'])
async def minecraft(ctx, username='Van'):
    '''
   Shows MC account info, skin and username history
    '''
    uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'
                        .format(username)).json()['id']

    url = json.loads(base64.b64decode(requests.get(
        'https://sessionserver.mojang.com/session/minecraft/profile/{}'
        .format(uuid)).json()['properties'][0]['value'])
                     .decode('utf-8'))['textures']['SKIN']['url']
    
    names = requests.get('https://api.mojang.com/user/profiles/{}/names'
                        .format(uuid)).json()
    history = "**Name History:**\n"
    for name in reversed(names):
        history += name['name']+"\n"

    await ctx.send('**Username: `{}`**\n**Skin: {}**\n**UUID: {}**'.format(username, url, uuid))
    await ctx.send(history)
    
@bot.command()     
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))
    
@client.command()
async def image(ctx, *, word):
    linkWord = word.replace(' ', '+')
    url = "https://imgur.com/search/time?q=" + linkWord + "&qs=thumbs"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    imgLinkList = soup.find_all("a", {"class": "image-list-link"})
    print(len(imgLinkList))
    imgLink = imgLinkList[random.randrange(0,len(imgLinkList))]
    imgLink = imgLink.get("href")
    # imgLink = imgContainerLink.find("img").get("src")
    # await client.say(imgLink.replace("//i.imgur.com/","https://i.imgur.com/"))
    await ctx.send("https://imgur.com/" + imgLink)
    
@client.command()
async def googling(ctx, *, word):
    definition = ""
    linkWord = word.replace(' ', '+')
    url = 'https://www.wordnik.com/words/' + linkWord
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    definition = soup.select_one('.active > h3:nth-child(1)').text + "\n\n" + soup.select_one(".active > ul:nth-child(2) > li:nth-child(1)").text
    await ctx.send("**" + word + "\n\n" + definition + "**")

@client.command()
async def video(ctx, *, word):
    linkWord = word.replace(' ', '+')
    url = 'https://www.youtube.com/results?sp=EgIQAQ%253D%253D&search_query=' + linkWord
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    vidLink = soup.find("div", {"class": "yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix"}).get("data-context-item-id")
    await ctx.send("https://www.youtube.com/watch?v=" + vidLink)
    
@client.command(aliases=['prefix', 'pv'])
@commands.has_permissions(administrator=True)
async def serverprefix(ctx, prefix):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    
  prefixes[str(ctx.guild.id)] = prefix
  
  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)
    
  embed = discord.Embed(title='Guild command', description=f'successfully change prefix to `{prefix}`', colour=discord.Colour.green(), timestamp=datetime.utcnow())
  embed.set_footer(text=f'Prefix update by {ctx.author}')
  await ctx.send(embed=embed, delete_after=15)
  await ctx.message.delete()

@serverprefix.error
async def serverprefix_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    embed = discord.Embed(title='Error', description=f'<a:Redtick:722006548276183071> {error}', colour=discord.Colour.red(), timestamp=datetime.utcnow())
    await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def servers(ctx):
	await ctx.send(f"I am connected to {len(bot.guilds)} servers:")
	async for guild in bot.fetch_guilds(limit=150):
		await ctx.send(f"`{guild.name}` | `{guild.id}`")
@servers.error
async def servers_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send(error)

@bot.command(aliases=['run', 'eval', 'e'])
@commands.is_owner()
async def eval_fn(ctx, *, cmd):
	"""Evaluates input.
    Input is interpreted as newline seperated statements.
    If the last statement is an expression, that is the return value.
    Usable globals:
      - `bot`: the bot instance
      - `discord`: the discord module
      - `commands`: the discord.ext.commands module
      - `ctx`: the invokation context
      - `__import__`: the builtin `__import__` function
    Such that `>eval 1 + 1` gives `2` as the result.
    The following invokation will cause the bot to send the text '9'
    to the channel of invokation and return '3' as the result of evaluating
    >eval ```
    a = 1 + 2
    b = a * 2
    await ctx.send(a + b)
    a
    ```
    """
	fn_name = "_eval_expr"

	cmd = cmd.strip("` ")

	# add a layer of indentation
	cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

	# wrap in async def body
	body = f"async def {fn_name}():\n{cmd}"

	parsed = ast.parse(body)
	body = parsed.body[0].body

	insert_returns(body)

	env = {
	    'bot': ctx.bot,
	    'discord': discord,
	    'commands': commands,
	    'ctx': ctx,
	    '__import__': __import__
	}
	exec(compile(parsed, filename="<ast>", mode="exec"), env)

	result = (await eval(f"{fn_name}()", env))
	await ctx.send(f"{result}")

@bot.command()
@commands.is_owner()
async def Myserver(ctx):
    servers = []
    for x in client.guilds:
        Add="\n"
        New = str(x.name)
        Final = str(New + Add)
        servers.append(Final)
        One_String = " ".join(servers)
        embed=discord.Embed(colour=discord.Colour.blue(),timestamp=datetime.datetime.now())
        embed.set_footer(text='Thanks to xEnder#0001 for helping')
        embed.add_field(name=f"Servers: {len(bot.guilds)}",value=One_String,inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_owner()
async def cog(ctx, type = None, *, name = None):
  
  if type == "load":
    
    bot.load_extension(name)
    
    await ctx.send(f"Loaded `{name}`.")
    
  elif type == "unload":
    
    bot.unload_extension(name)
    
    await ctx.send(f"Unloaded `{name}`.")
  
  elif type == "reload":

    if name == "all":

      for cog in os.listdir('cogs'):
        if cog.endswith('.py'):
          try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.reload_extension(cog)
            await ctx.send(f"Reloaded `{cog}`.")
            await asyncio.sleep(1)
      
          except Exception as e:
            await ctx.send(f'`{cog}` loading failed.')
            raise e

      await ctx.send("Reloaded all cogs.")

    else:

      bot.reload_extension(name)

      await ctx.send(f"Reloaded `{name}`.")

  else:
    
    embed = discord.Embed(title = "<a:lba:712993920350421002> Command name : Py!cog")
    
    embed.description = "`Py!cog load/unload <name>`\n`Py!cog reload <name / all>`"
    
    embed.color = discord.Color.blue()
    
    await ctx.send(embed=embed)

@client.command()   
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None):
  """➜  Banned Members!"""
  await member.ban()
  await ctx.send(f"**<a:pinWoe:715030587349663864> {member}** telah di ban")
  
@client.command()
async def ping(ctx):
	ping = client.latency
	ping = round(ping* 1000)
	ping1 = discord.Embed(
	    title='Pinging in 3', color=ctx.author.top_role.colour)
	ping2 = discord.Embed(
	    title='Pinging in 2', color=ctx.author.top_role.colour)
	ping3 = discord.Embed(
	    title='Pinging in 1', color=ctx.author.top_role.colour)
	embed = discord.Embed(
	    title='', description='', color=ctx.author.top_role.colour)
	embed.add_field(
	    name=':ping_pong: Pong!',
	    value=f'Bot Latency is {ping}ms.',
	    inline=False)
	pinging = await ctx.send(embed=ping1)
	await asyncio.sleep(1)
	await pinging.edit(embed=ping2)
	await asyncio.sleep(1)
	await pinging.edit(embed=ping3)
	await asyncio.sleep(1)
	await pinging.edit(embed=embed)
 
@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
    
@client.command()
@commands.has_permissions(manage_roles=True)
async def setupmute(ctx):
  '''➜  Setup for Mute Command'''
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  if role is not None:
    await ctx.send("Role already created.")
    for channel in ctx.guild.channels:
      await channel.set_permissions(role, send_messages=False)
  else:
   newRole = await ctx.guild.create_role(name="Muted")
   await ctx.send("Setup activated.")
   for channel in ctx.guild.channels:
      await channel.set_permissions(newRole, send_messages=False)
   await ctx.send("Setup is complete.")
   
@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, *, role):
  ROLE = discord.utils.get(ctx.guild.roles, name=role)
  channel = discord.utils.get(ctx.guild.channels, name="mod-logs-python")
  if channel is None:
    await ctx.send("There doesn't seem to be a channel called `mod-logs-python` in this server! Please create it and try again.")
  else:
    if ROLE in member.roles:
      await member.remove_roles(ROLE)
      await ctx.channel.send(
		    f"Role **{role}** has been removed from {member.name}'s roles."
		)     

    else:
      await member.add_roles(ROLE)
      await ctx.channel.send(
		    f"Role **{role}** has been added to {member.name}'s roles.")  
@role.error
async def role_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send(error)

@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member = None, duration: int = None):
  '''
  ➜  Muted User With reason
  '''
  equal = 60 * duration
  role = discord.utils.get(ctx.guild.roles,     name="Muted")
  if role is not None:
   if duration == None:
    await member.add_roles(role)
    await ctx.send(f"*{member.mention} has been muted.")
   else:
    await ctx.send(f"*{member.mention} has been muted for {duration} minute.*")
    await member.add_roles(role)
    await asyncio.sleep(equal)
    await member.remove_roles(role)
  else:
      await ctx.send("Please run the setup first by using `[prefix]setupmute`.")
@mute.error
async def mute_error(ctx,error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send(error)
  

@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member = None):
  '''
  ➜  unmute who muted users
  '''
  await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
  await ctx.send(f"<a:ac:713181919436603435> *{member} Already To Unmuted!*.")

@client.command(name="lock")
@commands.has_permissions(manage_channels=True)
async def lock(ctx, *, name = None):
  '''
  ➜  locked channels
  '''
  overwrite = discord.PermissionOverwrite()
  overwrite.send_messages = False
  xyz = discord.utils.get(ctx.guild.channels, name="mod-logs-python")
  if xyz is not None:
    if name == None:
        role = ctx.guild.default_role
        await xyz.send(f"Channel **{ctx.channel}** has been locked.\nMod: {ctx.author}")
        await ctx.channel.set_permissions(role, overwrite=overwrite)
        await ctx.send(f"**Channel has been locked.**")
    else:
        await xyz.send(f"Channel **{name}** has been locked.\nMod: {ctx.author}")
        channel = discord.utils.get(ctx.guild.channels, name=name)
        role = ctx.guild.default_role
        await channel.set_permissions(role, overwrite=overwrite)
        await ctx.send(f"Channel **{name}** has been locked.")
        await channel.send("**Channel has been locked.**")
  else:
    await ctx.send("There doesn't seem to be a channel called `mod-logs-python` in this server. Please create it an try again.")
@lock.error
async def lock_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send(error)
    
@client.command()
async def getHelp(ctx):
  '''
  ➜  Give all prefix (info)
  '''
  await ctx.send("<a:Betol:712209577298624565> Here My Prefix!")
  await ctx.send("**Invite me!**")
  await ctx.send("```https://bit.ly/2TL4e1k```")
  await ctx.send("```My prefix is Py!```""```Thanks for using me!```""```Made by Python and Minho Newt Uwu#2144```""```Type Py!help for list command!```")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'<a:sngbgsd:712993968924655686> WELCOME **{member.name}**! ```Hi, welcome to My Guild and My Nice Server! We all happy when u joinned! Please read announcement and Keep enjoy!```'
    )
    
@client.command(name="unlock")
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, name = None):
  '''
  ➜  Unlocked channels
  '''
  overwrite = discord.PermissionOverwrite()
  overwrite.send_messages = True
  overwrite.read_messages = True
  overwrite.attach_files = False
  role = ctx.guild.default_role
  xyz = discord.utils.get(ctx.guild.channels, name="mod-logs-python")
  if xyz is not None:
    if name == None:
      await xyz.send(f"Channel **{ctx.channel}** has been unlocked.\nMod: {ctx.author}")
      await ctx.channel.set_permissions(role, overwrite=overwrite)
      await ctx.send("**Channel has been unlocked.**")
    else:
      channel = discord.utils.get(ctx.guild.channels, name=name)
      await xyz.send(f"Channel **{name}** has been unlocked.\nMod: {ctx.author}")
      await channel.set_permissions(role, overwrite=overwrite)
      await channel.send("**Channel has been unlocked.**")
      await ctx.send(f"Channel **{name}** has been unlocked.")
  else:
    await ctx.send("There doesn't seems to be a channel called `mod-logs-python`mod-logs-python`` in this server. Please create it and try again.")
@unlock.error
async def unlock_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send(error)
   
@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, amount: int):
  """➜  Slowmode feature"""
  await ctx.channel.edit(slowmode_delay=amount)
  await ctx.send(f"**Set the slowmode of this channel to {amount} seconds <a:d0n3:712988326390530090>**")		

    
@bot.command(name='kick', help='➜  For getting rid of annoyances')
async def kick(ctx, usr: discord.Member, *, rsn=''):
    try:
        if ctx.author.guild_permissions.kick_members:
            await usr.kick
            await ctx.send('That fool just got kicked from my swamp!')
            await ctx.send(file=discord.File('WhatAreYouDoingInMySwamp.gif'))
        else:
            await ctx.send('Sorry, you do not have permissions to do that!')
    except discord.errors.Forbidden:
        await ctx.send('Sorry, but I do not have permission to kick.')
        
@client.command()
async def userroles(ctx, member: discord.Member = None):
  '''
  ➜  Give info about u roles
  '''
  if member == None:
    member = ctx.author     
    roles = [role for role in member.roles]

    embed = discord.Embed(title=f"{member.name}'s roles")
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    await ctx.send(embed=embed)
  else:
    roles = [role for role in member.roles]

    embed = discord.Embed(title=f"{member.name}'s roles")
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    await ctx.send(embed=embed)
    
@bot.command(pass_context=True)
async def roleinfo(ctx, *,role: discord.Role = None):
    """➜  Info about a role"""
    if role == None:
        await ctx.send(":x: | Role not found")
    else:
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Role Name", value = format(role.name))
        embed.add_field(name = "Role ID", value = format(role.id))
        embed.add_field(name = "For Guild", value = format(role.guild))
        embed.add_field(name = "Hoist", value = format(role.hoist))
        embed.add_field(name = "Role Position", value = format(role.position))
        embed.add_field(name = "Mentionable Role", value = format(role.mentionable))
        embed.add_field(name = "Role Created At", value = format(role.created_at))
        await ctx.send(embed = embed)

        
@client.command(aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
  """➜  Clear mesages with limit : 100"""
  channel = discord.utils.get(ctx.guild.channels, name="mod-logs-python")
  if channel is None:
    await ctx.send("There doesn't seem to be a channel called `mod-logs-python` in this server! Please create it and try again.")
  elif amount > 300:
    await ctx.send("The amount is too big. Please clear below 300 message.")  
  else:    
    await ctx.channel.purge(limit=amount + 1)
    embed = discord.Embed(color=ctx.author.top_role.colour, title=f':ballot_box_with_check: {ctx.author.name} deleted {amount} message')
    em = discord.Embed(title="Cleared Message Report", color = ctx.author.colour, timestamp=ctx.message.created_at)
    em.add_field(name=f'Mod:', value=ctx.author, inline=False)
    em.add_field(name='Message Cleared:', value=amount, inline=False)
    em.add_field(name='Channel:', value=ctx.channel, inline=False)
    await channel.send(embed=em)
    lol = await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await lol.delete()

@client.command(aliases=["purges"])
@commands.has_permissions(manage_messages=True)
async def clears(ctx, amount: int):
  """➜  Clears messages with limit : 300"""
  channel = discord.utils.get(ctx.guild.channels, name="mod-logs-python")
  if channel is None:
    await ctx.send("There doesn't seem to be a channel called `mod-logs-python` in this server! Please create it and try again.")
  elif amount > 300:
    await ctx.send("The amount is too big, please clear below 300 message.")  
  else:
    embed = discord.Embed(
        title='Cleared Messages Reogs-pythont',
        description='',
        color=ctx.message.author.top_role.colour,
        timestamp=ctx.message.created_at)
    embed.add_field(name=f'Mod:', value=(author), inline=False)
    embed.add_field(name='Messages Cleared:', value=(amount), inline=False)
    embed.add_field(name='Channel:', value=ctx.channel, inline=False)
    channel
    await channel.send(embed=embed)
    await ctx.channel.purge(limit=amount + 1)
    embed = discord.Embed(color=ctx.author.top_role.colour, title=f':ballot_box_with_check: {ctx.author.name} deleted {amount} message')
    lol = await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await lol.delete()

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send(error)

@client.event
async def on_member_update(before, after):
    channel = discord.utils.get(before.guild.text_channels, name="mod-logs-python")
    roles = [role for role in before.roles]
    roless = [role for role in after.roles]

    if before.roles != after.roles:
          embed = discord.Embed(color=before.colour, description=f"{before} - Updated role <a:pinWoe:715030587349663864>")
          embed.set_thumbnail(url=f"{before.avatar_url}")
          embed.add_field(name=f"Before ( {len(before.roles)} ) :", value=" ".join([role.mention for role in roles]))
          embed.add_field(name=f"After ( {len(after.roles)} ) :", value=" ".join([role.mention for role in roless]))
          embed.set_footer(text=f"Made by Minho Newt UwU#2144 | {datetime.datetime.now()}")
          await channel.send(embed=embed)
    elif channel is None:
        return
    else:
        return
      
@client.command()
async def serverinfo(ctx):

	embed = discord.Embed(
	    timestamp=ctx.message.created_at, color=ctx.author.top_role.colour)

	embed.set_footer(text=f"Made by Minho Newt uwu#2144") 
	embed.add_field(name="Guild Name:", value=ctx.guild.name, inline=False)
	embed.add_field(name="Guild ID:", value=ctx.guild.id, inline=False)
	embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=False)
	embed.add_field(name="Owner ID", value=ctx.guild.owner_id, inline=False)
	embed.add_field(
	    name="Server Region", value=ctx.guild.region, inline=False)
	embed.add_field(
	    name="Server Verification Level",
	    value=ctx.guild.verification_level,
	    inline=False)
	embed.add_field(
	    name="Server is large?", value=ctx.guild.large, inline=False)
	embed.add_field(
	    name="Created at", value=ctx.guild.created_at, inline=False)
	embed.add_field(
	    name="Roles", value='{}'.format(len(ctx.guild.roles)), inline=False)
	embed.add_field(
	    name="Member Count",
	    value=ctx.guild.member_count,
	    inline=False)    
	await ctx.send(embed=embed)
	
@client.command()
async def userinfo(ctx, member: discord.Member = None):
	if member == None:
		member = ctx.author
		roles = [role for role in member.roles]

		embed = discord.Embed(
		    colour=member.color, timestamp=ctx.message.created_at)

		embed.set_author(name=f"User Info - {member}")
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(
		    text=f"Requested by {ctx.author}",
		    icon_url=ctx.author.avatar_url,
		)

		embed.add_field(name="ID:", value=member.id, inline=False)
		embed.add_field(name="Server:", value=ctx.guild.name, inline=False)
		embed.add_field(
		    name="Activity:", value=member.activities, inline=False)
		embed.add_field(name="Nickname:", value=member.nick, inline=False)
		embed.add_field(name="Status:", value=member.status, inline=False)

		embed.add_field(
		    name="Created at:",
		    value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"),
		    inline=False)
		embed.add_field(
		    name="Joined at:",
		    value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"),
		    inline=False)

		embed.add_field(
		    name=f"Roles ({len(roles)})",
		    value=" ".join([role.mention for role in roles]),
		    inline=False)
		embed.add_field(
		    name="Top role", value=member.top_role.mention, inline=False)

		embed.add_field(name="Bot?", value=member.bot)

		await ctx.send(embed=embed)
	else:
		roles = [role for role in member.roles]

		embed = discord.Embed(
		    colour=member.color, timestamp=ctx.message.created_at)

		embed.set_author(name=f"User Info - {member}")
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(
		    text=f"Requested by {ctx.author}",
		    icon_url=ctx.author.avatar_url,
		)

		embed.add_field(name="ID:", value=member.id, inline=False)
		embed.add_field(name="Guild Name:", value=ctx.guild.name, inline=False)
		embed.add_field(
		    name="Activity:", value=member.activities, inline=False)
		embed.add_field(name="Nickname:", value=member.nick, inline=False)
		embed.add_field(name="Status:", value=member.status, inline=False)

		embed.add_field(
		    name="Created at:",
		    value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"),
		    inline=False)
		embed.add_field(
		    name="Joined at:",
		    value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"),
		    inline=False)

		embed.add_field(
		    name=f"Roles ({len(roles)})",
		    value=" ".join([role.mention for role in roles]),
		    inline=False)
		embed.add_field(
		    name="Top role", value=member.top_role.mention, inline=False)

		embed.add_field(name="Bot?", value=member.bot)

		await ctx.send(embed=embed)
		
@client.command(pass_context=True)
async def updates(ctx):
  """➜  Info about Updates The Bots"""
  embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Colour.blue())
  embed.set_author(name="Python Updates", icon_url="https://cdn.discordapp.com/avatars/696386680965562430/e7bb3840d9846c64520ed29c4eb565db.webp?size=1024")
  embed.add_field(name="System", value=f"**Python Version** : {platform.python_version()}\n**Discord.py Version** : {discord.__version__}\n**Operating system** : {platform.system()}\n**CPU Usage **: {psutil.cpu_percent()}%\n**CPU Count** : {psutil.cpu_count()}\n**Hosted on** : [repl.it](https://repl.it)")
  embed.set_footer(text="Made by Minho Newt uwuヅ#2144")
  await ctx.send(embed=embed)
    
@client.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member = None):
	if member == None:
		member = ctx.author
		embed = discord.Embed(title='This Your Avatar...', colour=member.color)

		embed.set_footer(
		    text=f"Made by Minho Newt Uwuヅ#2144", icon_url=ctx.author.avatar_url)
		embed.set_image(url=member.avatar_url)

		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title='This Your Avatar...', colour=member.color)

		embed.set_footer(
		    text=f"Made by Minho newt uwuヅ#2144", icon_url=ctx.author.avatar_url)
		embed.set_image(url=member.avatar_url)

		await ctx.send(embed=embed)

@bot.command(aliases=['yt'])
async def youtube(ctx, *, name):
  await ctx.send(hoversearch.search("url",f"{name}"))
	
@client.command(pass_context=True)
@commands.is_owner()
async def users(ctx):
	await ctx.send(
	    f"There are {ctx.guild.member_count} members in this server.")

import ast
import discord

from discord.ext import commands


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@client.command()
async def stats(ctx):
	embed = discord.Embed(title='Python Stats', color=ctx.author.top_role.colour)
	embed.add_field(name='Guilds', value=f'{len(bot.guilds)}', inline=True)
	embed.add_field(name='Users', value=f'{len(bot.users)}', inline=True)
	embed.add_field(
	    name="Support server",
	    value=f'[Link](https://discord.gg/cd947fD)',
	    inline=False)
	embed.set_footer(
	    text=(ctx.message.author.name) + " | Python's stats!",
	    icon_url=(ctx.message.author.avatar_url))
	await ctx.send(embed=embed)

@bot.command(help='➜ Giving greet messages')
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command(help='➜ Giving cat gif')
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    
@bot.command(help='➜ Giving info about the bot')
async def info(ctx):
    embed = discord.Embed(title="ツ About Me ツ", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<@552492140270452736>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<https://discord.com/api/oauth2/authorize?client_id=713971454089101332&permissions=0&scope=bot>)")

    await ctx.send(embed=embed)

keep_alive()  
client.loop.create_task(statuschange())
client.run('your token here')
