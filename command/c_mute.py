import discord

async def mute(interaction, member, reason):
    if not member.guild_permissions.mute_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    muted_role = discord.utils.get(interaction.guild.roles, name="Muted")
    
    if not muted_role:
        muted_role = await interaction.guild.create_role(name="Muted")
        
        for channel in interaction.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False)
    
    await member.add_roles(muted_role)
    await interaction.response.send_message(f"{member.mention} has been muted\n\n**Reason ->** {reason}")