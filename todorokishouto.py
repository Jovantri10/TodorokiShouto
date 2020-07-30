import discord
import discordgames as Games
import client
import canvas as Painter
import asyncio
from discord import client
import json
import datetime
import logging
from utils import has_voted
from bs4 import BeautifulSoup
import urllib.request
import requests
import re                          
import os
from datetime import datetime as todoroki
from discord.utils import get
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
from discord.ext.commands import (Bot,BotMissingPermissions,bot_has_permissions)
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
import udpy
from udpy import UrbanClient
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
import deku as todo
import statcord
from deku import *


client = discord.Client
client = commands.Bot(
  command_prefix=[
        "Todo.",
        'todo.',
        '~>',
        "<@714330708365148190> ",
    ],
    owner_id=552492140270452736)
    #Set the command prefix to what you preferrint(f'Logged in as {bot.user.name} - {bot.user.id}')

bot = client
todoroki = bot
async def statuschange():
	while not client.is_closed():
		await bot.wait_until_ready(
		)  # Makes the bot wait until it's fully ready before the stuff below are ran
		await bot.change_presence(
		    status=discord.Status.dnd,
		    activity=discord.Activity(
		        type=discord.ActivityType.watching,
		        name=f"{len(bot.guilds)} Guild's | Find bug? Todo.bug",
		        url="https://www.twitch.tv/pkidz2123"))
		await asyncio.sleep(
		    8
		)  # Makes it wait another 8 seconds and then it'll go back to the top on playing because we used "while" which makes it look
		await bot.change_presence(
		    status=discord.Status.dnd,
		    activity=discord.Activity(
		        type=discord.ActivityType.listening,
		        name=f"Todoroki and Deku | Todo.help",
		        url="https://www.twitch.tv/pkidz2123"))
		await asyncio.sleep(8)

extensions = ['Cogs.vaan','Cogs.commands','Cogs.api','Cogs.utils','Cogs.ownerr','Cogs.help','Cogs.util','Cogs.stuff','Cogs.jishaku','Cogs.ksoft','Cogs.mod','Cogs.warn','Cogs.afk','Cogs.snipe','Cogs.images','Cogs.user','Cogs.Encoding','Cogs.misc commands','Cogs.membercount','Cogs.Members','Cogs.Owner']

if __name__ == '__main__':
	for extension in extensions:
		client.load_extension(extension)
    
def get_prefix(bot, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)
		
		return prefixes[str(message.guild.id)]

@bot.event
async def on_ready():
	ass = discord.Status.idle
	print('Ready.')
	await client.change_presence(status=ass)
	replit.clear()
	print(f'Logged in as {bot.user.name} - {bot.user.id}')
	bot.remove_command('help')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CheckAnyFailure):
    await ctx.send(f'Hm There is Error : \n ```{error}```')

