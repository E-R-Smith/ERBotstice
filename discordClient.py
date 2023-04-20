from ast import arguments
import interactions
from interactions import Client, Intents, listen, slash_command, slash_option
import os

vc : interactions.TYPE_VOICE_CHANNEL | interactions.GuildChannel=''
tc : interactions.TYPE_MESSAGEABLE_CHANNEL | interactions.GuildChannel=''
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
    global tc
    await ctx.send("Hello World! :]")
    tc = ctx.channel

@slash_command(name="dictate_twitch", description="Pass twitch chat to SeaVoice tts")
async def dictate_twitch_function(ctx: interactions.InteractionContext):
    global vc, tc

    if (ctx.author.voice and not ctx.voice_state):
        # if we haven't already joined a voice channel
        # join the authors vc
        await ctx.send("Joining...")
        await ctx.author.voice.channel.connect()
        vc = ctx.author.voice.channel
        tc = ctx.channel
        await ctx.send('Bot joined')

        #await ctx.bot.connect_to_vc(vc._guild_id, ctx.author.voice._channel_id)
    else: #But is (s)he isn't in a voice channel
        await ctx.send("You must be in a voice channel first so I can join it.")

@slash_command(name="stop")
async def stop_function(ctx: interactions.InteractionContext):
    global vc, tc
    print(ctx.bot.get_bot_voice_state(ctx.guild_id))
    print(vc)
    print(ctx.bot.get_bot_voice_state(ctx.guild.id))
    await ctx.send("ran /stop")
    return
    await ctx.voice_state.channel.disconnect()
    return
    await vc.disconnect()
    if (bot.voice_client): # If the bot is in a voice channel 
        await bot.voice_client.disconnect() # Leave the channel
        await ctx.send('Bot left')
    else: # But if it isn't
        await ctx.send("I'm not in a voice channel, use the join command to make me join")


@slash_command(name="repeat")
@slash_option(
    name="msg",
    description="message",
    required=True,
    opt_type=interactions.OptionType.STRING
)
async def repeat_function(ctx: interactions.InteractionContext, msg: str):
    global tc
    tc = ctx.channel
    await repeat_text(msg)
    await ctx.send(":)")

async def repeat_text(msg : str):
    global tc
    await tc.send(f"{msg}", tts=True)


bot.load_extension("interactions.ext.jurigged")
bot.start()