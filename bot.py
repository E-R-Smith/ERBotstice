import os
import threading
from threading import Thread
from twitchClient import tc as TwitchClient
from discordClient import dc as DiscordClient


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


class Bot():
    tc = TwitchClient
    dc = DiscordClient
    
    @threaded
    def startTwitch(self):
        self.tc.run()
    @threaded
    def startDiscord(self):
        self.dc.start()

    tThread = None
    dThread = None

    def start(self):
        self.tThread = self.startTwitch()
        self.dThread = self.startDiscord()




bot = Bot()

if __name__ == "__main__":
    bot.start()
    while(True):
        continue