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
	
	# General commands
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong!')
	
	@commands.command()
	async def author(self, ctx):
		await ctx.send("good boy")


def setup(client):
	client.add_cog(General(client))