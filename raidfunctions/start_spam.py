import os
import toml
import time
from raidfunctions import tgraid
with open("config.toml") as file:
    config = toml.load(file)
success = '0'
raid_message = config["raid"]["message"]
class Settings:
    def __init__(self, join_chat, username=""):
        self.join_chat = join_chat
        self.username = username
    def get_messages(self, msg_type):
        ms = ""
        if msg_type == 1:
            a = open('args.txt', encoding='utf8')
            ms = a.read().split('\n')
            a.close()
            new_ms = []
            for m in ms:
                if m != "":
                    new_ms.append(self.username+" "+m)
            ms = new_ms
        elif msg_type == 2:
            ms = self.username+" "+raid_message
        return ms
    def start_spam(self):
        tg_accounts = os.listdir('accs')
        if not self.join_chat:
            answ = tgraid.PrepareRaid().questions()
            mentions = False
            if answ[2] == 1:
                if success == '0':
                    print('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n''')
                else:
                    print('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n''')
                msg_type = int(input())
                messages = self.get_messages(msg_type)
                if success == '0':
                    mentions_q = int(input("[#] Tag chat members?\n[1] Yes\n[2] No\n"))
                else:
                    mentions_q = int(input("[#] Tag chat members?\n[1] Yes\n[2] No\n"))
                if mentions_q == 1:
                    mentions = True
                for account in tg_accounts:
                    if success == '0':
                        print(f"[#] Spam with {account}!")
                    else:
                        print(f"[#] Spam has been launched from {account} acc!")
                    tgraid.RaidGroup(
                        session_name=account,
                        spam_type=answ[2],
                        files='',
                        messages=messages,
                        chat_id=answ[0],
                        msg_tp=msg_type,
                        speed=answ[1],
                        mentions=mentions
                    ).start()
            if answ[2] == 2:
                if success == '0':
                    msg_type = int(input('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n'''))
                    print('Media for spam is taken from folder "raidfiles"')
                else:
                    msg_type = int(input('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n'''))
                    print('Media for spam is taken from folder "raidfiles"')
                messages = self.get_messages(msg_type)
                files = os.listdir('raidfiles')
                if success == '0':
                    mentions_q = int(input("[#] Tag chat members?\n[1] Yes\n[2] No\n"))
                else:
                    mentions_q = int(input("[#] Tag chat members?\n[1] Yes\n[2] No\n"))
                if mentions_q == 1:
                    mentions = True
                for account in tg_accounts:
                    if success == '0':
                        print(f"[#] Spam has been launched from {account} acc!")
                    else:
                        print(f"[#] Spam has been launched from {account} acc!")
                    tgraid.RaidGroup(
                        session_name=account,
                        spam_type=answ[2],
                        files=files,
                        messages=messages,
                        chat_id=answ[0],
                        msg_tp=msg_type,
                        speed=answ[1],
                        mentions=mentions
                    ).start()
            if answ[2] == 3:
                for account in tg_accounts:
                    if success == '0':
                        print(f"[#] Spam has been launched from {account} acc!")
                    else:
                        print(f"[#] Spam has been launched from {account} acc!")
                    tgraid.RaidGroup(
                        session_name=account,
                        spam_type=answ[2],
                        files='',
                        messages=[],
                        chat_id=answ[0],
                        msg_tp=0,
                        speed=answ[1],
                        mentions=False
                    ).start()
            if success == '0':
                print(
                    '[#] Accounts has been launched!\n'
                    f'[#] Send command "{answ[0]}" from activating spam!'
                )
            else:
                print(
                    '[#] Accounts has been launched!\n'
                    f'[#] Send command "{answ[0]}" from activating spam!'
                )
        else:
            if success == '0':
                link_to_chat = input('[#] Enter chat link: \n')
                captcha_q = int(input('[#] Solve captcha?\n[1] Yes\n[2] No\n'))
            else:
                link_to_chat = input('[#] Enter chat link: \n')
                captcha_q = int(input('[#] Solve captcha?\n[1] Yes\n[2] No\n'))
            captcha = 0
            if captcha_q == 1:
                if success == '0':
                    captcha = int(input('[?] Captcha type:\n[1] Button\n[2]Math example\n'))
                else:
                    captcha = int(input('[?] Captcha type:\n[1] Button\n[2]Math example\n'))

            for tg_acc in tg_accounts:
                tgraid.ConfJoin(
                    accs=tg_acc,
                    chat_link=link_to_chat,
                    captcha=captcha
                ).start()
                if captcha_q == 1:
                    time.sleep(5)
