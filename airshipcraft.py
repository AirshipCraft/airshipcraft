import discord
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()

class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents = intents)

        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=os.getenv('GUILD_ID')))
            self.synced = True
        print(f'{self.user} successfully logged in')

client = aclient()
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    print(f'Message {user_message} by {username} on {channel}')

@tree.command(guild = discord.Object(id=os.getenv('GUILD_ID')), name = 'latency', description='Check the Bot Latency to Discord')
async def latency(interaction: discord.Interaction):
    await interaction.response.send_message(f'Server Ping: {round(client.latency * 1000)}ms')

client.run(os.getenv('TOKEN'))