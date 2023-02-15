from client import create_client
from commands import register_commands
from discord import app_commands
from dotenv import load_dotenv
import event_handler as eh
import os

load_dotenv()
env = os.environ
client = create_client()
tree = app_commands.CommandTree(client)
register_commands(env, client, tree)

@client.event
async def on_ready():
    await eh.on_ready(env, client, tree)

@client.event
async def on_message(message):
    await eh.log_message(message, client)

client.run(env['TOKEN'])