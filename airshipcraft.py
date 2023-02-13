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

client.run(os.getenv('TOKEN'))