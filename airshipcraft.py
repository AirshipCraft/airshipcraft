import command_latency
import command_ticket
import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import message_handler

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
    await message_handler.log_message(message)

@tree.command(guild = discord.Object(id=os.getenv('GUILD_ID')), name = 'latency', description='Check the Bots Latency to Discord')
async def latency(interaction: discord.Interaction):
    await command_latency.latency(interaction, client)

@tree.command(guild = discord.Object(id=os.getenv('GUILD_ID')), name = 'ticket', description='Create a Ticket')
async def ticket(interaction: discord.Interaction, name: str):
    await command_ticket.ticket(interaction, name, client)

client.run(os.getenv('TOKEN'))