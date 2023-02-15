async def unban(interaction, member, reason):
    if not member.guild_permissions.ban_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    await interaction.guild.unban(member)  
    await interaction.response.send_message(f"{member.mention} has been un-banned\n\n**Reason ->** {reason}")