import discord
import ast
import datetime, time
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
import json
import praw
import hoversearch
import traceback
import platform
import psutil
import base64
import json
import os
import random
from random import randint
import re
import signal
import sys
import urllib.parse
import datetime

from PIL import Image
import requests
      
client = discord.Client
client = commands.Bot(
    command_prefix=[
        "Py?",
        "Py!",
        "Pyt",
        "P",
        "<@your bot id> ",
    ],
    owner_id=552492140270452736,
    status=discord.Status.idle,
    activity=discord.Activity(
        type=discord.ActivityType.playing,
        name=f"With '''You name''' |Py?help",
        url="https://www.twitch.tv/pkidz2123"))  #Set the command prefix to what you prefer
        
bot = client
async def statuschange():
	while not client.is_closed():
		await bot.wait_until_ready(
		)  # Makes the bot wait until it's fully ready before the stuff below are ran
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.watching,
		        name=f"Maze runner",
		        url="https://www.twitch.tv/pkidz2123")
		)  # This line makes it change status to playing
		await asyncio.sleep(8)  # This line makes it waits 8 seconds
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.listening,
		        name=f"Rude word",
		        url="https://www.twitch.tv/pkidz2123")
		)  # This line makes it change status to listening
		await asyncio.sleep(
		    8
		)  # Makes it wait another 8 seconds and then it'll go back to the top on playing because we used "while" which makes it look
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.streaming,
		        name=f"With Thomas Brodie :)",
		        url="https://www.twitch.tv/pkidz2123"))
		await asyncio.sleep(8)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("with Python ツ"))

@bot.command(hidden=True, name='eval')
async def _eval(ctx, *, body: str):
   res = eval(message.content.split(P)[1])
   await ctx.send(res) 
    
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
          
@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, amount: int):
  await ctx.channel.edit(slowmode_delay=amount)
  await ctx.send(f"**Set the slowmode of this channel to {amount} seconds <a:d0n3:712988326390530090>**")		

@client.command()
@commands.is_owner()
async def SecretBot(ctx):
  await ctx.send(f"```Here My Token :v```")
  await ctx.send(f"**NzEzOTcxNDU0MDg5MTAxMzMy.XsyPnA.JlA0KYjyso0_jFa4_A1lLrGLZYk**")
  await ctx.send(f"```Link For Invited Me :```")
  await ctx.send(f"**https://discord.com/api/oauth2/authorize?client_id=713971454089101332&permissions=8&scope=bot**")

@client.command()
async def userroles(ctx, member: discord.Member = None):
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
  
@bot.command(helpinfo='Shows MC account info, skin and username history', aliases=['skin', 'mc'])
async def minecraft(ctx, username='P y t h o n'):
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
    
@bot.command(helpinfo='Searches the web (or images if typed first)', aliases=['search'])
async def google(ctx, *, searchquery: str):
    '''
    Should be a group in the future
    Googles searchquery, or images if you specified that
    '''
    searchquerylower = searchquery.lower()
    if searchquerylower.startswith('images '):
        await ctx.send('<https://www.google.com/search?tbm=isch&q={}>'
                       .format(urllib.parse.quote_plus(searchquery[7:])))
    else:
        await ctx.send('<https://www.google.com/search?q={}>'
                       .format(urllib.parse.quote_plus(searchquery)))
                       
@bot.command(pass_context=True)
async def roleinfo(ctx, *,role: discord.Role = None):
    """Info about a role"""
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

