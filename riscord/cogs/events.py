import discord
from discord.ext import commands
import datetime
from riscord.misc import *
import icalendar
# # ICS link: https://calendar.google.com/calendar/ical/rmitinfosecollective@gmail.com/public/basic.ics
cal = open("riscord/basic.ics", "r")
gcal = icalendar.Calendar.from_ical(cal.read())

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['events'])
    async def show_event(self, ctx):
        embed = discord.Embed(color=discord.Colour.blue(), title='Events',
                              description='All the events in the calendar')
        embed.set_author(name="RISC")
        counter = 1
        for component in gcal.walk():
            if component.name == "VEVENT":
                embed.add_field(name="Event " + str(counter), value=component.get('summary'),inline=False)
                counter+=1
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Events(client))