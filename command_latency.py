async def latency(client, interaction):
    await interaction.response.send_message(f'Server Ping: {round(client.latency * 1000)}ms')