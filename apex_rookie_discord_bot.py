import discord
from discord.ext import commands
import json
import random

# Load the handicaps from the JSON file
with open('handicaps.json') as handicaps_file:
    handicaps = json.load(handicaps_file)

# Create a bot instance with intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.tree.sync()

def find_close_handicaps(input_value, handicap_list, threshold=0.5):
    # Find handicaps close to the input value within a threshold
    close_handicaps = [handicap for handicap in handicap_list if abs(handicap['value'] - input_value) <= threshold]
    return close_handicaps

@bot.tree.command(name='handicap', description='Selects handicaps close to the given value')
async def handicap(interaction: discord.Interaction, number: float):
    # Find close handicaps
    close_handicaps = find_close_handicaps(number, handicaps)
    
    # If no close handicaps were found, respond accordingly
    if not close_handicaps:
        await interaction.response.send_message('No close handicaps found.')
        return

    # Randomly select one of the close handicaps
    selected_handicap = random.choice(close_handicaps)

    # Respond with the selected handicap's text
    await interaction.response.send_message(f"Selected Handicap: {selected_handicap['text']}")

# Load the bot token from a config file
with open('config.json') as config_file:
    config = json.load(config_file)

# Run the bot
bot.run(config['bot_token'])
