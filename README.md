## Todoroki Shouto
[![Discord Bots](https://top.gg/api/widget/714330708365148190.svg)](https://top.gg/bot/714330708365148190)

## Invite
> [Invite Me Here](https://discord.com/api/oauth2/authorize?client_id=714330708365148190&permissions=8&scope=bot)

## First require for building bot in discord.py
``` python
import discord
import os
from discord.ext import commands

todo = commands.Bot(command_prefix="todo.")
```

## Second require for building bot in discord.py
``` python
# we need event, for reporting if bot is ready

@todo.event()
async def on_ready():
  print(f"Loginned as {bot.user.name} - {bot.user.id}")
  print(f"Server : {len(bot.guilds)}")

@todo.command()
async def ping(ctx):
  await ctx.send("Pong!")
```

## Third require for building bot in discord.py

``` python
SECRET = os.environ.get("TOKEN")
todo.login(SECRET)
```

## Token
***Dont forget to put you token on `.env` file***

> .env
``` env
TOKEN=YOU_BOT_TOKEN
```
 ## Visit Me On [top.gg](https://top.gg) !
> [Click and Click Here](https://top.gg/bot/714330708365148190)
