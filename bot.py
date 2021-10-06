# bot.py
import discord
import os

import requests
from discord.ext import commands

import hypixel


bot = commands.Bot(command_prefix="=")


@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)



@bot.command()
async def playcount(ctx, mw):
        mwcount = hypixel.mwplayercount()
        await ctx.send(f"{playcount}: {mw}")



bot.run(os.environ['DISCORD_TOKEN'])