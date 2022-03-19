import discord
from discord.ext import commands
from music import music
import asyncio
import os

activity = discord.Game(name="with humans")

bot = commands.Bot(command_prefix='?', activity=activity, intents = discord.Intents.all())

bot.add_cog(music(bot))

bot.run(os.getenv("TOKEN"))
