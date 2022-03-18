import discord
from discord.ext import commands
from music import music
import os

bot = commands.Bot(command_prefix='?', intents = discord.Intents.all())

bot.add_cog(music(bot))

bot.run(os.getenv("TOKEN"))
