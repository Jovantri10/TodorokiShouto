import discord
from discord.ext import commands
import os
import pyfiglet
import canvas as Painter
import heapq
import random
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
from deku import *
import deku as todo
import bs4
from discord import Embed
import platform

cc = commands.command()
sm = commands.cooldown(1, 14, commands.BucketType.user)
cyan = 0, 255, 255
yell = 255, 255, 0 
ung = 191, 0, 255 
vi = 143, 0, 255
q = os.environ.get("BRAINLY")
k = os.environ.get("BRAINLYKEY")
say = os.environ.get("SS")
go = os.environ.get("go")
key = os.environ.get("keygo")
numkey = os.environ.get("numbertoken")

class Api(commands.Cog):
    
    def __init__(self, bot):

        self.bot = bot 
    
    @cc   
    @sm     
    async def brainly(self, ctx, *args):
      try:
        o = todo.urlify(' '.join(args))
        t = requests.get(q+str(o)+k).json()[0]["title"]
        u = requests.get(q+str(o)+k).json()[0]["url"]
        embed = discord.Embed(color=discord.Colour.from_rgb(0, 255, 255), description=f"**[{t}]({u})**\nSource : [Here](https://brainly.co.id)\nLink Tugas : [Here]({u})")
        embed.set_author(name=t, icon_url="https://cdn.discordapp.com/attachments/730367960572493828/737997714444255282/Screen_20200729_183739_e001.jpg")
        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(f"```{e}```")
      

    @cc 
    @sm  
    async def google(self, ctx, *args):
      if len(args)==0:
        y = await ctx.send("Searching.......")
        await y.edit(content="Couldn't find what what :V")
      try:
        y = todo.urlify(' '.join(args))
        q = requests.get(go+str(y)+key).json()["query"]["q"]
        ur = requests.get(go+str(y)+key).json()["query"]["url"]
        des = requests.get(go+str(y)+key).json()["knowledge_graph"][0]["description"]
        embed = discord.Embed(color = discord.Colour.from_rgb(255, 255, 0), description=f"**[{q}]({ur})**\n*{des}*")
        embed.set_author(name=q, icon_url='https://cdn.discordapp.com/attachments/730367960572493828/737808399831662694/socialmediaicon_29.png')
        embed.set_footer(text="© Google.com")
        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(f"```ERORR BANGG ~> {e}```")
        
    @commands.command(aliases=["screenshoot"])
    @commands.is_nsfw()
    @sm 
    async def ss(self, ctx, *args):
      try:
        o = todo.urlify(' '.join(args))
        y = say+str(o)
        await ctx.send(file=discord.File(Painter.urltoimage(y), 'screenshoot.png'))
      except Exception as e:
        await ctx.send(f"```{e}```")
      
    @commands.command(pass_context=True)
    @commands.is_owner()
    async def rp(self, ctx, *args):
        if ctx.message.author.id==Config.owner.id:
            try:
                user_to_send = self.bot.get_user(int(args[0]))
                em = discord.Embed(title="Hi, "+user_to_send.name+"! the bot owner sent a response for your suggest and bug!", description=' '.join(list(args)[1:len(list(args))]), colour=discord.Colour.from_rgb(101, 150, 142))
                await user_to_send.send(embed=em)
                await ctx.message.add_reaction('<a:ncgaes:713235013809864774>')
            except Exception as e:
                await ctx.send(f' | Error: `{e}`')
        else:
            await ctx.send('You are not the bot owner. Go get a life.')
    
    @cc
    @sm  
    async def notstonk(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Input text tolol")
      try:
        join = todo.urlify(' '.join(args))
        y = 'https://nezumiyuiz.glitch.me/api/notstonks?avatar='+str(ctx.author.avatar_url).replace('.webp', '.png')+'&text='+str(join)
        await ctx.send(file=discord.File(Painter.urltoimage(y), 'bangpeguigans.png'))
      except Exception as e:
        await ctx.send(f"```{e}```")
        
    @cc 
    @sm 
    async def cofee(self, ctx):
      t = requests.get('https://coffee.alexflipnote.dev/random.json').json()["file"]
      await ctx.send(file=discord.File(Painter.urltoimage(t), 'ea.png'))
      
    @cc
    @sm  
    async def quoteimg(self, ctx):
      url = 'https://quoteimg.glitch.me/generate?height=1080&width=1080&invert=true'
      await ctx.send(file=discord.File(Painter.urltoimage(url), 'ea.png'))
    @cc 
    @sm 
    async def nature(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,water"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'nature.png'))
    @cc 
    @sm 
    async def mountain(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,mountain"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'mountain.png'))
    @cc 
    @sm 
    async def home(self, ctx):
      n = "https://source.unsplash.com/1600x900/?house,cloud"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'house.png'))
      
    @cc
    @sm  
    async def randomimg(self, ctx):
      br = 'https://loremflickr.com/320/240'
      await ctx.send(file=discord.File(Painter.urltoimage(br), 'random.png'))
     
    @cc 
    @sm  
    async def randomuser(self, ctx, *args):
      gds = todo.urlify(' '.join(args))
      y = requests.get(f'https://anapioficeandfire.com/api/characters/'+str(gds)).json()["name"]
      a = requests.get(f'https://anapioficeandfire.com/api/characters/'+str(gds)).json()["gender"]
      b = requests.get(f'https://anapioficeandfire.com/api/characters/'+str(gds)).json()["culture"]
      c = requests.get(f'https://anapioficeandfire.com/api/characters/'+str(gds)).json()["titles"]
      d = requests.get(f'https://anapioficeandfire.com/api/characters/'+str(gds)).json()["born"]
      await ctx.send(f"Name : `{y}`")
      await ctx.send(f"Gender : `{a}`")
      await ctx.send(f"Culture : `{b}`")
      await ctx.send(f"Title : `{c}`")
      await ctx.send(f"Born : `{d}`")
      
      
    @cc 
    @sm  
    async def book(self, ctx, *args):
      tr = todo.urlify(' '.join(args))
      op = requests.get('https://anapioficeandfire.com/api/books/'+str(tr)).json()["name"]
      au = requests.get('https://anapioficeandfire.com/api/books/'+str(tr)).json()["authors"]
      isb = requests.get('https://anapioficeandfire.com/api/books/'+str(tr)).json()["isbn"]
      nop = requests.get('https://anapioficeandfire.com/api/books/'+str(tr)).json()["numberOfPages"]
      pu = requests.get('https://anapioficeandfire.com/api/books/'+str(tr)).json()["publisher"]
      co = requests.get('https://anapioficeandfire.com/api/books/'+str(tr)).json()["country"]
      await ctx.send(f"Book : `{op}`")
      await ctx.send(f"Author : `{au}`")
      await ctx.send(f"Isbn : `{isb}`")
      await ctx.send(f"Pages : `{nop}`")
      await ctx.send(f"Publisher : `{pu}`")
      await ctx.send(f"Country : `{co}`")
      
      
    @cc 
    @sm 
    async def fish(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,fish"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'fish.png'))
    @cc 
    @sm 
    async def animal(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,animal"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'animal.png'))
    @cc 
    @sm 
    async def river(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,river"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'river.png'))
      
    @cc
    @sm 
    async def kanyequote(self, ctx):
      k = requests.get('https://api.kanye.rest/').json()["quote"]
      await ctx.send(f"```{k}```-Kanye West")

    @cc 
    @sm 
    async def movie(self, ctx, *args):
      tol = todo.urlify(' '.join(args))
      name = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["name"]
      url = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["url"]
      lang = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["language"]
      type = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["type"]
      sta = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["status"]
      embed = discord.Embed(color = discord.Color.green())
      embed.add_field(name="Name", value=f"**```{name}```**")
      embed.add_field(name="URL", value=f"**[{name}]({url})**")
      embed.add_field(name="Language", value=f"**```{lang}```**")
      embed.add_field(name="Tag", value=f"**```{type}```**")
      embed.add_field(name="Status", value=f"**```{sta}```**")
      
      await ctx.send(embed=embed)
    
    @cc 
    @sm   
    async def pixabay(self, ctx, *args):
      pol = todo.urlify(' '.join(args))
      idi = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["id"]
      totk = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["total"]
      toth = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["totalHits"]
      pur = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["pageURL"]
      ty = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["type"]
      ta = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["tags"]
      vi = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["views"]
      do = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["downloads"]
      fa = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["favorites"]
      li = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["likes"]
      com = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["comments"]
      uid = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["user_id"]
      us = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["user"]
      im = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][random.randint(0, 5)]["largeImageURL"]
      embed = discord.Embed(color = discord.Color.blue(), description=f"***PIXABAY SEARCHING***\n\nTotal Image : `{totk}`\nTotal Hits : `{toth}`\nID : `{idi}`\nPage : [CLICK HERE]({pur})\nType : `{ty}`\nTags : `{ta}`\nViews : `{vi}`\nDownloads : `{do}`\nFavorites : `{fa}`\nLikes : `{li}`\nComments : `{com}`\nUser ID : `{uid}`\nUser : `{us}`")
      embed.set_image(url=im)
      await ctx.send(embed=embed)
    
    @cc 
    @sm  
    async def anime(self, ctx, *args):
      await ctx.send("```Anime commands on fixed!! Just waitting```")
      
    @cc 
    @sm   
    async def country(self, ctx, *args):
      if len(args)==0:
        await ctx.send("***`Todo.country [country]`***")
      else:
        y = todo.urlify(' '.join(args))
        n = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["name"]
        adc = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["alpha2Code"]
        c = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["capital"]
        r = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["region"]
        sr = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["subregion"]
        p = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["population"]
        t = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["timezones"]
        embed = discord.Embed(title=n, color=discord.Color.blue(), description=f"Name : **{n}**\nAliases : **{adc}**\nCapital : **{c}**\nRegion : **{r}**\nSubregion : **{sr}**\nPopulation : **{p}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730294436701012029/735080496656285746/unnamed.gif")
        await ctx.send(embed=embed)
      #except Exception:
        #await ctx.send("Cant find that on country list")
    @cc 
    @sm   
    async def news(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Give the topic news, like this \n***`Todo.news [news]`***")
      else:
        tj = todo.urlify(' '.join(args))
        st = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["status"]
        tr = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["totalResults"]
        d = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["description"]
        t = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["title"]
        a = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["author"]
        ur = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["url"]
        ut = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["urlToImage"]
        pa = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["publishedAt"]
        co = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["content"]
        embed = discord.Embed(title="NEWS!", color=discord.Color.blue(), description=f"Status : `{st}`\nResults : `{tr}`\n\nTitle : **`{t}`**\nAuthor : **`{a}`**\nURL : **[{t}]({ur})**\nPublished At : **`{pa}`**\nContent : ***`{co}`***")
        #Description : ***`{d}`***")
        embed.set_thumbnail(url=ut)
        await ctx.send(embed=embed)
      
    @cc 
    @sm   
    async def aes(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Please input the text!")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        y = todo.urlify(' '.join(args))
        u = requests.get('https://nezumiyuiz.glitch.me/api/aesthetic?text='+str(y)).json()["aesthetic"]
        await ctx.send(u)
    @cc 
    @sm   
    async def aessc(self, ctx, *args):
      y = todo.urlify(' '.join(args))
      u = requests.get('https://nezumiyuiz.glitch.me/api/aesthetic?text='+ctx.channel).json()["aesthetic"]
      await ctx.send(u)
    @cc 
    @sm 
    async def reverse(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Please input text for reversed")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        u = todo.urlify(' '.join(args))
        o = requests.get('https://nezumiyuiz.glitch.me/api/reverse?text='+str(u)).json()["reverse"]
        await ctx.send(o)
    @cc
    @sm 
    async def fancy(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Input text!")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        y = todo.urlify(' '.join(args))
        o = requests.get('https://nezumiyuiz.glitch.me/api/fancy?text='+str(y)).json()["fancy"]
        await ctx.send(o)
    @cc
    @sm 
    async def fliptext(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Input text!")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        y = todo.urlify(' '.join(args))
        o = requests.get('https://nezumiyuiz.glitch.me/api/fliptext?text='+str(y)).json()["fliptext"]
        await ctx.send(o)
        
    @cc 
    @sm
    async def zerotwo(self, ctx, *args):
      t = requests.get('https://nezumiyuiz.glitch.me/api/zerotwo').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(t), 'zerotwo.png'))
    
    @cc 
    @sm   
    async def findip(self, ctx, *args):
      if (args)==0:
        await ctx.send("Pleade input ip after ***`Todo.ip [ip]`***")
      try:
        urli = todo.urlify(' '.join(args))
        i = requests.get('https://ipapi.co/'+str(urli)+'/json/').json()["ip"]
        c = requests.get('https://ipapi.co/'+str(urli)+'/json/').json()["city"]
        r = requests.get('https://ipapi.co/'+str(urli)+'/json/').json()["region_code"]
        embed = discord.Embed(title=i, color=discord.Color.blue(), description=f"City : **`{c}`**\nAliases City : **`{r}`**\n")
        await ctx.send(embed=embed)
      except Exception:
        await ctx.send("Cant find the ip, sorry:v")
    
    @cc 
    @sm 
    async def sof(self, ctx, *args):
      if len(list(args))==0:
        await ctx.send("Input the questions")
      try:
        t = todo.urlify(' '.join(args))
        ti = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["title"]
        li = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["link"]
        ia = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["is_answered"]
        ac = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["answer_count"]
        vw = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["view_count"]
        qi = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["question_id"]
        pi = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["profile_image"]
        dn = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["display_name"]
        ui = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["user_id"]
        ut = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["user_type"]
        embed = discord.Embed(color=discord.Color.blue(), description=f"**[{ti}]({li})**\nAnswered : **{ia}**\nAnswer Count : **{ac}**\nView Count : **{vw}**\nQuestion ID : **{qi}**\n\nBy : **{dn}**\nID : **{ui}**\nType : **{ut}**\n")
        embed.set_thumbnail(url=pi)
        embed.set_footer(text="© Stackoverflow.com")
        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(f"Error | `{e}`")
    
    @cc 
    @sm   
    async def hero(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Input the hero name pls")
      try:
        y = todo.urlify(' '.join(args))
        n = requests.get('https://superheroapi.com/api/318053349328478/search/'+str(y)).json()["results"][0]["name"]
        inn = requests.get('https://superheroapi.com/api/318053349328478/search/'+str(y)).json()["results"][0]["powerstats"]["intelligence"]
        st = requests.get('https://superheroapi.com/api/318053349328478/search/'+str(y)).json()["results"][0]["powerstats"]["strength"]
        sp = requests.get('https://superheroapi.com/api/318053349328478/search/'+str(y)).json()["results"][0]["powerstats"]["speed"]
        du = requests.get('https://superheroapi.com/api/318053349328478/search/'+str(y)).json()["results"][0]["powerstats"]["durability"]
        po = requests.get('https://superheroapi.com/api/318053349328478/search/'+str(y)).json()["results"][0]["powerstats"]["power"]
        embed = discord.Embed(title=n, color=discord.Colour.from_rgb(0, 255, 255), description=f"**<a:boosterinbgsd:712992968990130189> POWERSTATS**\nInteligence : **`{inn}`**\nStrength : **`{st}`**\nSpeed : **`{sp}`**\nDurability : **`{du}`**\nPower : **`{po}`**")
        await ctx.send(embed=embed)
      except Exception:
        await ctx.send(f"Oof i cant find the hero from my list, i think that a hero, but there is no on my list, thank you")
        
        
def setup(bot):
  bot.add_cog(Api(bot))
