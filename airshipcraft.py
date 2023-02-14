import client as cl
import commands as co
from discord import app_commands
from dotenv import load_dotenv
import event_handler as eh
import os

load_dotenv()
env = os.environ
client = cl.create_client()
tree = app_commands.CommandTree(client)
co.register_commands(env, client, tree)

@client.event
async def on_ready():
    await eh.on_ready(env, client, tree)

@client.event
async def on_message(message):
    await eh.log_message(message, client)

client.run(env['TOKEN'])