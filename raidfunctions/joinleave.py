import time
import random
import os
from threading import Thread
from raidfunctions import tgraid, leave
success = '0'
class JoinLeave(Thread):
    def __init__(self, accs, chat_id, chat_link):
        Thread.__init__(self)
        self.accs = accs
        self.chat_id = chat_id
        self.chat_link = chat_link
    def run(self):
        while True:
            for tg_acc in self.accs:
                tgraid.ConfJoin(
                    accs=tg_acc,
                    chat_link=self.chat_link,
                    captcha=0
                ).start()
            post = self.chat_id.split("/")
            channel = post[3]
            if post[3] == "c":
                channel = (int(post[4])+1000000000000)*-1
            for acc in self.accs:
                leave.Leave(acc, channel).start()
            time.sleep(random.randint(5, 7))
            for filename in os.listdir("accs"):
                if filename.endswith(".session-journal"):
                    os.remove(
                        os.path.join("accs", filename)
                    )
