import discord
from discord.ext import commands
import os
import pyfiglet
import heapq
import pkg_info
from pkg_info import get_pkg_info
import pyshorteners
import nekos
import danksearch
import praw
import wikipedia
import json
import websocket
import psutil
import time
import random
import asyncio
import requests
import bs4
from bs4 import BeautifulSoup
from googletrans import Translator
import datetime
import platform

bot = commands.Bot(command_prefix="d/")

bot.launch_time = datetime.datetime.utcnow()
  
def apiresponses():
  
  ws = websocket.WebSocket() # Initalize websocket
  
  start_time=time.time()
  
  ws.connect("wss://gateway.discord.gg/?v=6&encoding=json") # Connect to host url
  
  ws.send("ping")
  
  result = ws.recv()
  
  response_time=time.time() - start_time
  
  ping = round(response_time * 1000)
  
  return ping

def apiresponse():
  
  ws = websocket.WebSocket() # Initalize websocket
      
  ws.connect("wss://gateway.discord.gg/?v=6&encoding=json") # Connect to host url
      
  ws.send("ping")
      
  result = ws.recv()
      
  fuck_you = time.time()
      
  response_time = time.time() - fuck_you
      
  fuck_you_too = str(response_time)[0:3]
      
  return fuck_you_too

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')

start_time = time.time()

