from riscord import client
import discord
from discord.ext import commands
import os, random	

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

@client.event
async def on_message(message):
	bad_words = ["fuck", "cunt", "bitch", "dick", "shit"]
	replies = ["You kiss your mother with that mouth?", ":angwy:", ":eyes:", "Isaac someone is swearing again", "Dickhead", "Shithead", "Watch your flipping language"]

	if message.author == client.user:
		return
	else:
		for i in bad_words:
			if i in message.content:
				await message.channel.send(replies[random.randint(0,3)])
		await client.process_commands(message)


for filename in os.listdir('./riscord/cogs'):
	if filename.endswith(".py"):
		client.load_extension(f'riscord.cogs.{filename[:-3]}')