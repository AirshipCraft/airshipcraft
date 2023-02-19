import discord
async def ban(interaction, member, reason):
    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    await interaction.guild.ban(member, reason=reason)  

    e = discord.Embed()
    e.title = 'BAN HAMMER'
    e.add_field(name='Player Banned', value=f'{member.mention}')
    e.add_field(name='Reason', value=f'{reason}')
    e.color = discord.Color.red()
    await interaction.response.send_message(embed=e)