import discord
from dotenv import load_dotenv
import os

load_dotenv()

class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents = intents)

    async def on_ready(self):
        print(f'{self.user} successfully logged in')

client = aclient()

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    print(f'Message {user_message} by {username} on {channel}')

client.run(os.getenv('TOKEN'))