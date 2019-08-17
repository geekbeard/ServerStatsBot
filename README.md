# Server Manager Bot

Этот Telegram бот умеет:

* Команды
   * `/stats` - дает обобщенную статистику о памяти \ диске \ процессах.
   * `/shell` - позволяет использовать бот в режиме Shell.
   * `/memgraph` - строит график использования памяти за прошедший период и отправляет вам изображение графика.
   * `/setmem` - возможность установить порог оперативной памяти (%) для мониторинга.
   * `/setpoll` - интервал опроса в секундах (выше 10).
* Отслеживает использование памяти и, **если** она **превышает** установленное пороговое значение =, **отправляет вам предупреждение**.

------------



**Как это работает**: [Gif](https://i.13.wf/2019/08/17/1566074720-2541.gif)

![Bot](https://i.13.wf/2019/08/17/1566074746-9489.png)

**Пример вывода команды shell от бота:**

![Shell](https://i.imgur.com/PtvcaSD.png)

**Пример графика**: [Gif](http://i.imgur.com/anX7rJR.gifv)

![Graph](http://i.imgur.com/K8mG3aM.jpg?1)

------------



# Использование

## Требования

* Python 3+
* [Telepot](https://github.com/nickoala/telepot)
* [Psutil](https://github.com/giampaolo/psutil)
    * Не забудьте установить его для Python 3+.
    * Чтобы убедиться, что `pip`устанавливает пакеты для версии 3+:
        * `curl -O https://bootstrap.pypa.io/get-pip.py`
        * `sudo python3 get-pip.py`
        * После этого установите `pip install psutil`
        * Also Stackoverflow question about that [here](http://stackoverflow.com/questions/11268501/how-to-use-pip-with-python-3-x-alongside-python-2-x)
* [matplotlib](http://matplotlib.org/)
    * `sudo apt-get install python3-matplotlib`
* Токен бота & `tokens.py`
    * Hide all the keys and admin variables in `tokens.py`. Use it only for sensitive variables. Avoid creating functions not to clutter the namespaces through the import.
    * Get a key from the [Bot Father](https://telegram.me/BotFather)
    * Clone that repo
    * In the folder with the cloned repo create a file `tokens.py`
       * It's added to the `.gitignore` so you don't commit your own (and I don't commit mine:)
    * In that file put a string variable `telegrambot` which equals your key
       * For example: `telegrambot = "000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"`


------------


## Запуск

Выполните: `python3 servstatsbot.py`

------------

## Запуск в режиме "daemon"

* Смотрите файл который включен в этот репозиторий: `servstatsbot.conf`
    * Откройте его и отредактируйте путь, как указано в комментариях к нему.
* Поместите файл в папку `/etc/init/`
* Запустите как "daemon" с: `start servstatsbot`
    * Используйте start|stop|restart
    * Если произойдет сбой ботов, он будет автоматически перезапущен.
    * Он также заработает после перезагрузки.

## Настройка администратора

You have to set a variable `adminchatid` in `tokens.py` to be equal your chat_id or multiple chat_id (if more people will use your bot).
For example:

* `adminchatid = [443355]`
* `adminchatid = [443355, 55667788, 99884433]`

I will reimplement this differently later.


# Развите проекта :)
 Я собрал этот код в течение 10 минут, чтобы он служил макетом для дальнейшей работы.
Но я думаю, что это хорошая идея, и некоторым из вас это тоже может понравится, и пригодится.

------------


------------


# Разработчики бота

### Alfred -- разрботчик
[http://alfredthebot.com](http://alfredthebot.com)
### vladios13 -- локализация и доработка 🌚
[Blog vladios13](http://blog.vladios13.com)
