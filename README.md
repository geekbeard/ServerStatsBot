# Server Stats Bot

A Telegram Bot:

* Commands
    * `/stats` - gives summed statistics about memory \ disk \ processes (will improve)
    * `/shell` - goes into the mode of executing shell commands & sends you the output
    * `/memgraph` - plots a graph of memory usage for a past period and sends you a picture of the graph
* Monitors memory usage and if it reaches above the set threshold = sends you warning message


![Bot](http://i.imgur.com/RnVdXlB.png)

# Requires

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
   
        

# Bot key
(lame way to keep the key safe)

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
