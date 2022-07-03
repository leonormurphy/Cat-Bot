import os
import discord
import requests #makes http requests to get data from the API
import json 
from replit import db
import random

imgs = [
  "Images/happyCat.jpg",
  "Images/politeCat.webp",
  "Images/happyCat.jpg",
  "Images/fancyCat.jpg",
  "Images/shookCat.webp",
  "Images/singingCat.jpg",
  "Images/strongCat.jpg"
]

#connection to discord
client = discord.Client()
    
#register an event
@client.event

#when the bot is ready
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#everytime a message is received
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #for our bot, all of the messages start with $
  if message.content.startswith('$inspire'):
    quote = get_quote
    await message.channel.send(quote)

  
  if message.content.startswith("cats"):
    await message.channel.send(file=discord.File(random.choice(imgs)))
      
#run the bot
client.run(os.environ['TOKEN'])
  