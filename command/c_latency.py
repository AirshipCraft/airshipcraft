import discord

async def latency(interaction, client):
    e = discord.Embed()
    e.title = 'Bot to Discord Latency'
    e.description = f'Latency between the Bot and Discord'
    e.add_field(name='Current Latency', value=f'{round(client.latency * 1000)}ms')
    e.color = discord.Color.green()
    await interaction.response.send_message(embed=e)