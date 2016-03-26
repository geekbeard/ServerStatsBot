from tokens import *
import telepot
import time
import psutil
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT

memorythreshold = 85  # If memory usage more this %

shellexecution = []
stopmarkup = {'keyboard': [['Stop']]}
hide_keyboard = {'hide_keyboard': True}

def clearall(chat_id):
    if chat_id in shellexecution:
        shellexecution.remove(chat_id)

class YourBot(telepot.Bot):
    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance2(msg)
        # Do your stuff according to `content_type` ...
        # print(chat_id)
        if chat_id == adminchatid:  # Store adminchatid variable in tokens.py
            if content_type == 'text':
                if msg['text'] == '/stats' and chat_id not in shellexecution:
                    bot.sendChatAction(chat_id, 'typing')
                    memory = psutil.virtual_memory()
                    disk = psutil.disk_usage('/')
                    boottime = datetime.fromtimestamp(psutil.boot_time())
                    now = datetime.now()
                    timedif = "Online for: %.1f Hours" % (((now - boottime).total_seconds()) / 3600)
                    memtotal = "Total memory: %.2f GB " % (memory.total / 1000000000)
                    memavail = "Available memory: %.2f GB" % (memory.available / 1000000000)
                    memuseperc = "Used memory: " + str(memory.percent) + " %"
                    diskused = "Disk used: " + str(disk.percent) + " %"
                    pids = psutil.pids()
                    pidsreply = ''
                    for pid in pids:
                        p = psutil.Process(pid)
                        try:
                            pmem = p.memory_percent()
                            if pmem > 1:
                                    pidsreply += p.name() + " " + ("%.2f" % pmem) + " %\n"
                        except:
                            None
                    reply = timedif + "\n" + \
                            memtotal + "\n" + \
                            memavail + "\n" + \
                            memuseperc + "\n" + \
                            diskused + "\n\n" + \
                            pidsreply
                    bot.sendMessage(chat_id, reply, disable_web_page_preview=True)
                elif msg['text'] == "Stop":
                    clearall(chat_id)
                    bot.sendMessage(chat_id, "All operations stopped.", reply_markup=hide_keyboard)
                elif msg['text'] == "/shell" and chat_id not in shellexecution:
                    bot.sendMessage(chat_id, "Send me a shell command to execute", reply_markup=stopmarkup)
                    shellexecution.append(chat_id)
                elif chat_id in shellexecution:
                    bot.sendChatAction(chat_id, 'typing')
                    p = Popen(msg['text'], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
                    output = p.stdout.read()
                    if output != b'':
                        bot.sendMessage(chat_id, output, disable_web_page_preview=True)
                    else:
                        bot.sendMessage(chat_id, "No output.", disable_web_page_preview=True)


TOKEN = telegrambot

bot = YourBot(TOKEN)
bot.notifyOnMessage()
tr = 0
# Keep the program running.
while 1:
    time.sleep(10)  # 10 seconds
    tr += 10
    if tr == 30:
        tr = 0
        memck = psutil.virtual_memory()
        mempercent = memck.percent
        memfree = memck.available / 1000000
        if mempercent > memorythreshold:
            memavail = "Available memory: %.2f GB" % (memck.available / 1000000000)
            bot.sendMessage(86298829, "CRITICAL! LOW MEMORY!\n" + memavail)
