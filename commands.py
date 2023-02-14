import command_airshipcraft as ca
import command_latency as cl
import command_ticket as ct
import discord

def register_commands(env, client, tree):
    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='airshipcraft', description='Get Information about AirshipCraft')
    async def airshipcraft(interaction: discord.Interaction):
        await ca.airshipcraft(interaction)

    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='latency', description='Check the Bots Latency to Discord')
    async def latency(interaction: discord.Interaction):
        await cl.latency(interaction, client)

    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='ticket', description='Create a Ticket')
    async def ticket(interaction: discord.Interaction, name: str):
        await ct.ticket(interaction, name, client)