@bot.command(helpinfo='Wikipedia summary', aliases=['w', 'wiki'])
async def wikipedia(ctx, *, query: str):
    '''
    Uses Wikipedia APIs to summarise search
    '''
    sea = requests.get(
        ('https://en.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

    if sea['searchinfo']['totalhits'] == 0:
        await ctx.send('Sorry, your search could not be found.')
    else:
        for x in range(len(sea['search'])):
            article = sea['search'][x]['title']
            req = requests.get('https://en.wikipedia.org//w/api.php?action=query'
                               '&utf8=1&redirects&format=json&prop=info|images'
                               '&inprop=url&titles={}'.format(article)).json()['query']['pages']
            if str(list(req)[0]) != "-1":
                break
        else:
            await ctx.send('Sorry, your search could not be found.')
            return
        article = req[list(req)[0]]['title']
        arturl = req[list(req)[0]]['fullurl']
        artdesc = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/'+article).json()['extract']
        lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'], "%Y-%m-%dT%H:%M:%SZ")
        embed = discord.Embed(title='**'+article+'**', url=arturl, description=artdesc, color=0x3FCAFF)
        embed.set_footer(text='Wiki entry last modified',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.set_author(name='Wikipedia', url='https://en.wikipedia.org/',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.timestamp = lastedited
        await ctx.send('**Search result for:** ***"{}"***:'.format(query), embed=embed)
        
@bot.command(pass_context=True)
async def clear(ctx, number):
    '''Clears The Chat 2-100'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" in user_roles:
        mgs = []
        number = int(number)
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await bot.delete_messages(mgs)
	
@client.event
async def on_member_update(before, after):
    channel = discord.utils.get(before.guild.text_channels, name="mod-logs-python")
    roles = [role for role in before.roles]
    roless = [role for role in after.roles]

    if before.roles != after.roles:
          embed = discord.Embed(color=before.colour, description=f"{before}'s Roles Change")
          embed.set_author(name=f"{before} ({before.id})", icon_url=before.avatar_url)
          embed.add_field(name=f"Old roles ( {len(before.roles)} ) :", value=" ".join([role.mention for role in roles]))
          embed.add_field(name=f"New roles ( {len(after.roles)} ) :", value=" ".join([role.mention for role in roless]))
          embed.set_footer(text=f"Made by Minho Newt UwU ヅ#2144 | {datetime.datetime.now()}")
          await channel.send(embed=embed)
    elif channel is None:
        return
    else:
        return
      
@client.command()
async def serverinfo(ctx):

	embed = discord.Embed(
	    timestamp=ctx.message.created_at, color=ctx.author.top_role.colour)

	embed.set_footer(text=f"Made by Minho newt Uwuヅ#2144") 
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
  embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Colour.blue())
  embed.set_author(name="Python Updates", icon_url="https://cdn.discordapp.com/avatars/696386680965562430/e7bb3840d9846c64520ed29c4eb565db.webp?size=1024")
  embed.add_field(name="System", value=f"**Python Version** : {platform.python_version()}\n**Discord.py Version** : {discord.__version__}\n**Operating system** : {platform.system()}\n**CPU Usage **: {psutil.cpu_percent()}%\n**CPU Count** : {psutil.cpu_count()}\n**Hosted on** : [repl.it](https://repl.it)")
  embed.set_footer(text="Made by Minho Newt uwuヅ#2144")
  await ctx.send(embed=embed)
  
@client.command(aliases=["yt"])
async def youtube(ctx, *, name):
    await ctx.send(hoversearch.search("url", f"{name}"))
    
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
	
@client.command()
async def say(ctx, *, arg):
  if "@everyone" in arg:
    await ctx.send(f"You can't use this command to ping everyone!", delete_after=4)
    await ctx.message.delete()
  elif "@here" in arg:
    await ctx.send(f"You can't use this command to ping everyone!", delete_after=4)
    await ctx.message.delete()
  else:
    embed = discord.Embed(title=f"{arg}", timestamp=ctx.message.created_at)
    embed.color = discord.Colour.red()
    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    await ctx.message.delete()
@say.error
async def say_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send(error)
  else:
    await ctx.send(error) 
    
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

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="ツ About Me ツ", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<@552492140270452736>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<https://discord.com/api/oauth2/authorize?client_id=713971454089101332&permissions=0&scope=bot>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Here Lιѕт My Coммαɴd  ツ", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="Py?add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="Py?multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="Py?greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="Py?cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="Py?info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="Py?help", value="Gives this message", inline=False)
    embed.add_field(name="Py?stats", value="Gives a little info about stats bot", inline=False)
    embed.add_field(name="Py?updates", value="Gives a little info about updates the bots", inline=False)
    embed.add_field(name="Py?avatar", value="Gives a little information about your avatar", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
	ping = client.latency
	ping = round(ping * 1000)
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
 
keep_alive()  
client.loop.create_task(statuschange())
bot.run('DISCORD_TOKEN')
