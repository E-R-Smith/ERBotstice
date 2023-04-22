from twitchio.ext import commands
import os
import dotenv


class TwitchClient(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(
            token=os.environ['TWITCH_TOKEN'],
            prefix=os.environ['TWITCH_PREFIX'],
            initial_channels=[os.environ['TWITCH_CHANNEL']],
            nick=os.environ['TWITCH_BOT_NICK']
        )

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print("Twitch - Ready")

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)


dotenv.load_dotenv()
tc = TwitchClient()


# region Twitch Commands
@tc.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')
# endregion
