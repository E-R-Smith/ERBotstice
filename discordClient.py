# This example requires the 'message_content' intent.
import os
import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')

# intents = discord.Intents.default()
# intents.message_content = True
# intents.voice_states = True


# client = MyClient(intents=intents)
# client.run(os.environ['DISCORD_TOKEN'])

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.hybrid_command()
async def test(ctx):
    await ctx.send("This is a hybrid command!")

@bot.listen()
async def on_ready():
    print(f'Discord - Ready')

@bot.listen()
async def on_message(message):
    print(f'{message.author}: {message.content}')

#dotenv load()
#bot.run(os.environ['DISCORD_TOKEN'])
