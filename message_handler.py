async def log_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    print(f'Message {user_message} by {username} on {channel}')