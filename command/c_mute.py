import discord

async def mute(interaction, member, reason):
    if not interaction.user.guild_permissions.mute_members:
        await interaction.response.send_message("You do not have permission to use this command")
        return

    muted_role = discord.utils.get(interaction.guild.roles, name="Muted")
    
    if not muted_role:
        muted_role = await interaction.guild.create_role(name="Muted")
        
        for channel in interaction.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False)
    
    await member.add_roles(muted_role)

    e = discord.Embed()
    e.title = 'UH-OH'
    e.add_field(name='Player Muted', value=f'{member.mention}')
    e.add_field(name='Reason', value=f'{reason}')
    e.color = discord.Color.red()
    await interaction.response.send_message(embed=e)