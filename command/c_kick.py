import discord

async def kick(interaction, member, reason):
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    await member.kick()

    e = discord.Embed()
    e.title = 'UH-OH'
    e.add_field(name='Player Kicked', value=f'{member.mention}')
    e.add_field(name='Reason', value=f'{reason}')
    e.color = discord.Color.red()
    await interaction.response.send_message(embed=e)