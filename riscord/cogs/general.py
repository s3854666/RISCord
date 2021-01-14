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
	@commands.command(aliases=['h'])
	async def help(self, ctx):
		embed = discord.Embed(color=discord.Colour.blue(), title='Help command', description='Shows the commands that you can run')
		embed.set_author(name="RISC")
		embed.add_field(name=';help or ;h', value='Shows this message', inline=False)
		embed.add_field(name=';verify or ;v', value='Verifies your membership', inline=False)
		embed.add_field(name='More features coming soon', value=" :)", inline=False)
		embed.set_footer(text="Source code https://github.com/n00bmasterr/RISCord")

		await ctx.send(embed=embed)

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong!')
	
	@commands.command()
	async def author(self, ctx):
		await ctx.send("good boy")



def setup(client):
	client.add_cog(General(client))