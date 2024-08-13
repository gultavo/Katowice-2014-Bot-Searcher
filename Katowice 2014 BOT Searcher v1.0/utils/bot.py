import discord
from discord.ext import commands
import asyncio
discord_token = 'MTI0NjQ1NjU2NjgyNDMwODg1OA.GDlA2t.xH5J28PWYmyh17j9cYw_90lPV0jMebiSWcyO2w'
intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=intents)
from os import listdir
async def load_cogs():
    for arquivo in listdir('cogs'):
        if arquivo.endswith('.py'):
            await client.load_extension(f'cogs.{arquivo[:-3]}')

async def main():
    await load_cogs()
    await client.start(discord_token)

@client.event
async def on_ready():
    print(f'{client.user.name} is ready')

asyncio.run(main())