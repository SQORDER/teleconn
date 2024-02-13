import os
import toml
import ctypes
import asyncio
from raidfunctions import register
from raidfunctions import tgraid
from raidfunctions import additional 
from raidfunctions import start_spam
from raidfunctions import joinleave
from raidfunctions import addsticker
from raidfunctions import see 
from raidfunctions import report
from raidfunctions import leave
from raidfunctions import polls 

print('''
                  88                                                          
  ,d              88                                                          
  88              88                                                          
MM88MMM ,adPPYba, 88  ,adPPYba,  ,adPPYba,  ,adPPYba,  8b,dPPYba,  8b,dPPYba,   
  88   a8P_____88 88 a8P_____88 a8"     "" a8"     "8a 88P'   `"8a 88P'   `"8a  
  88   8PP""""""" 88 8PP""""""" 8b         8b       d8 88       88 88       88 
  88,  "8b,   ,aa 88 "8b,   ,aa "8a,   ,aa "8a,   ,a8" 88       88 88       88 
  "Y888 `"Ybbd8"' 88  `"Ybbd8"'  `"Ybbd8"'  `"YbbdP"'  88       88 88       88  
''')
print('''
Created by 0x892 (github.com/0x892)
    ''')
text_spam = ('accs :' '{acc}!')


success = '0'


try:
    libgcc_s = ctypes.CDLL('libgcc_s.so.1')
except:
    pass
with open("config.toml") as file:
    config = toml.load(file)


if success == '0':
    menu = '''
[#] After operation restart program!
[#] Choose operation:

[0] Register or authorize acc
[1] Classic attack
[2] Join a chat/channel
[3] Send reports to message or post
[4] Add or remove stickers
[5] Other functions
[6] Increase views
[7] Vote in a poll
'''
    raidmenu = '''
[#] Raid Menu

[1] Spam a chat
[2] Spam in private chat to user
[3] Spam in channel's comments
[4] Spam in private chat to user via contact input
[5] Spam with forwarding message or post
[6] Join/Leave spam
[7] Spam with mention to one user
[8] Leave chat/channel
'''


for filename in os.listdir("accs"):
    if filename.endswith(".session-journal"):
        os.remove(
            os.path.join("accs", filename)
        )
acc_count = len(os.listdir("accs"))
if success == '0':
    print(f"[!] Accs : {acc_count}")

