import discord
from discord.ext import commands
from music import music
import asyncio
import os

bot = commands.Bot(command_prefix='?', intents = discord.Intents.all())

@client.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="with humans"))
  
  print("Ready")

bot.add_cog(music(bot))

bot.run(os.getenv("TOKEN"))