class Command(commands.Cog):
    
    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def f(self, ctx, type = None):

      file = open("f.json", "r")

      load = json.load(file)

      files = open("useful.json", "r")

      loads = json.load(files)

      if not "global-respecc" in loads:

        loads["global-respecc"] = 0

      msg = "```"

      msg += "F Leaderboard\n"

      if type == "leaderboard":

        top_ten = heapq.nlargest(10, load)

        highscore = sorted(top_ten, key=lambda x: load[x].get("respecc", 0), reverse = True)

        for number, user in enumerate(highscore):

          respecc = "{:,}".format(load[user].get("respecc", 0))

          member = await self.bot.fetch_user(user)

          msg += "\n{} - {} has paid their respect {} times.".format(number + 1, member.name, respecc)

        msg += "\n\n{} respects have been paid globally.".format(loads["global-respecc"])

        msg += "```"

        await ctx.send(msg)

      else:

        if not str(ctx.author.id) in load:

          load[str(ctx.author.id)] = {}

        if not "global-respecc" in loads:

          loads["global-respecc"] = 0

        if not "respecc" in load[str(ctx.author.id)]:

          load[str(ctx.author.id)]["respecc"] = 0

        load[str(ctx.author.id)]["respecc"] += 1
        
        loads["global-respecc"] += 1

        dumps = open("f.json", "w")

        json.dump(load, dumps, indent = 4)

        dumpss = open("useful.json", "w")

        json.dump(loads, dumpss, indent = 4)

        await ctx.message.add_reaction("🙏")
        
    @commands.command(name = "channel-members")
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def channelmem(self, ctx):
      
      try:
      
        if len(ctx.message.channel_mentions) > 0:
        
          channel = ctx.message.channel_mentions[0]
        
          embed = discord.Embed()
          
          embed.timestamp = ctx.message.created_at
          
          embed.set_author(name = "Members that can see {}".format(channel.name))
          
          embed.description = "\n".join([user.mention for user in channel.members])
        
          embed.color = discord.Color.blue()
          
          await ctx.send(embed = embed)
          
        else:
          
          channel = ctx.channel
          
          embed = discord.Embed()
          
          embed.timestamp = ctx.message.created_at
          
          embed.set_author(name = "Members that can see {}".format(channel.name))
          
          embed.description = "\n".join([user.mention for user in channel.members])
        
          embed.color = discord.Color.blue()
          
          await ctx.send(embed = embed)
          
      except discord.HTTPException:
        
        embed = discord.Embed()

        embed.description = ":x: There's too many members to fit in the embed!"

        embed.color = discord.Color.red()

        await ctx.send(embed = embed)
        
      else:
        
        pass
    
    @commands.command(name = "first-message")
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def firstmessage(self, ctx):
      
      if len(ctx.message.channel_mentions) > 0:
        
        channel = ctx.message.channel_mentions[0]
        
        async for message in channel.history(limit = 1, oldest_first = True):
          
          embed = discord.Embed()

          embed.timestamp = ctx.message.created_at

          embed.color = discord.Color.blue()

          embed.set_author(name = "First message in {}".format(channel.name))
          
          embed.description = "[Jump to message]({})".format(message.jump_url)
          
          embed.add_field(name = "Author", value = message.author, inline = False)

          embed.add_field(name = "Message", value = message.content, inline = False)
          
          embed.add_field(name = "Message Creation Date", value = message.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
          
          embed.add_field(name = "ID", value = message.id, inline = False)

          await ctx.send(embed = embed)
          
      else:
        
        channel = ctx.channel
        
        async for message in channel.history(limit = 1, oldest_first = True):
          
          embed = discord.Embed()
  
  
          embed.timestamp = ctx.message.created_at
  
          embed.color = discord.Color.blue()
 
          embed.set_author(name = "First message in {}".format(channel.name))
          
          embed.description = "[Jump to message]({})".format(message.jump_url)

          embed.add_field(name = "Author", value = message.author, inline = False)

          embed.add_field(name = "Message", value = message.content, inline = False)
          
          embed.add_field(name = "Message Creation Date", value = message.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
          
          embed.add_field(name = "ID", value = message.id, inline = False)

          await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def finduser(self, ctx, *, rolename = None):

      if rolename == None:

        errorembed = discord.Embed()

        errorembed.title = ":x: Invalid argument"

        errorembed.description = "**Todo.members <mention role / role name>**"

        errorembed.color = discord.Color.red()

        return await ctx.send(embed = errorembed)

      try:

        if len(ctx.message.role_mentions) > 0:

          role = ctx.message.role_mentions[0]

          embed = discord.Embed()

          embed.set_author(name = "Members in {}".format(role.name))

          embed.description = "\n".join([user.mention for user in role.members])

          embed.color = role.color

          embed.timestamp = ctx.message.created_at

          await ctx.send(embed = embed)

        else:

          roles = [role for role in ctx.guild.roles if role.name.lower().startswith(rolename.lower())]

          role = roles[0]

          embed = discord.Embed()

          embed.set_author(name = "Members in {}".format(role.name))

          embed.description = "\n".join([user.mention for user in role.members])

          embed.color = role.color

          embed.timestamp = ctx.message.created_at

          await ctx.send(embed = embed)

      except discord.HTTPException:

        embed = discord.Embed()

        embed.description = " There's too many members to fit in the embed!"

        embed.color = discord.Color.red()

        await ctx.send(embed = embed)

      except IndexError:

        embed = discord.Embed()

        embed.description = " I couldn't find that role."

        embed.color = discord.Color.red()

        await ctx.send(embed = embed)

      else:

        pass
    @commands.command(name = "channel-info")
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def channelinfo(self, ctx, *, channelname = None):

      if channelname == None:

        errorembed = discord.Embed()

        errorembed.title = " Invalid argument"
 
        errorembed.description = "**Todo.channel-info <mention channel / channel name>**"

        errorembed.color = discord.Color.red()

        return await ctx.send(embed = errorembed)

      try:

        if len(ctx.message.channel_mentions) > 0:

          channel = ctx.message.channel_mentions[0]

          embed = discord.Embed()

          embed.set_author(name = channel.name)

          embed.color = discord.Color.blue()

          embed.timestamp = ctx.message.created_at

          embed.add_field(name = "ID", value = channel.id, inline = False)

          if channel.topic:

            embed.add_field(name = "Topic", value = str(channel.topic), inline = False)

          else:

            embed.add_field(name = "Topic", value = "None", inline = False)

          embed.add_field(name = "Position", value = channel.position, inline = False)

          embed.add_field(name = "Mention", value = "`{}`".format(channel.mention), inline = False)

          await ctx.send(embed = embed)

        else:

          channelss = [channel for channel in ctx.guild.channels if channel.name.lower().startswith(channelname.lower())]

          channels = channelss[0]

          embed = discord.Embed()

          embed.set_author(name = channels.name)

          embed.color = discord.Color.blue()

          embed.timestamp = ctx.message.created_at

          embed.add_field(name = "ID", value = channels.id, inline = False)

          if channels.topic:

            embed.add_field(name = "Topic", value = str(channels.topic), inline = False)

          else:

            embed.add_field(name = "Topic", value = "None", inline = False)

          embed.add_field(name = "Position", value = channels.position, inline = False)

          embed.add_field(name = "Mention", value = "`{}`".format(channels.mention), inline = False)

          await ctx.send(embed = embed)

      except IndexError:

        embed = discord.Embed()

        embed.description = " I couldn't find that channel."

        embed.color = discord.Color.red()

        await ctx.send(embed = embed)

      else:

        pass
    
    @commands.command()
    async def pp(self, ctx):
      
      return await ctx.send("This command has been disabled.")
      
      with open("useful.json", "r") as f:
        
        pp = json.load(f)

      pp_size = random.randint(1, 50)

      if not str(ctx.author.id) in pp:
   
        pp[str(ctx.author.id)] = pp_size

        with open("useful.json", "w") as f:
          
          json.dump(pp, f, indent = 4)

        await ctx.send("Your pp size has been measured! It's {}in!".format(pp_size))

      else:

        random_numbers = random.randint(1, 10)
    
        pp_size_murgn = pp[str(ctx.author.id)]

        if random_numbers > 5:

          await ctx.send("You can't change your pp size, it's still {}in.".format(pp_size_murgn))

        else:

          random_pp_size = random.randint(1, 50)

          pp[str(ctx.author.id)] = random_pp_size

          with open("useful.json", "w") as f:

            json.dump(pp, f, indent = 4)

          await ctx.send("Your pp size has changed to {}in!".format(random_pp_size))
          
    @commands.command()
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def asciify(self, ctx, *, arg = None):
      
      if arg == None:

        embed = discord.Embed(title = ":x: Invalid argument", description = "**Todo.asciify <words>**", color = discord.Color.red())

        return await ctx.send(embed = embed)

      result = pyfiglet.figlet_format(arg)

      await ctx.send(f"```{result}```")

    @commands.command(name = "apiping")
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def apipings(self, ctx):
      
      await ctx.send(f"API Latency : \n {apiresponses()} ms")
      
    @commands.command(name = "8ball")
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def ball(self, ctx, *, question = None):
      
      if question == None:
        
        embed = discord.Embed()
        
        embed.color = discord.Color.red()
        
        embed.title = ":x: Invalid argument"
        
        embed.description = "**Todo.8ball <question>**"
        
        return await ctx.send(embed=embed)
        
      answers = ["As I see it, yes", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes", "Yes - definitely", "You may rely on it."]
      
      em = discord.Embed()
      
      em.color = ctx.author.color
      
      em.timestamp = ctx.message.created_at
      
      em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
      
      em.set_footer(text = "🎱 8ball")
      
      em.add_field(name = "Question", value = question, inline = False)

      em.add_field(name = "Answer", value = random.choice(answers))
      
      await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def testmemory(self, ctx):
      tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
      await ctx.send(f"Used Memory: {used_m} - Total Memory: {tot_m}")

    @commands.command()
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def tinyurl(self, ctx, *, arg = None):
      if arg.startswith("http"):
        await ctx.trigger_typing()
        shortener = pyshorteners.Shortener()
        x = shortener.tinyurl.short(arg)
        embed = discord.Embed(description=f"[{x}]({x})", color = discord.Colour.blue())
        await ctx.send(embed=embed)
      else:
        error = discord.Embed(title=" :x: Invalid argument", description="**Todo.tinyurl <link>**", color = discord.Colour.red())
        await ctx.send(embed=error)
    @commands.command()
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def pypi(self, ctx, *, arg = None):
      
      if arg == None:
        
        embed = discord.Embed(title=" :x: Invalid argument", description="**Todo.pypi <name>**", color = discord.Color.red())
      
        return await ctx.send(embed = embed)
      
      try:
        
        pkg = get_pkg_info(arg)
      
        pkg_url = pkg.url
      
        pkg_name = pkg.name
      
        embed = discord.Embed()
      
        embed.description = f"[PyPI Package - {pkg_name}]({pkg_url})"
      
        embed.color = discord.Color.blue()
      
        embed.add_field(name="Package Version", value = pkg.version, inline = False)
      
        embed.add_field(name="Package Info", value = pkg.summary, inline=False)
      
        embed.set_author(name=pkg.author.name)
      
        embed.timestamp = ctx.message.created_at
      
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png")
      
        await ctx.send(embed=embed)
        
      except Exception:
        
        await ctx.send(f"Can't find **{arg}** in PyPI.")
        
      else:
        
        pass
    
    
    @commands.command(aliases=["av","ava"])
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def avatar(self, ctx, user: discord.Member = None):
      if user == None:
        
        embed = discord.Embed(color = discord.Colour.blue())
        embed.description = f"[Image Link]({ctx.author.avatar_url})"
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
      else:

        embed = discord.Embed(color = discord.Colour.blue())
        embed.description = f"[Image Link]({user.avatar_url})"
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 14, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, *, arg = None):
      if arg == None:
        error = discord.Embed(title="<:nos:654270016568557568> Invalid argument", description="**d/poll <message>**", color = discord.Colour.red())
        await ctx.send(embed=error)
      else:
        await ctx.message.delete()
        embed = discord.Embed(description=arg, timestamp=ctx.message.created_at, color=discord.Colour.blue())
        embed.set_author(name=f"{ctx.author.name} • Poll", icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("<:yes:654269889539866644>")
        await msg.add_reaction("<:nos:654270016568557568>")
    
    @commands.command(aliases=["tr"])
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def translate(self, ctx, type = None, *, arg = None):
      if type == None:
        error = discord.Embed(title="<:nos:654270016568557568> Invalid argument", description="**d/translate <language> <sentence>**", color = discord.Colour.red())
        await ctx.send(embed=error)
      elif arg == None:
         error = discord.Embed(title="<:nos:654270016568557568> Invalid argument", description="**Todo.translate <language> <sentence>**", color = discord.Colour.red())
         await ctx.send(error)
      else:
        embeds = discord.Embed(description="Translating..", color = discord.Colour.light_grey())
        msg = await ctx.send(embed=embeds)
        translator = Translator()
        translation = translator.translate(arg, dest=type)
        embed = discord.Embed(description=translation.text, color = discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"{translation.src} ~~> {translation.dest}")
        await msg.edit(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 14, commands.BucketType.user)
    async def about(self, ctx, type = None, member: discord.Member = None):
      if type == "user":
        if member == None:
            member = ctx.author
            roles= [role for role in member.roles]
            embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
            embed.set_author(name = member, icon_url = member.avatar_url)
            embed.set_footer(text = "ID: {}".format(member.id))
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Nickname", value=member.nick, inline=False)
            embed.add_field(name="Status", value=member.status, inline=False)
            embed.add_field(name="Registered", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
            embed.add_field(name="Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
            embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
            embed.add_field(name="Bot?", value=member.bot)
            
            await ctx.send(embed=embed)
	        
        else:
	          
	          roles= [role for role in member.roles]
	        
	          embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
	        
	          embed.set_author(name=f"{member}", icon_url=member.avatar_url)
	        
	          embed.set_thumbnail(url=member.avatar_url)
	       
	          embed.set_footer(text = "ID: {}".format(member.id))
	        
	          embed.add_field(name="Nickname", value=member.nick, inline=False)
	        
	          embed.add_field(name="Status", value=member.status, inline=False)
	        
	          embed.add_field(name="Registered", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
	        
	          embed.add_field(name="Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
	        
	          embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
	        
	          embed.add_field(name="Bot?", value=member.bot)
	        
	          await ctx.send(embed=embed)
	          
      elif type == "server":

            await self.bot.request_offline_members()

            offline = [user for user in ctx.guild.members if user.status == discord.Status.offline]

            dnd = [user for user in ctx.guild.members if user.status == discord.Status.dnd]

            online = [user for user in ctx.guild.members if user.status == discord.Status.online]

            idle = [user for user in ctx.guild.members if user.status == discord.Status.idle]
            
            embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Colour.blue())
	          
            embed.set_thumbnail(url=ctx.guild.icon_url)	      
	      
            embed.set_footer(text=f"ID: {ctx.guild.id}")
	      
            embed.set_thumbnail(url=ctx.guild.icon_url)
	      
            embed.add_field(name="Server Name", value=ctx.guild, inline=False)
	      
            embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=False)
	      
            embed.add_field(name="Server Region", value=ctx.guild.region, inline=False)
	      
            embed.add_field(name="Channels", value=len(ctx.guild.channels), inline=False)
	      
            embed.add_field(name="Emojis", value=len(ctx.guild.emojis), inline=False)
	      
            embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=False)
	      
            bots = [x for x in ctx.guild.members if x.bot]
	      
            human = [x for x in ctx.guild.members if not x.bot]
	      
            embed.add_field(name=f"Members [ All: {len(ctx.guild.members)} | Human: {len(human)} | Bots: {len(bots)} ]", value=f":black_circle: Offline: {len(offline)}\n:red_circle: DND: {len(dnd)}\n:yellow_circle: Idle: {len(idle)}\n:green_circle: Online: {len(online)}", inline=False)
	      
            embed.add_field(name="Server Creation Date", value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
	      
            await ctx.send(embed=embed)
	    
      elif type == "bot":

        embed = discord.Embed(color=discord.Colour.blue(), timestamp=ctx.message.created_at)
        embed.set_author(name="Dispenser", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="Bot's Owner", value="Shoto#2144", inline=False)
        embed.set_footer(text=f"ID: {bot.user.id}")
        embed.add_field(name='Guilds', value=f'{len(self.bot.guilds)}', inline=False)
        embed.add_field(name='Users', value=f'{len(self.bot.users)}', inline=False)
        embed.add_field(name="Library", value="discord.py", inline=False)
        embed.add_field(name="Shard ID", value=ctx.guild.shard_id, inline = False)
        delta_uptime = datetime.datetime.utcnow() - bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(embed=embed)
	          
      else:
	      
	      embed = discord.Embed(title="Command: Todo.about", description="`Todo.about user` or `Todo.about user <@user>`\n`Todo.about server`\n`Todo.about bot`", color = discord.Colour.blue())
	      
	      await ctx.send(embed=embed)
		
def setup(bot):
    bot.add_cog(Command(bot))
    
