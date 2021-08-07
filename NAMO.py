import os
import discord
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print("the bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith(">pranaam"):
       await message.channel.send(f"Jai Shree Ram! {message.author}")
    elif message.content.startswith(">kaise ho"):
      await message.channel.send(f"Main First Class,Mere Bhakto Tum Kaise Ho?") 
    elif message.content.startswith(">beef"):
      await message.channel.send(f"Gaay Humari Maata Hai! @{message.author} Agar Tumne Usko Kuch Kiya Toh Dekhlena")  
    elif message.content.startswith(">tax ke paiso ka kya kiya"):
      await message.channel.send(f"Usse Toh Main WORLD TOUR Kar Raha Hu LMAO")    
    elif message.content.startswith(">ache din kab aayenge"):
      await message.channel.send(f"Kabhi Nahi!! Maine Tumko Chutiya Banaya hehehe")    
    
TOKEN = os.environ['token']
keep_alive()
client.run(TOKEN)
