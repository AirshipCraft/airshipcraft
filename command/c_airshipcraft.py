import discord

async def airshipcraft(interaction):
    e = discord.Embed()
    e.title = 'AirshipCraft Information'
    e.description = f'This is still under development'
    e.color = discord.Color.red()

    e.add_field(name='Total Users', value=f'{interaction.guild.member_count}')

    await interaction.response.send_message(embed=e)