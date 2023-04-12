import interactions
from interactions import Client, Intents, listen, slash_command
import os

vc : interactions.TYPE_VOICE_CHANNEL | interactions.GuildChannel= ''

# intents are what events we want to receive from discord, `DEFAULT` is usually fine
bot = Client(intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT, token=os.environ['DISCORD_TOKEN'])


@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Discord - Ready")

@listen()
async def on_message_create(event):
    # This event is called when a message is sent in a channel the bot can see
    print(f"D: {event.message.author.display_name}: {event.message.content}")

@slash_command(name="test", description="classic.")
async def my_command_function(ctx: interactions.InteractionContext):
    await ctx.send("Hello World!")

@slash_command(name="dictate_twitch", description="Pass twitch chat to SeaVoice tts")
async def dictate_twitch_function(ctx: interactions.InteractionContext):
    global vc
    if (ctx.author.voice): # If the person is in a channel
        vc = ctx.author.voice.channel
        await ctx.bot.connect_to_vc(vc._guild_id, ctx.author.voice._channel_id)
        await ctx.send('Bot joined')
    else: #But is (s)he isn't in a voice channel
        await ctx.send("You must be in a voice channel first so I can join it.")

@slash_command(name="stop")
async def stop_function(ctx: interactions.InteractionContext):
    if (ctx.voice_client): # If the bot is in a voice channel 
        await ctx.guild.voice_client.disconnect() # Leave the channel
        await ctx.send('Bot left')
    else: # But if it isn't
        await ctx.send("I'm not in a voice channel, use the join command to make me join")

bot.start()