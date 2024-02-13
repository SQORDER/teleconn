import random
import os
import toml
import asyncio
from threading import Thread
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
with open("config.toml") as file:
    config = toml.load(file)
success = '0'
api_id = config["authorization"]["api_id"]
api_hash = config["authorization"]["api_hash"]
class Bio(Thread):
    def __init__(self, bio_text, tg_acc):
        Thread.__init__(self)
        self.bio_text = bio_text
        self.tg_acc = tg_acc
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            with TelegramClient("accs/" + self.tg_acc, api_id, api_hash) as client:
                client(UpdateProfileRequest(about=self.bio_text))
            if success == '0':
                print(f'[#] Bio has been updated on account {self.tg_acc}')
            else:
                print(f'[#] Bio has been updated on account {self.tg_acc}')
        except Exception as err:
            print(f'Error:\n{err}')
class Avatar(Thread):
    def __init__(self, tg_acc):
        Thread.__init__(self)
        self.tg_acc = tg_acc
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            with TelegramClient("accs/" + self.tg_acc, api_id, api_hash) as client:
                photo = 'avatars/' + random.choice(os.listdir('avatars/'))
                upload_file = client.upload_file(photo)
                client(UploadProfilePhotoRequest(upload_file))
                if success == '0':
                    print(f'[#] Avatar has been updated on account {self.tg_acc}')
                else:
                    print(f'[#] Avatar has been updated on account {self.tg_acc}')
        except Exception as err:
            print(f'Error:\n{err}')
class CreateName(Thread):
    def __init__(self, tg_acc, namelist, surnamelist):
        Thread.__init__(self)
        self.tg_acc = tg_acc
        self.namelist = namelist
        self.surnamelist = surnamelist
    def run(self):
        names = []
        for name in self.namelist:
            if name != "":
                names.append(name)
        surnames = []
        for surname in self.surnamelist:
            if surname != "":
                surnames.append(surname)
        name = random.choice(names)
        surname = random.choice(surnames)
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            with TelegramClient("accs/" + self.tg_acc, api_id, api_hash) as client:
                client(
                    UpdateProfileRequest(
                        first_name=name,
                        last_name=surname
                    )
                )
                if success == '0':
                    print(f'[#] Set name {name} {surname} on account {self.tg_acc}')
                else:
                    print(f'[#] Set name {name} {surname} on account {self.tg_acc}')
        except Exception as err:
            if success == '0':
                print(f'[#] Error:\n{err}')
            else:
                print(f'[#] Error:\n{err}')
