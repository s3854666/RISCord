import discord
from discord.ext import commands

class General(commands.Cog):
	def __init__(self, client):
		self.client = client

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		print('Bot is up')
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("```Please enter all the required arguments.\nCheck the ;help command for more information on the commands.```")
	
	@commands.Cog.listener()
	async def on_message(message):
		bad_words = ["fuck", "cunt", "bitch"]
		replies = ["You kiss your mother with that mouth?", "Dickhead", "Shithead", "Watch your fucking language"]
		if client.user.id != message.author.id:
			for i in bad_words:
				if i in message.content.lower():
					await message.channel.send(replies[random.randint(0,3)])
	
	# General commands
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong!')
	
	@commands.command()
	async def author(ctx):
		await ctx.send("good boy")


def setup(client):
	client.add_cog(General(client))