while True:
    try:
        accs = os.listdir('accs')
        a = int(input(menu))
        if a == 0:
            while True:
                if success == '0':
                    print('''
[1] Authorize acc or register
[2] Get activation code for authorization
[3] Check accs validation
[4] Check accs spamblock
[5] Set 2fa auth on accounts'''
                    )
                c = int(input())
                accounts = os.listdir('accs')
                if c == 1:
                    if success == '0':
                        name = input("[#] Name session :\n")
                    register.Register(name, 1, None, None).regaccountreg()
                elif c == 2:
                    if success == '0':
                        print("[#] Enter Phone Number\n")
                    else:
                        print("[#] Enter Phone Number\n")
                    name = input()
                    register.Register(name, 2, None, None).checkcode()
                elif c == 3:
                    for account in accounts:
                        register.Register(account, 4, None, None).start()
                elif c == 4:
                    for account in accounts:
                        register.Register(account, 3, None, None).start()
                elif c == 5:
                    if success == '0':
                        old_pwd = input("[#] Old Password (if exists):\n")
                    else:
                        old_pwd = input("[#] Enter old password (if exists):\n")
                    if success == '0':
                        pwd = input("[#] New Password:\n")
                    else:
                        pwd = input("[#] Enter new password:\n")
                    for account in accounts:
                        register.Register(account, 5, pwd, old_pwd).start()
        elif a == 1:
            b = int(input(raidmenu))
            if b == 1:
                spam = start_spam.Settings(False)
                spam.start_spam()
            elif b == 2:
                if success == '0':
                    idtg = input("[#] Username :\n")
                    spam_type = int(input('''
[1] Spam via text
[2] Spam via media
[3] Spam via Sticker\n'''))
                    msg_tp = int(input('''
[1] args.txt 
[2] config.toml\n'''))
                else:
                    idtg = input("[#] Enter person's username\n")
                    spam_type = int(input('''
[1] Spam via text
[2] Spam via media
[3] Spam via Sticker\n'''))
                    msg_tp = int(input('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n'''))
                files = []
                if spam_type in [1, 2]:
                    msg = start_spam.Settings(False).get_messages(msg_tp)
                else:
                    msg = ''
                if spam_type == 2:
                    files = os.listdir('raidfiles')
                for acc in accs:
                    try:
                        if success == '0':
                        	#print(f"Spam has been launched from {acc} acc!")
                            print(f"{text_spam}")
                        else:
                        	#print(f"Spam has been launched from {acc} acc!")
                            print(f"Spam with {acc}!")
                        tgraid.LsRaid(
                            user_id=idtg,
                            session_name=acc,
                            msg_tp=msg_tp,
                            messages=msg,
                            files=files,
                            spam_type=spam_type
                        ).start()
                    except:
                        pass
            elif b == 3:
                if success == '0':
                    idtg = input("Post : \n").split("/")
                    spam_type = int(input('''
[1] Spam via text
[2] Spam via media
[3] Spam via Sticker\n'''))
                    msg_tp = int(input('''
[1] args.txt 
[2] config.toml\n'''))
                else:
                    idtg = input("[#] Enter post link: \n").split("/")
                    spam_type = int(input('''
[1] Spam via text
[2] Spam via media
[3] Spam via Sticker\n'''))
                    msg_tp = int(input('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n'''))
                channel = idtg[3]
                post_id = idtg[4]
                files = []
                if channel == 'c':
                    channel = idtg[4]
                    post_id = idtg[5]
                msg = start_spam.Settings(False).get_messages(msg_tp)
                if spam_type == 2:
                    files = os.listdir('raidfiles')
                if success == '0':
                    print('''
[#] SPEED RAID
[1] Fast
[2] Slow\n''')
                else:
                    print('''
[#] SPEED RAID
[1] Fast
[2] Slow\n''')
                speed = int(input())
                for acc in accs:
                    try:
                        if success == '0':
                            print(f"{text_spam}")
                        else:
                            print(f"Spam with {acc}!")
                        tgraid.RaidComments(
                            channel=channel,
                            session_name=acc,
                            msg_tp=msg_tp,
                            messages=msg,
                            spam_type=spam_type,
                            post_id=post_id,
                            files=files,
                            speed=speed
                        ).start()
                    except:
                        pass
            elif b == 4:
                if success == '0':
                    phonetg = input("[#] Number Flood:\n")
                else:
                    phonetg = input("[#] Enter victim's phone number:\n")
                phone_tg = ""
                for s in phonetg:
                    if s not in [" ", "(", ")"]:
                        phone_tg += s
                print(phone_tg)
                files = []
                if success == '0':
                    spam_type = int(input('''
[1] Spam via text
[2] Spam via media
[3] Spam via Sticker\n'''))
                else:
                    spam_type = int(input('''
[1] Spam via text
[2] Spam via media
[3] Spam via Sticker\n'''))
                if spam_type == 1:
                    if success == '0':
                        msg_tp = int(input('''
[1] args.txt 
[2] config.toml\n'''))
                    else:
                        msg_tp = int(input('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n'''))
                    msg = start_spam.Settings(False).get_messages(msg_tp)
                else:
                    if success == '0':
                        msg_tp = int(input('''
[1] args.txt 
[2] config.toml\n'''))
                    else:
                        msg_tp = int(input('''
[1] Spam with sentences from args.txt
[2] Repeat phrace from config.toml\n'''))
                    msg = start_spam.Settings(False).get_messages(msg_tp)
                    files = os.listdir('raidfiles')
                for acc in accs:
                    try:
                        if success == '0':
                            print(f"{text_spam}")
                        else:
                            print(f"Spam with {acc}!")
                        tgraid.PhoneLsRaid(
                            phone_tg=phone_tg,
                            session_name=acc,
                            msg_tp=msg_tp,
                            messages=msg,
                            files=files,
                            spam_type=spam_type
                        ).start()
                    except:
                        pass
            elif b == 5:
                if success == '0':
                    fwd_link = input('[#] Copy and paste forwadding message link from chat:\n').split("/")
                    msg_link = input('[#] Copy and paste message link from chat:\n').split("/")
                else:
                    fwd_link = input('[#] Copy and paste forwadding message link from chat:\n').split("/")
                    msg_link = input('[#] Copy and paste message link from chat:\n').split("/")
                chat = fwd_link[3]
                post_id = fwd_link[4]
                if fwd_link[3] == "c":
                    chat = (int(fwd_link[4]) + 1000000000000) * -1
                    post_id = fwd_link[5]
                spam_chat = msg_link[3]
                if msg_link[3] == "c":
                    spam_chat = (int(msg_link[4]) + 1000000000000) * -1
                for acc in accs:
                    try:
                        tgraid.ForwardSpam(
                            session_name=acc,
                            chat=chat,
                            post_id=post_id,
                            spam_chat=spam_chat
                        ).start()
                    except:
                        pass
            elif b == 6:
                if success == '0':
                    link_to_chat = input('[#] Link:\n')
                    print("[#] Copy message or post link:\n")
                else:
                    link_to_chat = input('[#] Enter chat link:\n')
                    print("[#] Copy message or post link:\n")
                msg_link = input()
                joinleave.JoinLeave(accs, msg_link, link_to_chat).start()
            elif b == 7:
                if success == '0':
                    print('''
[1] USERNAME TAG
[2] ID TAG''')
                else:
                    print('''
[1] Mention via username
[2] Mention via telegram id''')
                ch = int(input())
                if ch == 1:
                    if success == '0':
                        print("[#] Enter username with @:")
                    else:
                        print("[#] Enter username with @:")
                    username = input()
                elif ch == 2:
                    if success == '0':
                        print("[#] ID TELEGRAM")
                    else:
                        print("[#] Enter telegram id")
                    username = f"<a href='tg://user?id={input()}'>.</a>"
                else:
                    username = ""
                spam = start_spam.Settings(False, username)
                spam.start_spam()
            elif b == 8:
                if success == '0':
                    print("[#] Copy message or post link:")
                else:
                    print("[#] Copy message or post link:")
                post = input().split("/")
                channel = post[3]
                if post[3] == "c":
                    channel = (int(post[4])+1000000000000)*-1
                for acc in accs:
                    try:
                        leave.Leave(acc, channel).start()
                    except:
                        pass
        elif a == 2:
            spam = start_spam.Settings(True)
            spam.start_spam()
        elif a == 3:
            post_ids = []
            if success == '0':
                msg_link = input('[#] Copy and paste message link from chat: \n').split("/")
            else:
                msg_link = input('[#] Copy and paste message link from chat: \n').split("/")
            channel = msg_link[3]
            post_id = msg_link[4]
            if msg_link[3] == "c":
                channel = (int(msg_link[4]) + 1000000000000) * -1
                post_id = msg_link[5]
            post_ids.append(int(post_id))
            if success == '0':
                m1 = '''
[#]Choose a reason of reporting:
                    
[1] CP
[2] Stolen content
[3] Fake account or channel
[4] Pornography
[5] Spam
[6] Violence
[7] Other'''
            else:
                m1 = '''
[#]Choose a reason of reporting:
                    
[1] CP
[2] Stolen content
[3] Fake account or channel
[4] Pornography
[5] Spam
[6] Violence
[7] Other'''
            print(m1)
            reason_num = int(input())-1
            if success == '0':
                comment = input("[#] Write comment about report: \n")
                print("[!] Reports has been activated...")
            else:
                print('[!] Reports has been activated...')
                comment = input("[#] Write comment about report: \n")
            for acc in accs:
                try:
                    report.Report(
                        acc=acc,
                        post_ids=post_ids,
                        reason_num=reason_num,
                        comment=comment,
                        channel=channel
                    ).start()
                except:
                    pass
        elif a == 4:
            if success == '0':
                print('''
[1] Add stickerpacks
[2] Remove stickerpacks''')
            else:
                print('''
[1] Add stickerpacks
[2] Remove stickerpacks''')
            m = int(input())
            if m == 1:
                if success == '0':
                    your_id = int(input("[#] Enter your telegram id then send sticker into the chat with bots: \n"))
                else:
                    your_id = int(input("[#] Enter your telegram id then send sticker into the chat with bots: \n"))
                for acc in accs:
                    try:
                        addsticker.AddStickerpack(acc, your_id).start()
                    except:
                        pass
            if m == 2:
                for acc in accs:
                    try:
                        addsticker.RemoveStickerpacks(acc).start()
                    except:
                        pass
        elif a == 5:
            if success == '0':
                print('''
[1] Set bio
[2] Set avatar
[3] Set name
[4] Leave from channels & chats'''
                )
            else:
                print('''
[1] Set bio
[2] Set avatar
[3] Set name
[4] Leave from channels & chats'''
                )
            a = int(input())
            if a == 1:
                if success == '0':
                    bio_text = input("[#] Enter bio: \n")
                else:
                    bio_text = input("[#] Enter bio: \n")
                for acc in accs:
                    try:
                        additional.Bio(bio_text, acc).start()
                    except:
                        pass
            if a == 2:
                for acc in accs:
                    try:
                        additional.Avatar(acc).start()
                    except:
                        pass
            if a == 3:
                f = open("name.txt", encoding='utf-8', errors='ignore')
                namelist = f.read().split('\n')
                v = open("surname.txt", encoding='utf-8', errors='ignore')
                surnamelist = v.read().split('\n')
                f.close()
                v.close()
                for acc in accs:
                    try:
                        additional.CreateName(
                            acc,
                            namelist,
                            surnamelist
                        ).start()
                    except:
                        pass
            if a == 4:
                accs = os.listdir("accs")
                x = 1
                if success == '0':
                    print("[#] Choose an account:")
                else:
                    print("[#] Choose an account:")
                for acc in accs:
                    print(f"{x}. {acc}")
                    x += 1
                acc_input = int(input())-1
                if success == '0':
                    s = input("[#] Sure that you want to clear chats? y/n\n")
                else:
                    s = input("[#] Sure that you want to clear chats? y/n\n")
                if s == "y":
                    leave.LeaveChat(accs[acc_input]).start()
        elif a == 6:
            accs = os.listdir("accs")
            if success == '0':
                a = input('[#] Enter post link:\n ')
            else:
                a = input('[#] Enter post link:\n ')
            b = a.split(',')
            ids = []
            private = False
            channel = b[0].split('/')[3]
            for x in b:
                x1 = x.split('/')
                if channel == "c":
                    private = True
                    ids.append(int(x1[5]))
                else:
                    ids.append(int(x1[4]))

            if private:
                channel = b[0].split('/')[4]
            for acc in accs:
                try:
                    view = see.Channel(acc, channel, ids, private)
                    view.start()
                except:
                    pass
        elif a == 7:
            if success == '0':
                poll_link = input("[#] Enter message link with poll: \n")
            else:
                poll_link = input("[#] Enter message link with poll: \n")
            input_variants = input('''
[#] Choose a variants: 
[$] Exmaple : 1, 2...\n''')

            variants = []
            for variant in input_variants.split(","):
                variants.append(str(int(variant)-1))
            private = False
            channel = poll_link.split('/')[3]
            x = poll_link.split('/')
            if channel == "c":
                private = True
                poll_id = int(x[5])
            else:
                poll_id = int(x[4])

            if private:
                channel = poll_link.split('/')[4]
            for acc in accs:
                try:
                    view = polls.Channel(acc, channel, poll_id, variants, private)
                    view.start()
                except:
                    pass

    except KeyboardInterrupt:
        break
    except ValueError:
        break
