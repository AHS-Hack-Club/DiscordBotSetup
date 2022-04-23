import os # Allows to safely access the bot token

# Allows us to create a new bot which we can modify 
from discord.ext import commands

bot = commands.Bot() # Creates a new bot

# Creates a bot "event" which prints to us when the robot is running
@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}') # bot.user is the username of the bot

bot.run(os.getenv('TOKEN')) # Activates the bot (takes in the bot's user token)