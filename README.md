# Server Manager Bot

原项目详见fork源，您正在看的这个repo某种意义上属于二开版，Working in progress之后是原readme的完整
翻译，也可以当做部署教程，实际上，这个repo只是比原repo多几个功能+汉化而已。

2020-3-31新增

输入/start或/help或help时回复所有可用的命令。

Known Issue
* 机器人新上线一段时间内绘制图标x轴为负数，过一段时间后恢复正常。
* 设置新阈值或探测间隔，收到新消息后不会自动stop。

Working in Progress
* 开机以来所用流量功能
* 当前网速
* 磁盘使用详细情况
* 重启/掉进程后上线提示

欢迎与我或原作者（找不到人了）发邮件探讨/提issue！

功能：
* 命令
    * `/stats` - 检查磁盘/CPU/内存使用情况（正在完善中）
    * `/shell` - 进入执行命令模式并返回结果
    * `/memgraph` - 绘制近一段时间的内存使用记录表
    * `/setmem` - 设置内存占用告警阈值,并在占用情况高于这个值时告警
    * `/setpoll` - 设置探测间隔（不少于10秒）
* 检测内存使用情况并且在高于设定阈值时通过telegram发送告警消息


`/stats`命令演示: [Gif](http://i.imgur.com/AhCvy9W.gifv)

![Bot](http://i.imgur.com/hXT0drx.png)


`/shell`命令演示: 

![Shell](https://i.imgur.com/PtvcaSD.png)


`/memgraph`命令演示: [Gif](http://i.imgur.com/anX7rJR.gifv)

![Graph](http://i.imgur.com/K8mG3aM.jpg?1)

# 使用方法

## 所需环境

* Python 3+
* [Telepot](https://github.com/nickoala/telepot)
* [Psutil](https://github.com/giampaolo/psutil)
    * 确保Psutil是为Python3工作,而非2
    * 确保`pip`是最新版本:
        * `curl -O https://bootstrap.pypa.io/get-pip.py`
        * `sudo python3 get-pip.py`
        * 之后使用`pip install psutil`
        * 在Stackoverflow上也有相关问题的回答[链接](http://stackoverflow.com/questions/11268501/how-to-use-pip-with-python-3-x-alongside-python-2-x)
* [matplotlib](http://matplotlib.org/)
    * `sudo apt-get install python3-matplotlib`
* Bot key & `tokens.py`
    * 把token放在`tokens.py`里. `tokens.py`只用来保存您的chat_id和bot token.不要随便定义/更改函数名.
    * 从@Bot Father新建机器人/获取token[Bot Father](https://telegram.me/BotFather)
    * 克隆该仓库
    * 在本地文件夹内新建文件`tokens.py`
       * 已经加入`.gitignore`豪华套餐,所以谁的key/token都不会提交上来
    * 将`telegrambot`后字符串换成自己的token
       * 如: `telegrambot = "000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    * 编者按：原readme中的确是这样写的，但作者更新的时候可能忘了改了，这里直接vim编辑tokens.py_example再mv重命名去掉_example就可以了。
     
## 开始运行

`python3 servstatsbot.py`

## 将bot作为进程运行

* 参见文件: `servstatsbot.conf`
    * 根据文件内注释指示更改路径
* 将`servstatsbot.conf`放在`/etc/init/`内
* 用该命令启动进程: `start servstatsbot`
    * 之后,以下命令将可用：`service servstatsbot start|stop|restart`
    * 如果进程崩溃将会自动重启
    * 开机启动

## 设定一个管理员

在`tokens.py`中设定`adminchatid`变量为chat_id(如果您的工具人是个公交车,参照如下方法).
* `adminchatid = [443355]`
* `adminchatid = [443355, 55667788, 99884433]`

之后我将会重新编写这块的代码

译者按：这句话是原作者写的,我没说过        
 
# 欢迎一键三连 XD
 我在十分钟之内拼凑出这个代码,之后又花了一点时间使之成.我觉得这个bot是个很好的想法,并且阅读这段话当中的某些人会非常喜欢他.所以请随便fork,pull,提交新功能!
 可以给你contributors access哦!笔芯
 真心希望看到这个项目能够快速发展起来:)
译者按：这些话也是作者说的,可是他已经4年没有更新了,会不会...

 
 
# 其他的bot项目
 
## Alfred
[http://alfredthebot.com](http://alfredthebot.com)

译者按：已404
 
 
 GB
