import discord

async def unmute(interaction, member, reason):
    if not interaction.user.guild_permissions.mute_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    muted_role = discord.utils.get(interaction.guild.roles, name="Muted")
    
    if not muted_role:
        await interaction.response.send_message("The are no members with the Muted role")
        return

    if muted_role not in member.roles:
        await interaction.response.send_message(f"{member.mention} is not muted")
        return
    
    await member.remove_roles(muted_role)

    e = discord.Embed()
    e.title = 'YEAH'
    e.add_field(name='Player Unmuted', value=f'{member.mention}')
    e.add_field(name='Reason', value=f'{reason}')
    e.color = discord.Color.green()
    await interaction.response.send_message(embed=e)