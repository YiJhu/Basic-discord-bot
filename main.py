#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord_slash import SlashCommand
import os

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all(),
                   allowed_mentions=discord.AllowedMentions(everyone=False))
slash = SlashCommand(bot, sync_commands=True, override_type=True)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="DN-Team"))
    print('Discord Test is Online!')
    print('BOT NAME : %s' % bot.user.name)
    print('USER ID : %s' % bot.user.id)
    print('------' * 5)


if __name__ == "__main__":
    bot.run('')
