import discord

async def unban(interaction, member, reason):
    if not member.guild_permissions.ban_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    await interaction.guild.unban(member)  

    e = discord.Embed()
    e.title = 'YEAH'
    e.add_field(name='Player Unbanned', value=f'{member.mention}')
    e.add_field(name='Reason', value=f'{reason}')
    e.color = discord.Color.green()
    await interaction.response.send_message(embed=e)