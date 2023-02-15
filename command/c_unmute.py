import discord

async def unmute(interaction, member, reason):
    if not member.guild_permissions.mute_members:
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
    await interaction.response.send_message(f"{member.mention} has been un-muted\n\n**Reason ->** {reason}")