def get_prefix(client, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

		return prefixes[str(message.guild.id)]

import statcord 

key = 'statcord.com-c9AeEy6Wic9clB5nIxH0'
api = statcord.Client(bot,key)
api.start_loop()

@bot.event
async def on_command(ctx, *args):
    y = bot.get_channel(713061501333798932)
    lo = bot.get_channel(736792598458531892)
    await lo.send(f"*```{ctx.author} | {ctx.author.id} |\nUse {ctx.command.name} Commands\n-----------------------------------------------```*")
    await y.send(f"```| ID : {ctx.author.id}\n| GUILD : {ctx.guild.id}\n| CHANNEL : {ctx.channel.id}\n| AUTHOR : {ctx.author}```")
    api.command_run(ctx)

@todoroki.command(helpinfo='Looks up a sequence of numbers', aliases=['numbers', 'integers'])
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

t = todoroki.command()
cd = 	commands.cooldown(1, 12, commands.BucketType.user)
owner = 552492140270452736

@bot.command()
@cd
async def bug(ctx, *, msg: str):
  own = bot.get_user(552492140270452736)
  lol = bot.get_channel(726671245621592175)
  serverinvite = await ctx.message.channel.create_invite(reason='Requested by '+str(ctx.message.author.name))
  color = discord.Color(value=0x00ff00)
  em = discord.Embed(color=color, title="Bug reported!")
  em.description = f"Bug : {msg}\nBug sent by {ctx.author}\nInvite : [Link]({serverinvite})"
  await lol.send(embed=em)
  await own.send(ctx.author.id)
  await ctx.send(
	    "Thanks for reporting that bug! We will send your report now!.")

@bot.command()
@cd
async def suggest(ctx, *, msg: str):
	"""Got a PROB? Tell us about it...  """
	o = ''.join(list(msg))
	invite = await ctx.message.channel.create_invite(reason='Requested by '+str(ctx.message.author.name))
	lol = bot.get_channel(726827658528161804)
	color = discord.Color(value=0x00ff00)
	em = discord.Embed(color=color, title="Suggestion!")
	em.description = f"Suggest : ***{o}***\nID : ***{ctx.author.id}***\nServer : [Invite]({invite})"
	em.set_footer(text=f"Suggest sent by {ctx.message.author}")
	await lol.send(embed=em)
	await ctx.send("Thanks for Your Suggest!.")

@todoroki.command(aliases=["trg"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def triggered(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://useless-api--vierofernando.repl.co/triggered?image='+str(ctx.author.avatar_url)+'&increment=5'.replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'vierofernando.png'))
  try:
    go = 'https://useless-api--vierofernando.repl.co/triggered?image='+str(ctx.message.mentions[0].avatar_url)+'&increment=5'.replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'vierofernando.png'))
  except Exception as e:
    await ctx.send(f"```404 ~> {e}```")

@t   
@cd   
async def ping(ctx):
  ping = client.latency
  ping = round(ping * 1000)
  await ctx.send("<:wipii:736786400069943398> Pong! `{} ms`".format(ping))

@todoroki.command(aliases=["copid","19"])
@cd 
async def covid(ctx, *args):
  if len(args)==0:
    cases = requests.get('https://disease.sh/v3/covid-19/all').json()["cases"]
    today = requests.get('https://disease.sh/v3/covid-19/all').json()["todayCases"]
    death = requests.get('https://disease.sh/v3/covid-19/all').json()["deaths"]
    dtoday = requests.get('https://disease.sh/v3/covid-19/all').json()["todayDeaths"]
    rec = requests.get('https://disease.sh/v3/covid-19/all').json()["recovered"]
    trec = requests.get('https://disease.sh/v3/covid-19/all').json()["todayRecovered"]
    act = requests.get('https://disease.sh/v3/covid-19/all').json()["active"]
    cri = requests.get('https://disease.sh/v3/covid-19/all').json()["critical"]
    popu = requests.get('https://disease.sh/v3/covid-19/all').json()["population"]
    embed = discord.Embed()
    embed.set_author(name="Covid Stats", icon_url="https://cdn.discordapp.com/attachments/721753102822277130/733695614843617350/691d9ddf630b9658d959075881715405.png")
    embed.add_field(name='Total Cases', value=f'**```{cases} cases```**')
    embed.add_field(name="Today Cases", value=f"**```{today}```**")
    embed.add_field(name="Total Deaths", value=f"**```{death}```**")
    embed.add_field(name="Deaths Today", value=f"**```{dtoday}```**")
    embed.add_field(name="Recovered Total", value=f"**```{trec}```**")
    embed.add_field(name="Active", value=f"**```{act}```**")
    embed.add_field(name="Critical", value=f"**```{cri}```**")
    embed.add_field(name="Population", value=f"**```{popu}```**")
    embed.add_field(name="Recovered Today", value=f"**```{rec}```**")
    embed.color = discord.Color.blue()
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721753102822277130/733695614843617350/691d9ddf630b9658d959075881715405.png")
    await ctx.send(embed=embed)
  try:
    cav = todo.urlify(' '.join(args))
    ca = requests.get(f'https://disease.sh/v3/covid-19/countries/'+str(cav)).json()["cases"]
    tca = requests.get(f'https://disease.sh/v3/covid-19/countries/'+str(cav)).json()["todayCases"]
    de = requests.get(f'https://disease.sh/v3/covid-19/countries/'+str(cav)).json()["deaths"]
    tre = requests.get(f'https://disease.sh/v3/covid-19/countries/'+str(cav)).json()["todayRecovered"]
    re = requests.get(f'https://disease.sh/v3/covid-19/countries/'+str(cav)).json()["recovered"]
    po = requests.get(f'https://disease.sh/v3/covid-19/countries/'+str(cav)).json()["population"]
    tde = requests.get(f'https://disease.sh/v3/covid-19/countries/'+str(cav)).json()["todayDeaths"]
    embed = discord.Embed(color = discord.Color.blue())
    embed.add_field(name="Population ", value=f"**```{po}```**")
    embed.add_field(name="Cases", value=f"**```{ca}```**")
    embed.add_field(name="Today Cases", value=f"**```{tca}```**")
    embed.add_field(name="Death", value=f"**```{de}```**")
    embed.add_field(name="Today Death", value=f"**```{tde}```**")
    embed.add_field(name="Today Recovered", value=f"**```{tre}```**")
    embed.add_field(name="Recovered", value=f"**```{re}```**")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721753102822277130/733695614843617350/691d9ddf630b9658d959075881715405.png")
    await ctx.send(embed=embed)
  except Exception:
    await ctx.send("Cant find country on list or there is no cases on that country")
    
@t 
@cd 
async def contributors(ctx):
  await ctx.send(f"<a:ncgaes:713235013809864774> ***SPECIAL THANKS***\n**```{bot.get_user(661200758510977084).name}#{bot.get_user(661200758510977084).discriminator} | {bot.get_user(271576733168173057).name}#{bot.get_user(271576733168173057).discriminator} | {bot.get_user(493768058012172288).name}#{bot.get_user(493768058012172288).discriminator} | {bot.get_user(524969551419670559).name}#{bot.get_user(524969551419670559).discriminator}```**")
  
@todoroki.command(aliases=["jpgif"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def jpegify(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://api.alexflipnote.dev/filter/jpegify?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'jpegify.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://api.alexflipnote.dev/filter/jpegify?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'jpegify.png'))
 
@todoroki.command(aliases=["snw"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def snow(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://api.alexflipnote.dev/filter/snow?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'snow.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://api.alexflipnote.dev/filter/snow?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'snow.png'))
 
@todoroki.command(aliases=["bisex"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def gay(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://api.alexflipnote.dev/filter/gay?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'gay.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://api.alexflipnote.dev/filter/gay?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'gay.png'))
 
@todoroki.command(aliases=["cmnst"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def communist(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://api.alexflipnote.dev/filter/communist?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'idontlikethis.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://api.alexflipnote.dev/filter/communist?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'idonlikethis.png'))
 
@t 
@cd 
async def fml(ctx):
  aq = requests.get('https://api.alexflipnote.dev/fml').json()["text"]
  await ctx.send(aq)

@todoroki.command(aliases=["plt"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def pixelate(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://api.alexflipnote.dev/filter/pixelate?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'pixelalex.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://api.alexflipnote.dev/filter/pixelate?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'pixelalex.png'))
 

@todoroki.command(aliases=["bdanw"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def bw(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://api.alexflipnote.dev/filter/b&w?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'bw.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://api.alexflipnote.dev/filter/b&w?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'bw.png'))
 
@todoroki.command(aliases=["blr"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def blur(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://api.alexflipnote.dev/filter/blur?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'blur.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://api.alexflipnote.dev/filter/blur?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'blur.png'))
    
@t 
@cd
async def invert(ctx):
  if len(ctx.message.mentions)==0:
    gola5 = 'https://nezumiyuiz.glitch.me/api/invert?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola5), 'bangepguigans.png'))
  else:
    s = 'https://nezumiyuiz.glitch.me/api/invert?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(s), 'bangpeguigans.png'))

@t 
@cd 
async def servercard(ctx):
  bots = [x for x in ctx.guild.members if x.bot]
  human = [x for x in ctx.guild.members if not x.bot]
  offline = [user for user in ctx.guild.members if user.status == discord.Status.offline]
  dnd = [user for user in ctx.guild.members if user.status == discord.Status.dnd]
  online = [user for user in ctx.guild.members if user.status == discord.Status.online]
  idle = [user for user in ctx.guild.members if user.status == discord.Status.idle]
  try:
    sc = f'https://useless-api--vierofernando.repl.co/servercard?icon={ctx.guild.icon_url}&name={ctx.guild}&date=2%20minutes%20ago&author=Todoroki%20Shouto&humans={len(human)}&bots={len(bots)}&roles={len(ctx.guild.roles)}&channels={len(ctx.guild.channels)}&boosters={ctx.guild.premium_subscribers or "0"}&tier={ctx.guild.premium_tier}&online={len(online)}'
    await ctx.send(file=discord.File(Painter.urltoimage(sc), 'servercard.png'))
  except Exception as e:
      await ctx.send(f"```404 ~> {e}```")

@t 
@cd
async def goat(ctx):
  await ctx.send(file=discord.File(Painter.urltoimage('https://placegoat.com/'+str(random.randint(500, 700))), 'goat.png'))

@t 
@cd 
async def snake(ctx):
  await ctx.send(file=discord.File(Painter.urltoimage('https://fur.im/snek/i/'+str(random.randint(1, 874))+'.png'), 'snek.png'))

@t
@cd 
async def iotd(ctx):
  data = todo.jsonisp('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')['images'][0]
  embed = discord.Embed( title=data['copyright'], url=data['copyrightlink'], color=discord.Color.from_rgb(201, 160, 112))
  embed.set_image(url='https://bing.com'+data['url'])
  await ctx.send(embed=embed)

@t 
@cd
async def trash(ctx):
  if len(ctx.message.mentions)==0: await ctx.send('Please mention someone!')
  else:
      async with ctx.message.channel.typing():
          av = ctx.message.author.avatar_url
          toTrash = ctx.message.mentions[0].avatar_url
          url='https://api.alexflipnote.dev/trash?face='+str(av).replace('webp', 'png')+'&trash='+str(toTrash).replace('webp', 'png')
          data = Painter.urltoimage(url)
          await ctx.send(file=discord.File(data, 'trash.png'))
@t 
@cd 
async def textimg(ctx, *args):
  if len(args)==0:
    await ctx.send("Input the text!")
  if len(' '.join(list(args)))>50:
    await ctx.send("The word is limit")
  else:
    async with ctx.message.channel.typing():
      txt = todo.urlify(' '.join(args))
      data = Painter.urltoimage('https://useless-api--vierofernando.repl.co/texttoimage?text='+str(txt))
      await ctx.send(file=discord.File(data, 'viero.png'))


@t 
@cd 
async def captchatxt(ctx, *args):
  async with ctx.message.channel.typing():
    if len(args)==0:
      await ctx.send("Input the Text!")
    else:
      capt = todo.urlify(' '.join(args))
      data = Painter.urltoimage('https://api.alexflipnote.dev/captcha?text='+str(capt))
      await ctx.send(file=discord.File(data, 'captcha.png'))
      
@t
@cd
async def serverinvite(ctx):
  if not ctx.message.author.guild_permissions.create_instant_invite:
     await ctx.send(':x: Sorry u dont have perms')
  else:
     serverinvite = await ctx.message.channel.create_invite(reason='Requested by '+str(ctx.message.author.name))
     await ctx.send('<a:load:713196760264212570> Succes! Link: **'+str(serverinvite)+'**')

@todoroki.command(aliases=["disg"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def disgusting(ctx):
  if len(ctx.message.mentions)==0:
    gola = 'https://useless-api--vierofernando.repl.co/disgusting?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola), 'vierofernando.png'))
  if len(ctx.message.mentions)==1:
    go = 'https://useless-api--vierofernando.repl.co/disgusting?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(go), 'vierofernando.png'))

@todoroki.command()
async def duck(ctx):
  await ctx.send(file=discord.File(Painter.urltoimage(todo.jsonisp('https://random-d.uk/api/v2/random?format=json')['url']), 'duck.png'))

@todoroki.command(aliases=["ftv"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def ferbtv(ctx):
  if len(ctx.message.mentions)==0:
    gy = 'https://useless-api--vierofernando.repl.co/ferbtv?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gy), 'vierofernando.png'))
  else:
    bbi = 'https://useless-api--vierofernando.repl.co/ferbtv?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(bbi), 'vierofernando.png'))

@todoroki.command(aliases=["art"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def artmeme(ctx):
  if len(ctx.message.mentions)==0:
    golam = 'https://useless-api--vierofernando.repl.co/art?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(golam), 'vierofernando.png'))
  else:
    uu = 'https://useless-api--vierofernando.repl.co/art?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(uu), 'vierofernando.png'))


@todoroki.command(aliases=["gray"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def grayscale(ctx):
  if len(ctx.message.mentions)==0:
    golat = 'https://useless-api--vierofernando.repl.co/grayscale?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(golat), 'vierofernando.png'))
  else:
    g = 'https://useless-api--vierofernando.repl.co/grayscale?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(g), 'vierofernando.png'))

@todoroki.command(aliases=["resp"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def respect(ctx):
  if len(ctx.message.mentions)==0:
    golay = 'https://useless-api--vierofernando.repl.co/respects?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(golay), 'vierofernando.png'))
  else:
    f = 'https://useless-api--vierofernando.repl.co/respects?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(f), 'vierofernando.png'))
  
@todoroki.command()    
@commands.cooldown(1, 5, commands.BucketType.user)
async def sepia(ctx):
  if len(ctx.message.mentions)==0:
    gola5 = 'https://nezumiyuiz.glitch.me/api/sepia?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola5), 'bangepguigans.png'))
  else:
    s = 'https://nezumiyuiz.glitch.me/api/sepia?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(s), 'bangpeguigans.png'))
  
@todoroki.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def baby(ctx):
  if len(ctx.message.mentions)==0:
    gola1 = 'https://useless-api--vierofernando.repl.co/baby?image='+str(ctx.author.avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(gola1), 'vierofernando.png'))
  else:
    b = 'https://useless-api--vierofernando.repl.co/baby?image='+str(ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
    await ctx.send(file=discord.File(Painter.urltoimage(b), 'jovangans.png'))

@t 
@cd 
async def achiv(ctx, *args):
  async with ctx.message.channel.typing():
    if len(args)==0:
      await ctx.send("Input the Text!")
    else:
      capt = todo.urlify(' '.join(args))
      data = Painter.urltoimage('https://api.alexflipnote.dev/achievement?text='+str(capt))
      await ctx.send(file=discord.File(data, 'alexcantik.png'))
      
@todoroki.command()
@commands.cooldown(1, 6, commands.BucketType.user)
async def catfact(ctx):
  cat = requests.get("https://some-random-api.ml/facts/cat").json()['fact']
  em = discord.Embed(title="<a:boosterinbgsd:712992968990130189> Cat Fact <a:boosterinbgsd:712992968990130189>", description=f"**```{cat}```**\n-CatFact", color=discord.Color.blue())
  await ctx.send(embed=em)

@todoroki.command()
@commands.cooldown(1, 6, commands.BucketType.user)
async def quote(ctx):
  quotetod = requests.get('https://quotes.herokuapp.com/libraries/math/random').text
  em = discord.Embed(title="Quote Today", description=f"{quotetod}", color=discord.Color.blue())
  await ctx.send(embed=em)

@has_voted()
@todoroki.command(helpinfo='Wikipedia summary', aliases=['w', 'wiki'])
@commands.cooldown(1, 4, commands.BucketType.user)
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

@bot.event
async def on_guild_join(guild):
  lol = bot.get_channel(726676707226157076)
  em = discord.Embed(color=discord.Color(value=0x00ff00))
  em.title = f"Todoroki kun bot has arrived in new guids!"
  em.description = f"<a:HatiMel:712209640750055464> Server Name : **{guild}**\n<a:HatiMel:712209640750055464> Server Count : {len(bot.guilds)} servers!"
  await lol.send(embed=em)

@bot.command(aliases=['topgg'])
async def vote(ctx):
	y = "You can vote me every 12 hours! Remember!"
	vote = "https://top.gg/bot/714330708365148190"
	embed = discord.Embed(
	    title=
	    "<a:verify10:698678441502965851> VOTE ME NOW <a:verify10:698678441502965851>"
	)
	embed.description = f"*{y}*\nWant vote me? Vote on here \n [Vote Me Now On Here :)]({vote})"
	embed.timestamp = ctx.message.created_at
	embed.color = discord.Color.blue()
	embed.set_footer(text=f"{ctx.author.name}")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await ctx.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
	lol = bot.get_channel(726827078543999099)
	em = discord.Embed(color=discord.Color(value=0xf44242))
	em.title = f"Todoroki Kun bot has been removed from guild"
	em.description = f"<a:Chekbaru:712209716645724221> Server : **{guild}**\n<a:Chekbaru:712209716645724221> Server Count : {len(bot.guilds)} Servers"
	await lol.send(embed=em)

@bot.command(aliases=["urb"])
@commands.is_nsfw()
@commands.cooldown(1, 3, commands.BucketType.user)
async def urban(ctx, *, arg=None):

	if arg == None:
		embederror = discord.Embed()
		embederror.title = ":x: Invalid argument"
		embederror.description = "**Todo.urban [search]**"
		embederror.color = discord.Color.red()
		return await ctx.send(embed=embederror)
	try:
		urban = UrbanClient()

		defs = urban.get_definition(arg)

		def0 = defs[0]

		def1 = defs[1]

		def2 = defs[2]

		def3 = defs[3]

		def4 = defs[4]

		embeds = [
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def0.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def1.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def2.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def3.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def4.definition,
		        color=discord.Color.green())
		]

		paginator = BotEmbedPaginator(ctx, embeds)

		await paginator.run()

	except Exception:

		await ctx.send(f"Can't find **{arg}** in Urban Dictionary.")

@client.command(aliases=['json'])
@commands.is_owner()
async def json2(ctx, json3: str):
	with open(f"{json3}.json", "r") as f:

		command = json.load(f)

		nicejson = pprint.pformat(command, indent=4, sort_dicts=True)
		nicejson2 = nicejson[:-1] + "\n}"
		nicejson3 = str(nicejson2).replace("'", '"')
		await ctx.send(f'```json\n{nicejson3}```')

@bot.command()
@commands.is_owner()
async def ay(ctx, *, msg: str):
	await ctx.send(msg)
	await ctx.message.delete()


@bot.command()
async def say(ctx, *, msg: str):
	await ctx.send(msg)


@bot.command()
@commands.is_owner()
async def connect(ctx, type=None):

	if type == "serv":
		ser = len(bot.guilds)
		await ctx.send(f'Am connected to {ser} servers')
	elif type == "user":
		user = len(bot.users)
		await ctx.send(f'Am connected to {user} users')
	elif type == None:
		embed = discord.Embed(title="CONNECTED")
		embed.color = discord.Color.blue()
		s = "Van connect serv"
		u = "Van connect user"
		embed.description = f"{s}\n{u}"
		await ctx.send(embed=embed)


@bot.command(aliases=['bot'])
@commands.is_owner()
async def reboot(ctx):
	await ctx.send('<a:fastdance3:712218698248880158> Restarting....')
	os.execv(sys.executable, [sys.executable] + sys.argv)


@client.command()
@commands.is_owner()
async def pip(ctx, module: str):

	subprocess.check_call(["python3.8", "-m", "pip", "install", module])
	await ctx.send('Installing module, please wait...')
	asyncio.sleep(5)

	output = subprocess.getoutput(f"python3.8 -m pip install {module}")
	await ctx.send(f"Output:\n```{output}```")

@has_voted()
@bot.command(helpinfo='Searches for YouTube videos', aliases=['yt'])
@commands.cooldown(1, 4, commands.BucketType.user)
async def youtube(ctx, *, query: str):
	'''
    Uses YouTube Data v3 API to search for videos
    '''
	req = requests.get((
	    'https://www.googleapis.com/youtube/v3/search?part=id&maxResults=1'
	    '&order=relevance&q={}&relevanceLanguage=en&safeSearch=moderate&type=video'
	    '&videoDimension=2d&fields=items%2Fid%2FvideoId&key=').format(query) +
	                   os.environ['YOUTUBE_API_KEY'])
	await ctx.send('**Video URL: https://www.youtube.com/watch?v={}**'.format(
	    req.json()['items'][0]['id']['videoId']))


start_time = time.time()

bot.launch_time = datetime.datetime.utcnow()


@bot.command(aliases=['up', 'upt'])
@commands.is_owner()
async def uptime(ctx):
	delta_uptime = datetime.datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	await ctx.send(
	    f"<a:d0n3:712988326390530090> I am online since <a:d0n3:712988326390530090> ```{days}d, {hours}h, {minutes}m, {seconds}s```"
	)


@bot.command(helpinfo='For when plain text just is not enough')
async def emojify(ctx, *, text: str):
	'''
    Converts the alphabet and spaces into emoji
    ''' ""
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
			await author.send('`' + emojified + '`')


@bot.command(
    helpinfo='Shows MC account info, skin and username history',
    aliases=['skin', 'mc'])
async def minecraft(ctx, username='Van'):
	'''
   Shows MC account info, skin and username history
    '''
	uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.
	                    format(username)).json()['id']

	url = json.loads(
	    base64.b64decode(
	        requests.get(
	            'https://sessionserver.mojang.com/session/minecraft/profile/{}'
	            .format(uuid)).json()['properties'][0]['value']).decode(
	                'utf-8'))['textures']['SKIN']['url']

	names = requests.get(
	    'https://api.mojang.com/user/profiles/{}/names'.format(uuid)).json()
	history = "**Name History:**\n"
	for name in reversed(names):
		history += name['name'] + "\n"

	await ctx.send('**Username: `{}`**\n**Skin: {}**\n**UUID: {}**'.format(
	    username, url, uuid))

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def image(ctx, *, word):
	linkWord = word.replace(' ', '+')
	url = "https://imgur.com/search/time?q=" + linkWord + "&qs=thumbs"
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page.read(), "html.parser")
	imgLinkList = soup.find_all("a", {"class": "image-list-link"})
	print(len(imgLinkList))
	imgLink = imgLinkList[random.randrange(0, len(imgLinkList))]
	#imgLink = imgLink.get("href")
  #imgLink = imgContainerLink.find("img").get("src")
 # await client.say(imgLink.replace("//i.imgur.com/","https://i.imgur.com/"))
	await ctx.send("https://imgur.com/" + imgLink)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def googling(ctx, *, word):
	definition = ""
	linkWord = word.replace(' ', '+')
	url = 'https://www.wordnik.com/words/' + linkWord
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page.read(), "html.parser")
	definition = soup.select_one(
	    '.active > h3:nth-child(1)').text + "\n\n" + soup.select_one(
	        ".active > ul:nth-child(2) > li:nth-child(1)").text
	await ctx.send("**" + word + "\n\n" + definition + "**")


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


@bot.command(aliases=['run', 'eval', 'e'])
@commands.is_owner()
@commands.cooldown(1, 3, commands.BucketType.user)
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
	await ctx.send(f"<a:boosterinbgsd:712992968990130189> OUTPUT :\n**```{result}```**")


@bot.command()
@commands.is_owner()
async def Myserver(ctx):
	servers = []
	for x in client.guilds:
		Add = "\n"
		New = str(x.name)
		Final = str(New + Add)
		servers.append(Final)
		One_String = " ".join(servers)
		embed = discord.Embed(
		    colour=discord.Colour.blue(), timestamp=datetime.datetime.now())
		embed.set_footer(text='Thanks to xEnder#0001 for helping')
		embed.add_field(
		    name=f"Servers: {len(bot.guilds)}", value=One_String, inline=False)
	await ctx.send(embed=embed)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
	brooklyn_99_quotes = [
	    'I\'m the human form of the 💯 emoji.',
	    'Bingpot!',
	    ('Cool. Cool cool cool cool cool cool cool, '
	     'no doubt no doubt no doubt no doubt.'),
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

@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member = None):
	'''
  ➜  unmute who muted users
  '''
	await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
	await ctx.send(f"<a:ac:713181919436603435> *{member} Already To Unmuted!*."
	               )

@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, amount: int):
	"""➜  Slowmode feature"""
	await ctx.channel.edit(slowmode_delay=amount)
	await ctx.send(
	    f"**Set the slowmode of this channel to {amount} seconds <a:d0n3:712988326390530090>**"
	)


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
		embed.add_field(
		    name=f"Roles ({len(roles)})",
		    value=" ".join([role.mention for role in roles]))
		await ctx.send(embed=embed)
	else:
		roles = [role for role in member.roles]

		embed = discord.Embed(title=f"{member.name}'s roles")
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(
		    name=f"Roles ({len(roles)})",
		    value=" ".join([role.mention for role in roles]))
		await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def roleinfo(ctx, *, role: discord.Role = None):
	"""➜  Info about a role"""
	if role == None:
		await ctx.send(":x: | Role not found")
	else:
		colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
		colour = int(colour, 16)
		embed = discord.Embed(
		    colour=discord.Colour(value=colour),
		    timestamp=datetime.datetime.utcnow())
		embed.add_field(name="Role Name", value=format(role.name))
		embed.add_field(name="Role ID", value=format(role.id))
		embed.add_field(name="For Guild", value=format(role.guild))
		embed.add_field(name="Hoist", value=format(role.hoist))
		embed.add_field(name="Role Position", value=format(role.position))
		embed.add_field(
		    name="Mentionable Role", value=format(role.mentionable))
		embed.add_field(name="Role Created At", value=format(role.created_at))
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
		await ctx.send(embed=embed)


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
	embed = discord.Embed(
	    title='Python Stats', color=ctx.author.top_role.colour)
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

@bot.command(help='➜ Giving info about the bot')
async def info(ctx):
	embed = discord.Embed(
	    title="ツ About Me ツ",
	    description="Nicest bot there is ever.",
	    color=0xeee657)

	# give info about you here
	embed.add_field(name="Author", value="<@552492140270452736>")

	# Shows the number of servers the bot is member of.
	embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

	# give users a link to invite thsi bot to their server
	embed.add_field(
	    name="Invite",
	    value=
	    "[Invite link](<https://discord.com/api/oauth2/authorize?client_id=713971454089101332&permissions=0&scope=bot>)"
	)

	await ctx.send(embed=embed)


keep_alive()
client.loop.create_task(statuschange())
client.run(os.environ.get("BABI"))
