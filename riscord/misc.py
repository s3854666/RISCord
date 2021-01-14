import json
authorized_users = json.loads(open("riscord/authorized_users.json", "r").read())
authorized_users = [v.strip() for k,v in authorized_users.items()]

def check_auth(ctx):
	if str(ctx.message.author.id) in authorized_users:
		return True
	else:
		return False
