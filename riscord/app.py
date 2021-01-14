from riscord import client
from riscord.misc import *
import discord
from discord.ext import commands
import os, random, json

bad_words = open("riscord/badwords.txt", "r").readlines()

@client.command()
async def load(ctx, extension):
	if check_auth(ctx):
		await ctx.send("Your wish is my command")
		client.load_extension(f'riscord.cogs.{extension}')
		await ctx.send(f"Loaded {extension}")
	else:
		await ctx.send("You don't have permission to run this")

@client.command()
async def unload(ctx, extension):
	if check_auth(ctx):
		await ctx.send("Your wish is my command")
		client.unload_extension(f'riscord.cogs.{extension}')
		await ctx.send(f"Unloaded {extension}")
	else:
		await ctx.send(f"You don't have permission to run this")

@client.command()
async def reload(ctx, extension):
	if check_auth(ctx):
		await ctx.send("Your wish is my command")
		client.unload_extension(f'riscord.cogs.{extension}')
		client.load_extension(f'riscord.cogs.{extension}')
		await ctx.send(f"Reloaded {extension}")
	else:
		await ctx.send(f"You don't have permission to run this")
@client.event
async def on_message(message):
	reactions = ['💩',  '👀', '👹', '🤬']
	if message.author == client.user:
		return
	else:
		for i in bad_words:
			if i.strip() in message.content.split(" "):
				await message.add_reaction(reactions[random.randint(0,len(reactions) - 1)])
				break
		if '​' in message.content:
			await message.channel.send("​")
		await client.process_commands(message)

	# Delete the message right away if it contains a student number.
	if message.content.startswith(";verify") or message.content.startswith(";v"):
		await message.channel.purge(limit=2)


for filename in os.listdir('./riscord/cogs'):
	if filename.endswith(".py"):
		client.load_extension(f'riscord.cogs.{filename[:-3]}')