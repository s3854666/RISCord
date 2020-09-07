from riscord import client
import discord
from discord.ext import commands
import os, random	

# @has_permissions()
@client.command()
async def load(ctx, extension):
	client.load_extension(f'riscord.cogs.{extension}')
	await ctx.send(f"Loaded {extension}")

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'riscord.cogs.{extension}')
	await ctx.send(f"Unloaded {extension}")

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'riscord.cogs.{extension}')
	client.load_extension(f'riscord.cogs.{extension}')
	await ctx.send(f"Reloaded {extension}")


for filename in os.listdir('./cogs'):
	if filename.endswith(".py"):
		client.load_extension(f'riscord.cogs.{filename[:-3]}')