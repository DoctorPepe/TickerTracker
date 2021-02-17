import discord
from discord.ext import commands

class DiscordBot(object):
    def run(self):
        client = commands.Bot(command_prefix='$')

        @client.event
        async def on_ready():
            print("The bot is ready...")
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with stonks"))

        client.run('token')
