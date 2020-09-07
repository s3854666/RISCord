from riscord import client, verify_student
from discord.ext import commands

@client.event
async def on_ready():
	print("Bot is ready.")

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def verify(ctx, *, student_id):
	
	verified = await verify_student.verify_user(student_id)
	if verified:
		# member = ctx.message.author
		# role = get(member.server.roles, name="Bots")
		# await bot.add_roles(member, role)
		await ctx.send('Membership confirmed')
	else:
		await ctx.send("The student is not a member")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("```Please enter all the required arguments.\nCheck the ;help command for more information on the commands.```")