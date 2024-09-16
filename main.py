# i must admit that I literally copied this code from the previous repository, and modified it (named "createADiscordBotInPython")

import discord # importing the Discord library, use "pip install discord" or "conda install discord" to install it
from discord.ext import commands

intents = discord.Intents.default() # setting the intents the bot will be able to use, check it in the Discord Developers Portal so that the bot can send messages, etc.
intents.message_content = True # allowing the bot to send messages

bot = commands.Bot(
  intents=intents # assign intents to the bot
) # creating a bot instance, it is responsible for the application

@bot.event # decorator "@bot.event" allows you to listen for events
async def on_ready(): # we use an asynchronous "on_ready" function, it is executed when the bot is ready
   print("bot is ready") # sending a log, you can do anything else here, but if you want to do something related to the Discord API, use "await" before the command

@bot.event
async def on_message(message): # we use the asynchronous function "on_message" which is called when someone sends a message, and the "message" is an instance of the sent message
   if message.author == user.bot: # the command "message.author" refers to the user sending the message, "bot.user" refers to the bot instance made in "commands.Bot"
      return # returning nothing
   else:
      if message.content == "?ping": # "message.content" refers to the content of the message, (text) checking if the message is equal to "?ping"
         await message.channel.send("Pong!") # the "message.channel.send" command allows you to send a message to a channel, "message.channel" refers to the instance of the channel on which the user sent the message

@bot.run("token") # replace the "token" with your token from the "Bot" tab in the Discord Developers Portal, and give it here (as a string), remember not to share it with ANYONE
