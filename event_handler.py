import discord

async def on_ready(env, client, tree):
    await client.wait_until_ready()
    await tree.sync(guild = discord.Object(id=env['GUILD_ID']))
    print(f'{client.user} is now ready for action!')

async def log_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    print(f'Message {user_message} by {username} on {channel}')