import discord
from discord.ext import commands
import os
import pyfiglet
import heapq
import pkg_info
from pkg_info import get_pkg_info
import pyshorteners
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

reddit = praw.Reddit(client_id='GKg9xGGzV4vM9Q', client_secret='FutzuRgQ-0-fFTlOsbbDeJPdcUg', user_agent='Eternal City Bot by u/RedPhantomIRP')

start_time = time.time()

class Command(commands.Cog):
    
    def __init__(self, bot):

        self.bot = bot

    @commands.command(name = "channel-members")
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

        embed.description = "There's too many members to fit in the embed!"

        embed.color = discord.Color.red()

        await ctx.send(embed = embed)
        
      else:
        
        pass

    @commands.command()
    async def finduser(self, ctx, *, search = None):

      if search == None:

        errorembed = discord.Embed()

        errorembed.title = " Invalid argument"

        errorembed.description = "**Py!finduser <name>**"

        errorembed.color = discord.Color.red()

        return await ctx.send(embed = errorembed)

      embed = discord.Embed()

      namess = [user for user in ctx.guild.members if user.name.lower().startswith(search.lower())]

      names = namess[0:50]

      embed = discord.Embed()

      embed.color = discord.Color.blue()

      embed.timestamp = ctx.message.created_at

      embed.set_author(name = 'Members username that starts with "{}"'.format(search))

      embed.description = "\n".join([user.name + "#" + user.discriminator for user in names])      

      embed.set_footer(text = "Results are limited to 50 users.")

      await ctx.send(embed = embed)

    @commands.command()
    async def findrole(self, ctx, *, role = None):

      if len(ctx.message.role_mentions) > 0:

        ROLE = ctx.message.role_mentions[0]

        await ctx.send(ROLE.name)

      else:

        Role = [rOle for rOle in ctx.guild.roles if rOle.name.startswith(role)]

        await ctx.send(Role[0].name)

    @commands.command()
    async def members(self, ctx, *, rolename = None):

      if rolename == None:

        errorembed = discord.Embed()

        errorembed.title = " Invalid argument"

        errorembed.description = "**Py!members <mention role / role name>**"

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

        embed.description = "There's too many members to fit in the embed!"

        embed.color = discord.Color.red()

        await ctx.send(embed = embed)

      except IndexError:

        embed = discord.Embed()

        embed.description = "I couldn't find that role."

        embed.color = discord.Color.red()

        await ctx.send(embed = embed)

      else:

        pass

    @commands.command(name = "channel-info")
    async def channelinfo(self, ctx, *, channelname = None):

      if channelname == None:

        errorembed = discord.Embed()

        errorembed.title = "<:nos:654270016568557568> Invalid argument"

        errorembed.description = "**d/channel-info <mention channel / channel name>**"

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

        embed.description = "<:nos:654270016568557568> I couldn't find that channel."

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
    async def asciify(self, ctx, *, arg = None):
      
      if arg == None:

        embed = discord.Embed(title = "Invalid argument", description = "**Py!asciify <words>**", color = discord.Color.red())

        return await ctx.send(embed = embed)

      result = pyfiglet.figlet_format(arg)

      await ctx.send(f"```{result}```")

    @commands.command()
    async def rps(self, ctx, choice = None):
      
      choices = ["rock", "paper", "scissors"]

      xyz = random.choice(choices)

      if choice == "rock":

        if xyz == "rock":
                
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "It's a tie!"
          
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)

          await ctx.send(embed = embed)

        elif xyz == "paper":
                
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "You lose.."
          
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
        elif xyz == "scissors":
                
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "You win!"
      
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
      elif choice == "paper":

        if xyz == "rock":
          
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "You win!"
      
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
        elif xyz == "paper":
          
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "It's a tie!"
      
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
        elif xyz == "scissors":
          
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "You lose.."
      
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
      elif choice == "scissors":

        if xyz == "rock":
        
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "You lose.."
      
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
        elif xyz == "paper":
          
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "You win!"
      
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
        elif xyz == "scissors":
          
          embed = discord.Embed()
          
          embed.set_author(name = "Rock - Paper - Scissors")
          
          embed.color = discord.Color.blue()
      
          embed.timestamp = ctx.message.created_at
      
          embed.description = "It's a tie!"
      
          embed.add_field(name = "You", value = choice , inline = False)
      
          embed.add_field(name = "Donut", value = xyz)
      
          await ctx.send(embed = embed)
          
      else:
        
        embed = discord.Embed()
        
        embed.color = discord.Color.red()
      
        embed.title = "Invalid argument"
        
        embed.description = "**Py!rps <rock/paper/scissors>**"
        
        await ctx.send(embed = embed)
     
    @commands.command(name = "8ball")
    async def ball(self, ctx, *, question = None):
      
      if question == None:
        
        embed = discord.Embed()
        
        embed.color = discord.Color.red()
        
        embed.title = " Invalid argument"
        
        embed.description = "**Py!8ball <question>**"
        
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
    async def testmemory(self, ctx):
      tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
      await ctx.send(f"Used Memory: {used_m} - Total Memory: {tot_m}")

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    @commands.bot_has_permissions(manage_channels = True)
    async def counting(self, ctx, type = None):
      
      if type == "disable":
        
        with open("useful.json", "r") as f:
          
          count = json.load(f)
        
        if str(ctx.guild.id) in count:
        
          counting_channel = count[str(ctx.guild.id)]["counting-channel"]
          
          count.pop(str(ctx.guild.id))
        
          with open("useful.json", "w") as f:
          
            json.dump(count, f, indent = 4)
          
          channel = await self.bot.fetch_channel(counting_channel)
        
          await channel.delete()
        
          await ctx.send("Counting disabled.")
          
        else:
          
          await ctx.send("Counting wasn't enabled.")
      
      elif type == "enable":
      
        with open("useful.json", "r") as f:
        
          count = json.load(f)
        
        if not str(ctx.guild.id) in count:
          
          channel = await ctx.guild.create_text_channel("counting")
          
          count[str(ctx.guild.id)] = {}
        
          count[str(ctx.guild.id)]["counting-channel"] = channel.id
        
          count[str(ctx.guild.id)]["counter"] = 0
        
          with open("useful.json", "w") as f:
          
            json.dump(count, f, indent = 4)
          
          await ctx.send("Counting has been enabled.")
        
        else:
        
          await ctx.send("Counter is already enabled.")
    
      else:
        
        Embed = discord.Embed(title = "Command: d/counting", description = "`d/counting enable/disable`", color = discord.Color.blue())
        
        await ctx.send(embed=Embed)
    
    @commands.command()
    async def pypi(self, ctx, *, arg = None):
      
      if arg == None:
        
        embed = discord.Embed(title=" Invalid argument", description="**Py!pypi <name>**", color = discord.Color.red())
      
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
    
    @commands.command()
    async def tinyurl(self, ctx, *, arg = None):
      if arg.startswith("http"):
        await ctx.trigger_typing()
        shortener = pyshorteners.Shortener()
        x = shortener.tinyurl.short(arg)
        embed = discord.Embed(description=f"[{x}]({x})", color = discord.Colour.blue())
        await ctx.send(embed=embed)
      else:
        error = discord.Embed(title="<:nos:654270016568557568> Invalid argument", description="**d/tinyurl <link>**", color = discord.Colour.red())
        await ctx.send(embed=error)

    
    @commands.command(aliases=["av"])
    async def ava(self, ctx, user: discord.Member = None):
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
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, *, arg = None):
      if arg == None:
        error = discord.Embed(title="Invalid argument", description="**Py!poll <message>**", color = discord.Colour.red())
        await ctx.send(embed=error)
      else:
        await ctx.message.delete()
        embed = discord.Embed(description=arg, timestamp=ctx.message.created_at, color=discord.Colour.blue())
        embed.set_author(name=f"{ctx.author.name} • Poll", icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("<:yes:654269889539866644>")
        await msg.add_reaction("<:nos:654270016568557568>")
    
    @commands.command(aliases=["tr"])
    async def translate(self, ctx, type = None, *, arg = None):
      if type == None:
        error = discord.Embed(title="Invalid argument", description="**Py!translate <language> <sentence>**", color = discord.Colour.red())
        await ctx.send(embed=error)
      elif arg == None:
         error = discord.Embed(title="Invalid argument", description="**Py!translate <language> <sentence>**", color = discord.Colour.red())
         await ctx.send(error)
      else:
        embeds = discord.Embed(description="Translating..", color = discord.Colour.light_grey())
        msg = await ctx.send(embed=embeds)
        translator = Translator()
        translation = translator.translate(arg, dest=type)
        embed = discord.Embed(description=translation.text, color = discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Translated {translation.src} >> {translation.dest}")
        await msg.edit(embed=embed)
    
    @commands.command()
    async def meme(self, ctx):
	    await ctx.trigger_typing()
	    memes_submissions = reddit.subreddit('dankmemes').hot()
	    post_to_pick = random.randint(1, 100)
	    for i in range(0, post_to_pick):
		    submission = next(x for x in memes_submissions if not x.stickied)

	    embed = discord.Embed(title=f'{submission.title}', color=ctx.author.colour, url=submission.url)
	    embed.set_image(url=submission.url)
	    embed.add_field(name="Reddit r/dankmemes", value=f"By u/{str(submission.author)}")
	    all_comments = submission.comments
	    embed.set_footer(text=f"⬆️ {submission.ups} | 💬 {len(all_comments)}")
	    await ctx.send(embed=embed)
       
    @commands.command()
    async def about(self, ctx, type = None, member: discord.Member = None):
      if type == "user":
	        if member == None:
	          member = ctx.author
	          
	          roles= [role for role in member.roles]
	        
	          embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
	        
	          embed.set_author(name=f"{member}", icon_url=member.avatar_url)
	        
	          embed.set_thumbnail(url=member.avatar_url)
	        
	          embed.add_field(name="ID", value=member.id, inline=False)
	        
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
	       
	          embed.add_field(name="ID", value=member.id, inline=False)
	        
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
        embed.set_author(name="Todoroki Shouto", icon_url="https://cdn.discordapp.com/avatars/696661877631090739/4479b5df7063a6f409bd910fd1004b81.webp?size=1024")
        embed.add_field(name="Bot's Owner", value="Minho Newt Uwu#2144", inline=False)
        embed.set_footer(text="ID: 714330708365148190")
        embed.add_field(name='Guilds', value=f'{len(self.bot.guilds)}', inline=False)
        embed.add_field(name='Users', value=f'{len(self.bot.users)}', inline=False)
        embed.add_field(name="Library", value="discord.py", inline=False)
        embed.add_field(name="Shard ID", value=ctx.guild.shard_id, inline = False)
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed.add_field(name="Uptime", value=text, inline = False)
        with open("prefixes.json", "r") as f:

          prefixes = json.load(f)

        prefix = prefixes[str(ctx.guild.id)]

        embed.add_field(name = "Prefix", value = f"Default - `Py!`\nServer - `{prefix}`", inline = False)
        await ctx.send(embed=embed)
	          
      else:
	      
	      embed = discord.Embed(title="Command: Py!about", description="`Py!about user` or `Py!about user <@user>`\n`Py!about server`\n`Py!about bot`", color = discord.Colour.blue())
	      
	      await ctx.send(embed=embed)
		
def setup(bot):
    bot.add_cog(Command(bot))
