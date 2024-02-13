import asyncio
import toml
from threading import Thread
from telethon.sync import TelegramClient, events
from telethon import functions, types
from telethon.tl.functions.messages import GetAllStickersRequest
with open("config.toml") as file:
    config = toml.load(file)
success = '0'
api_id = config["authorization"]["api_id"]
api_hash = config["authorization"]["api_hash"]
class AddStickerpack(Thread):
    def __init__(self, session_name, your_id):
        Thread.__init__(self)
        self.session_name = session_name
        self.your_id = your_id
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient("accs/"+self.session_name, api_id, api_hash)
        client.connect()
        @client.on(events.NewMessage)
        async def my_event_handler(event):
            try:
                if event.message.media is not None and event.from_id.user_id == self.your_id:
                    sticker = event.message.media.document.attributes[1].stickerset
                    sticker_id = sticker.id
                    sticker_hash = sticker.access_hash
                    await client(functions.messages.InstallStickerSetRequest(
                        stickerset=types.InputStickerSetID(
                            id=sticker_id,
                            access_hash=sticker_hash
                        ),
                        archived=False
                    ))
                    if success == '0':
                        print(f"[#] Stickerpack has been successfully added to {self.session_name}!")
                    else:
                        print(f"[#] Stickerpack has been successfully added to {self.session_name}!")
                    await client.disconnect()
            except:
                pass
        client.start()
        client.run_until_disconnected()
class RemoveStickerpacks(Thread):
    def __init__(self, session_name):
        Thread.__init__(self)
        self.session_name = session_name
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient("accs/"+self.session_name, api_id, api_hash)
            client.connect()
            sticker_sets = client(GetAllStickersRequest(0)).sets
            for sticker_set in sticker_sets:
                client(functions.messages.UninstallStickerSetRequest(
                    stickerset=types.InputStickerSetID(
                        id=sticker_set.id,
                        access_hash=sticker_set.access_hash
                    )
                ))
            client.disconnect()
            if success == '0':
                print(f"[#] Stickerpacks has been removed from {self.session_name}!")
            else:
                print(f"[#] Stickerpacks has been removed from {self.session_name}!")
        except:
            pass
