import discord

async def airshipcraft(interaction):
    e = discord.Embed()
    e.title = 'AirshipCraft Information'
    e.description = f'This is still under development'
    e.color = discord.Color.red()
    await interaction.response.send_message(embed=e)