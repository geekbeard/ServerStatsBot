# Server Manager Bot

Этот Telegram бот умеет:

* Комманды
    * `/stats` - дает обобщенную статистику о памяти \ диске \ процессах.
    * `/shell` - позволяет использовать бот в режиме Shell.
    * `/memgraph` - строит график использования памяти за прошедший период и отправляет вам изображение графика.
    * `/setmem` - возможность установить порог оперативной памяти (%) для мониторинга.
    * `/setpoll` - интервал опроса в секундах (выше 10).
* Отслеживает использование памяти и, если она превышает установленное пороговое значение =, отправляет вам предупреждение.


Как это работает: [Gif](https://i.13.wf/2019/08/17/1566074720-2541.gif)

![Bot](https://i.13.wf/2019/08/17/1566074746-9489.png)


Example shell command output as a message from the bot: 

![Shell](https://i.imgur.com/PtvcaSD.png)


Example graph sent by bot: [Gif](http://i.imgur.com/anX7rJR.gifv)

![Graph](http://i.imgur.com/K8mG3aM.jpg?1)

# Usage

## Requirements 

* Python 3+
* [Telepot](https://github.com/nickoala/telepot)
* [Psutil](https://github.com/giampaolo/psutil)
    * Make sure to install it for Python 3+
    * In order to make sure that `pip` installs packages for the 3+ version:
        * `curl -O https://bootstrap.pypa.io/get-pip.py`
        * `sudo python3 get-pip.py`
        * After that `pip install psutil`
        * Also Stackoverflow question about that [here](http://stackoverflow.com/questions/11268501/how-to-use-pip-with-python-3-x-alongside-python-2-x)
* [matplotlib](http://matplotlib.org/)
    * `sudo apt-get install python3-matplotlib`
* Bot key & `tokens.py`
    * Hide all the keys and admin variables in `tokens.py`. Use it only for sensitive variables. Avoid creating functions not to clutter the namespaces through the import.
    * Get a key from the [Bot Father](https://telegram.me/BotFather)
    * Clone that repo
    * In the folder with the cloned repo create a file `tokens.py`
       * It's added to the `.gitignore` so you don't commit your own (and I don't commit mine:)
    * In that file put a string variable `telegrambot` which equals your key
       * For example: `telegrambot = "000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"`
   
## Running the bot

`python3 servstatsbot.py`

## Running the bot as "daemon"

* See included file in the repo: `servstatsbot.conf`
    * Open it and edit the path as mentiond in the comments there
* Place that file in `/etc/init/`
* Start the "daemon" with: `start servstatsbot`
    * You can start|stop|restart
    * If bot crashes it'll be automatically restarted
    * It will also start after reboot

## Setting an admin

You have to set a variable `adminchatid` in `tokens.py` to be equal your chat_id or multiple chat_id (if more people will use your bot).
For example:

* `adminchatid = [443355]`
* `adminchatid = [443355, 55667788, 99884433]`

I will reimplement this differently later.
        
 
# PLEASE CONTRIBUTE :)
 I threw this code together within 10 minutes or so as a mockup to work on it later. But I think it's a nice bot idea and some of you guys might like this too. So please feel free to fork, pull, requests features!
 Can give contributors access!
 Would really love to see this bot grow some fat and brain:)
 
 
# Other bot development
 
## Alfred
[http://alfredthebot.com](http://alfredthebot.com)
 
 
 GB
