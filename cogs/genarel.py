# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from core.core import Core
import time, datetime

class Genarel(Core):
    #@cog_ext.cog_slash(name="test")
    #async def _test(self, ctx: SlashContext):
        #embed = discord.Embed(title="embed test")
        #await ctx.send(content="test", embeds=[embed])

    @cog_ext.cog_slash(name="time")
    async def _time(self, ctx: SlashContext):
        """Show now time (UTC+8)"""
        now = time.strftime('%Y-%m-%d %I:%M:%S %p')
        embed = discord.Embed(title="Now time", description="%s" %(now), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="DN-Test")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name="ping")
    async def _ping(self, ctx: SlashContext):
        """Ping latency"""
        embed = discord.Embed(title="ping latency", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Api latency", value="%s ms" %(f'{round(self.bot.latency*1000)}'), inline=False)
        embed.set_footer(text="DN-Test")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name="server_info")
    async def _server_info(self, ctx):
        """Display status of the server"""
        server_name = ctx.guild.name
        server_create_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        server_owner = ctx.guild.owner
        server_user = len(ctx.guild.members)
        text_channel = len(ctx.guild.text_channels)
        voice_channel = len(ctx.guild.voice_channels)
        embed = discord.Embed(title="Server info", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Server Name", value="%s" %(server_name), inline=False)
        embed.add_field(name="Create Time", value="%s" %(server_create_date), inline=False)
        embed.add_field(name="Server Owner", value="%s" %(server_owner), inline=False)
        embed.add_field(name="Total of people", value="%s" %(server_user), inline=False)
        embed.add_field(name="Total of text channel", value="%s" %(text_channel), inline=False)
        embed.add_field(name="Total of voice channel", value="%s" %(voice_channel), inline=False)
        embed.set_footer(text="DN-Test")
        await ctx.send(embeds = [embed])
    


def setup(bot):
    bot.add_cog(Genarel(bot))