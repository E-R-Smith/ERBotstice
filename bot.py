import asyncio
import os
import threading
import dotenv
from threading import Thread
from twitchClient import tc as TwitchClient
from discordClient import bot as DiscordClient
from discordClient import relay


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread
    return wrapper


class Bot:
    tc = TwitchClient
    dc = DiscordClient
    tc.twitchEvents.on_msgRX += relay
    
    @threaded
    def start_twitch(self):
        self.tc.run()

    tThread = None
    dThread = None

    def start(self):
        print(f"Starting...")
        self.tThread = self.start_twitch()
        asyncio.run(self.dc.start(os.environ['DISCORD_TOKEN']))

    async def stop(self):
        await asyncio.wait_for(self.dc.close(), 5)
        print('Discord - Disconnected')
        print('Twitch - Disconnected')


bot = Bot()

if __name__ == "__main__":
    try:
        dotenv.load_dotenv()
        bot.start()
        while True:
            continue
    except KeyboardInterrupt:
        print('Shutting down...')
        asyncio.run(bot.stop())
        pass
