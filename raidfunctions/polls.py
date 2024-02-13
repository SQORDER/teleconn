import asyncio
import toml
from telethon.sync import TelegramClient
from telethon import functions
from threading import Thread
with open("config.toml") as file:
    config = toml.load(file)
success = '0'
api_id = config["authorization"]["api_id"]
api_hash = config["authorization"]["api_hash"]
class Channel(Thread):
    def __init__(self, acc, channel, poll_id, variants, private):
        Thread.__init__(self)
        self.acc = acc
        self.channel = channel
        self.poll_id = poll_id
        self.variants = variants
        self.private = private
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        if self.private:
            self.channel = -1000000000000-int(self.channel)
        with TelegramClient("accs/"+self.acc, api_id, api_hash) as client:
            try:
                client(functions.messages.SendVoteRequest(
                    peer=self.channel,
                    msg_id=self.poll_id,
                    options=self.variants
                ))
                if success == '0':
                    print(f'{self.acc} проголосовал!')
                else:
                    print(f'{self.acc} has voted!')
            except:
                if success == '0':
                    print(f'{self.acc} не смог проголосовать!')
                else:
                    print(f'{self.acc} cannot vote!')