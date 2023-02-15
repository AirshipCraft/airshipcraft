async def ban(interaction, member, reason):
    if not member.guild_permissions.ban_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    await interaction.guild.ban(member, reason=reason)  
    await interaction.response.send_message(f"{member.mention} has been banned\n\nReason -> {reason}")