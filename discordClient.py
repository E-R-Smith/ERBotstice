# This example requires the 'message_content' intent.
import asyncio
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

textChannel: discord.TextChannel = None
voiceChannel: discord.VoiceChannel = None

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.listen()
async def on_ready():
    print(f'Discord - Ready')


@bot.listen()
async def on_message(message):
    print(f'{message.author}: {message.content}')


@bot.hybrid_command()
async def test(ctx):
    await ctx.send("This is a hybrid command!")


@bot.hybrid_command(name="bind")
async def bind(ctx : discord.ext.commands.Context):
    global textChannel
    await ctx.send(f"Binding twitch relay to #{ctx.channel}")
    textChannel = ctx.channel

    
@bot.hybrid_command(name='unbind')
async def unbind(ctx : discord.ext.commands.Context):
    global textChannel
    textChannel = None
    await ctx.send("Text relay channel unbound")


def relay(msg: str):
    if textChannel is not None:
        asyncio.run_coroutine_threadsafe(textChannel.send(msg), bot.loop)

# dotenv load()
# bot.run(os.environ['DISCORD_TOKEN'])
