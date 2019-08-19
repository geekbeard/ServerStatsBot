# Server Manager Bot

Этот Telegram бот умеет:

* Команды
   * `/stats` - дает обобщенную статистику о памяти \ диске \ процессах, а также общую нагрузку за определнный период времени.
   * `/shell` - позволяет использовать бот в режиме Shell.
   * `/memgraph` - строит график использования памяти за прошедший период и отправляет вам изображение графика.
   * `/setmem` - возможность установить порог оперативной памяти (%) для мониторинга.
   * `/setpoll` - интервал опроса в секундах (выше 10).
* Отслеживает использование памяти и, **если** она **превышает** установленное пороговое значение то **отправляет вам предупреждение**.

------------


**Как это работает**: [Смотреть GIF](https://i.13.wf/2019/08/17/1566074720-2541.gif)

![Вывод изображения ](https://i.13.wf/2019/08/17/1566074746-9489.png)

**Пример вывода команды shell от бота:**

![Shell](https://i.imgur.com/PtvcaSD.png)

**Пример графика**: [Gif](http://i.imgur.com/anX7rJR.gifv)

![Пример графика](http://i.imgur.com/K8mG3aM.jpg?1)

------------


# Установка

## Требования к системе:

* Python 3+
* [Telepot](https://github.com/nickoala/telepot)
* [Psutil](https://github.com/giampaolo/psutil)
    * Не забудьте установить его для Python 3+.
    * Чтобы убедиться, что `pip` устанавливает пакеты для версии 3+:
        * `curl -O https://bootstrap.pypa.io/get-pip.py`
        * `sudo python3 get-pip.py`
        * После этого установите: `pip install psutil`
        * Also Stackoverflow question about that [here](http://stackoverflow.com/questions/11268501/how-to-use-pip-with-python-3-x-alongside-python-2-x)
* [matplotlib](http://matplotlib.org/)
    * `sudo apt-get install python3-matplotlib`
* Токен бота & `tokens.py`
    * Все ключи и токены сохраняйте в `tokens.py`.
    * Получить токен для бота можно в  [Bot Father](https://telegram.me/BotFather)
    * Клонировать репозиторий командой: `https://github.com/vladios13/ServerStatsBot.git`
    * В папке с клонированным репозиторием создайте файл `tokens.py`
       * В этот файл поместите строковую переменную `telegrambot` токен вашего бота.
       * *Пример*: `telegrambot = "000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"`


------------


## Запуск

Выполните: `python3 servstatsbot.py`

------------

## Запуск в режиме "daemon"

* Вся нужная информация находится в: `servstatsbot.conf`
    * Откройте его и отредактируйте путь, как указано в комментариях к нему.
* Поместите файл в папку `/etc/init/`
* Запустите как "daemon" с: `start servstatsbot`
    * Используйте `start|stop|restart`
    * Если произойдет сбой, он будет автоматически перезапущен.
    * Он также заработает после перезагрузки.

## Настройка администратора

Вы должны установить переменную. `adminchatid` в `tokens.py`. Вы так же можете указать несколько пользователей.

**Пример**:

* `adminchatid = [443355]`
* `adminchatid = [443355, 55667788, 99884433]`

# Развите проекта :)
 Я собрал этот код в течение 10 минут, чтобы он служил макетом для дальнейшей работы.
Но я думаю, что это хорошая идея, и некоторым из вас это тоже может понравится, и пригодится.

------------

# Разработчики бота

### Alfred - разрботчик
[http://alfredthebot.com](http://alfredthebot.com)
### vladios13 - локализация и доработка 🌚
[Blog vladios13](http://blog.vladios13.com)
