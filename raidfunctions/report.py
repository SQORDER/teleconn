import toml
import asyncio
from telethon.sync import TelegramClient
from telethon import functions, types
from threading import Thread
success = '0'
with open("config.toml") as file:
    config = toml.load(file)    
api_id = config["authorization"]["api_id"]
api_hash = config["authorization"]["api_hash"]
class Report(Thread):
    def __init__(self, acc, post_ids, reason_num, comment, channel):
        Thread.__init__(self)
        self.acc = acc
        self.post_ids = post_ids
        self.reason_num = reason_num
        self.comment = comment
        self.channel = channel
        self.reasons = [
            types.InputReportReasonChildAbuse(),
            types.InputReportReasonCopyright(),
            types.InputReportReasonFake(),
            types.InputReportReasonPornography(),
            types.InputReportReasonSpam(),
            types.InputReportReasonViolence(),
            types.InputReportReasonOther()
        ]
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            with TelegramClient("accs/"+self.acc, api_id, api_hash) as client:
                try:
                    result = client(functions.messages.ReportRequest(
                        peer=self.channel,
                        id=self.post_ids,
                        reason=self.reasons[self.reason_num],
                        message=self.comment
                    ))
                    if result:
                        if success == '0':
                            print(f"[#] Report has been sended succesfully from {self.acc}!")
                        else:
                            print(f"[#] Report has been sended succesfully from {self.acc}!")
                except Exception as error:
                    print(f"[#] Error:\n{error}")
        except Exception as error:
            print(f"[#] Error:\n{error}")
