import discord
import re

async def unban(interaction, member, reason):

    try:
        match = re.match(r'^[A-Za-z]+#[0-9]{4}$', member)
        if not match:
            raise ValueError('Member string must be formatted as "name#1234"')

        member_name, member_discriminator = member.split('#')
        banned_users = interaction.guild.bans()
        
        for banned_entry in banned_users:
            user = banned_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await interaction.guild.unban(user, reason=reason)
                e = discord.Embed()
                e.title = 'SUCCESS'
                e.add_field(name='Player Unbanned', value=member)
                e.add_field(name='Reason', value=reason)
                e.color = discord.Color.green()
                await interaction.response.send_message(embed=e)
                break
        else:
            raise ValueError(f"{member} not found in the server's ban list.")

    except ValueError as e:
        error_embed = discord.Embed(
            title='ERROR',
            description=str(e),
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=error_embed)