from command import c_airshipcraft , c_latency , c_ban , c_unban , c_kick , c_mute , c_unmute , c_ticket
import discord

def register_commands(env, client, tree):
    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='airshipcraft', description='Get Information about AirshipCraft')
    async def airshipcraft(interaction: discord.Interaction):
        await c_airshipcraft.airshipcraft(interaction)

    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='latency', description='Check the Bots Latency to Discord')
    async def latency(interaction: discord.Interaction):
        await c_latency.latency(interaction, client)

    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='ban', description='Ban a User')
    async def ban(interaction: discord.Interaction, member: discord.Member, reason: str):
        await c_ban.ban(interaction, member, reason)

    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='unban', description='Unban a User')
    async def unban(interaction: discord.Interaction, member: str, reason: str):
        await c_unban.unban(interaction, member, reason)

    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='kick', description='Kick a User')
    async def kick(interaction: discord.Interaction, member: discord.Member, reason: str):
        await c_kick.kick(interaction, member, reason)
    
    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='mute', description='Mute a User')
    async def mute(interaction: discord.Interaction, member: discord.Member, reason: str):
        await c_mute.mute(interaction, member, reason)
    
    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='unmute', description='Unmute a User')
    async def unmute(interaction: discord.Interaction, member: discord.Member, reason: str):
        await c_unmute.unmute(interaction, member, reason)

    @tree.command(guild=discord.Object(id=env['GUILD_ID']), name='ticket', description='Create a Ticket')
    async def ticket(interaction: discord.Interaction, name: str):
        await c_ticket.ticket(interaction, name, client)