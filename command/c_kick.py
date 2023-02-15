async def kick(interaction, member, reason):
    if not member.guild_permissions.kick_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    await member.kick()
    await interaction.response.send_message(f"{member.mention} has been kicked\n\n**Reason ->** {reason}")