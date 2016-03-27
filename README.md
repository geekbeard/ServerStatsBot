# Server Manager Bot

A Telegram Bot:

* Commands
    * `/stats` - gives summed statistics about memory \ disk \ processes (will improve)
    * `/shell` - goes into the mode of executing shell commands & sends you the output
    * `/memgraph` - plots a graph of memory usage for a past period and sends you a picture of the graph
* Monitors memory usage and if it reaches above the set threshold = sends you warning message


Example summary: (will improve)

![Bot](http://i.imgur.com/RnVdXlB.png)


Example shell command output as a message from the bot:

![Shell](https://i.imgur.com/PtvcaSD.png)


Example graph sent by bot:

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
   
## Running the bot

`python3 servstatsbot.py`

## Setting an admin

You have to set a variable `adminchatid` in `tokens.py` to be equal your chat_id or multiple chat_id (if more people will use your bot).
For example:

* `adminchatid = [443355]`
* `adminchatid = [443355, 55667788, 99884433]`

I will reimplement this differently later.
        

# Bot key
(lame way to keep the key safe)

Hide all the keys and admin variables in `tokens.py`.
Use it only for sensitive variables. Avoid creating functions not to clutter the namespaces through the import.

* Get a key from the [Bot Father](https://telegram.me/BotFather)
* Clone that repo
* In the folder with the cloned repo create a file `tokens.py`
    * It's added to the `.gitignore` so you don't commit your own (and I don't commit mine:)
* In that file put a string variable `telegrambot` which equals your key
    * For example: `telegrambot = "000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"`
 
# PLEASE CONTRIBUTE :)
 I threw this code together within 10 minutes or so as a mockup to work on it later. But I think it's a nice bot idea and some of you guys might like this too. So please feel free to fork, pull, requests features!
 Can give contributors access!
 Would really love to see this bot grow some fat and brain:)
 
 
 GB
