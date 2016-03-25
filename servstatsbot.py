from tokens import *
import telepot
import time
import psutil
from datetime import datetime

testing = False  # !!!!!!!!!!!!!!!!!!!!!!!! TEST BOT OR PRODUCTION BOT !!!!!!!!!!!!!

# scputimes(user=29834.13, nice=0.0, system=13796.32, idle=763043.78)
# svmem(total=8589934592, available=2068557824, percent=75.9, used=6165536768, free=196009984, active=3025891328, inactive=1872547840, wired=1267097600)
# sdiskusage(total=248828264448, used=167839813632, free=80726306816, percent=67.5)


class YourBot(telepot.Bot):
    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance2(msg)
        # Do your stuff according to `content_type` ...
        if content_type == 'text':
            if msg['text'] == '/stats':
                bot.sendChatAction(chat_id, 'typing')
                # reply =
                memory = psutil.virtual_memory()
                disk = psutil.disk_usage('/')
                boottime = datetime.fromtimestamp(psutil.boot_time())
                now = datetime.now()
                timedif = "Online for: %.1f Hours" % (((now - boottime).total_seconds()) / 3600)
                # print(timedif)
                memtotal = "Total memory: %.2f GB " % (memory.total / 1000000000)
                memavail = "Available memory: %.2f GB" % (memory.available / 1000000000)
                memuseperc = "Used memory: " + str(memory.percent) + " %"
                diskused = "Disk used: " + str(disk.percent) + " %"
                # print(psutil.cpu_times())
                # print(memtotal +"\n"+memavail+ "\n" +memuseperc+"\n\n"+diskused)
                # print(psutil.disk_usage('/'))
                pids = psutil.pids()
                pidsreply = ''
                for pid in pids:
                    p = psutil.Process(pid)
                    try:
                        pmem = p.memory_percent()
                        if pmem > 1:
                                pidsreply += p.name() + " " + ("%.2f" % pmem) + " %\n"
                    except:
                        print("error")
                bot.sendMessage(chat_id, memtotal +"\n"+memavail+ "\n" +memuseperc+"\n\n"+diskused+"\n\n"+pidsreply)

TOKEN = telegrambot

bot = YourBot(TOKEN)
bot.notifyOnMessage()
tr = 0
# Keep the program running.
while 1:
    time.sleep(10)  # 10 seconds
    tr += 10
    if tr == 300:
        tr = 0
        memck = psutil.virtual_memory()
        memfree = memck.available / 1000000
        memavail = "Available memory: %.2f GB" % (memck.available / 1000000000)
        if memfree < 300:
            bot.sendMessage(86298829, "WARNING! LOW MEMORY!\n"+memavail)
