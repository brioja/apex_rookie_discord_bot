import discord
from discord.ext import commands
import json

# Load the config file
with open('config.json') as config_file:
    config = json.load(config_file)

# Create a bot instance with intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    # Sync the command tree to make slash commands available
    await bot.tree.sync()

@bot.tree.command(name='handicap', description='Responds with the provided handicap number')
async def handicap(interaction: discord.Interaction, number: int):
    # Respond to the slash command
    await interaction.response.send_message(f'Handicap number received: {number}')

# Run the bot using the token from the config file
bot.run(config['bot_token'])
