import client as cl
import commands as co
import discord
from discord import app_commands
from dotenv import load_dotenv
import message_handler as mh
import os

load_dotenv()
env = os.environ
client = cl.create_client()
tree = app_commands.CommandTree(client)
co.register_commands(env, client, tree)

@client.event
async def on_ready():
    await client.wait_until_ready()
    await tree.sync(guild = discord.Object(id=os.getenv('GUILD_ID')))
    print(f'{client.user} is now ready for action!')

@client.event
async def on_message(message):
    await mh.log_message(message)

client.run(env['TOKEN'])