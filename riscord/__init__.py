import discord
from discord.ext import commands

client = commands.Bot(command_prefix=';')
client.remove_command('help')