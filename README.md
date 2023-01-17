<div align=center><img width="320" height="320" src="https://s2.loli.net/2023/01/16/7b4TJpn1tYP8sej.png"/></div>

<div align=center>

<p><strong>一款为芳文党服务的胡桃同学！</strong></p>

`<img src="https://img.shields.io/badge/OneBot-11-black?style=for-the-badge"></img>` `<img src="https://img.shields.io/github/license/misaka10843/AoBot?style=for-the-badge"></img>` `<img src="https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge"></img>`

</div>

# 🤖AoBot

此项目基于 Nonebot2 和 go-cqhttp 开发，一款有一些插件的QQ群娱乐机器人

（此项目定位为个人Bot，可能不会进行长期维护！）

## 💭About

用爱发电，某些功能学习借鉴了大佬们的代码，并且引用了一些插件后进行个性化的修改，因为本人为胡桃同学力推人因此开发了Aobot，实现了一些对群友的娱乐功能/实用功能/芳文社相关功能（大概）。

## 🔨功能图

![qwq](./Road.png)

## 📣声明

此项目仅用于学习交流，请勿用于非法用途

此项目均为开源代码，在正常情况下除非引用代码的仓库另有许可证，所有代码均使用[**GPL v3**](https://choosealicense.com/licenses/gpl-3.0/)

## 💡简单部署

### 1.配置gocq

在 [go-cqhttp仓库](https://github.com/Mrs4s/go-cqhttp) 下载Releases最新版本，运行后选择反向WS，然后打开go-cqhttp生成的 `config.yml`在对应地方填写 `ws://127.0.0.1:8531/onebot/v11/ws`

比如go-cqhttp生成的 `config.yml`中对应的地方填写应该这样

```yml
  - ws-reverse:
      # 反向WS Universal 地址
      # 注意 设置了此项地址后下面两项将会被忽略
      universal: ws://127.0.0.1:8531/onebot/v11/ws #这里需要更改！
      # 反向WS API 地址
      api: ws://your_websocket_api.server
      # 反向WS Event 地址
      event: ws://your_websocket_event.server
      # 重连间隔 单位毫秒
      reconnect-interval: 3000
      middlewares:
        <<: *default # 引用默认中间件
```

### 2.配置AoBot

首先先获取本仓库文档，您可以下载[zip](https://github.com/misaka10843/AoBot/archive/refs/heads/main.zip)或者 `git clone https://github.com/misaka10843/AoBot.git`

如果您是下载的 `zip`，请解压后 `cd AoBot-main`

如果您是 `git clone`，请允许 `cd AoBot`

然后新建 `.env`文件，将 `.env.dev`的内容复制到 `.env`后按照对应的注解进行配置

请注意，默认情况下，请不要修改以下的内容，如需修改，请连同修改go-cqhttp的 `config.yml`中的反向WS地址

```.env
################
#ws配置
################

HOST=127.0.0.1
PORT=8531
```

### 3.启动对应端

首先，我们启动**go-cqhttp**

切换到go-cqhttp的文件夹，输入 `./go-cqhttp`，然后将进程挂起即可

(Linux可以使用 `Screen`来进行挂起)

然后，我们启动**AoBot**

**请注意，在进行接下来的过程前，请注意您的python必须大于等于3.8**

强烈建议您使用[虚拟环境](https://docs.python.org/zh-cn/3/library/venv.html)安装依赖和运行，不会创建虚拟环境可以去看 [virtualenv 文档](https://virtualenv.pypa.io/en/latest/index.html)，看不懂英语的可以去看[廖雪峰教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480)

首先，切换到AoBot文件夹，然后输入 `pip install -r ./requirements.txt`来安装依赖

然后输入 `python bot.py`来启动Bot后，挂起进程即可

## 🔗引用插件

- [bilibili视频、番剧解析](https://github.com/mengshouer/nonebot_plugin_analysis_bilibili)
- [HarukaBot(bili动态)](https://github.com/SK-415/HarukaBot)
- [HikariSearch](https://github.com/MeetWq/nonebot-plugin-hikarisearch)
- [无数据库的问答插件](https://github.com/kexue-z/nonebot-plugin-word-bank2)
- [nonebot-twitter(并未测试)](https://github.com/SlieFamily/nonebot-twitter)
- [ELF_RSS(Twitter及其他RSS源的转发动态)](https://github.com/Quan666/ELF_RSS)

其他未列出的插件因为并未做出修改，所以您可以直接在 `plugins.json`中查看

## ❓常见问题

### Q1：在Windows中停止机器人会报错

```python
01-17 12:57:10 [ERROR] apscheduler | Job "dy_sched (trigger: date[2023-01-17 12:57:09 CST], next run at: 2023-01-17 12:57:09 CST)" raised an exception
Traceback (most recent call last):
  File "bot.py", line 19, in <module>
    nonebot.run()
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\nonebot\__init__.py", line 273, in run
    get_driver().run(*args, **kwargs)
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\nonebot\drivers\fastapi.py", line 172, in run
    uvicorn.run(
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\uvicorn\main.py", line 569, in run
    server.run()
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\uvicorn\server.py", line 60, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "d:\pl\python\python38\lib\asyncio\runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "d:\pl\python\python38\lib\asyncio\base_events.py", line 603, in run_until_complete
    self.run_forever()
  File "d:\pl\python\python38\lib\asyncio\windows_events.py", line 316, in run_forever
    super().run_forever()
  File "d:\pl\python\python38\lib\asyncio\base_events.py", line 570, in run_forever
    self._run_once()
  File "d:\pl\python\python38\lib\asyncio\base_events.py", line 1859, in _run_once
    handle._run()
  File "d:\pl\python\python38\lib\asyncio\events.py", line 81, in _run
    self._context.run(self._callback, *self._args)
> File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\apscheduler\executors\base_py3.py", line 30, in run_coroutine_job
    retval = await job.func(*job.args, **job.kwargs)
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\haruka_bot\plugins\pusher\dynamic_pusher.py", line 38, in dy_sched
    await grpc_get_user_dynamics(
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\bilireq\grpc\utils\__init__.py", line 48, in
 wrapper
    result = await func(
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\bilireq\grpc\dynamic\__init__.py", line 20, in grpc_get_user_dynamics
    return await stub.DynSpace(req, **kwargs)
  File "D:\Users\misaka10843\Documents\GitHub\AoBot\.venv\lib\site-packages\grpc\aio\_call.py", line 271, in __await__
    response = yield from self._call_response
asyncio.exceptions.CancelledError
01-17 12:57:10 [INFO] uvicorn | Application shutdown complete.
01-17 12:57:10 [INFO] uvicorn | Finished server process [1016]
```

如果是上面这种报错，均为正常情况，详细可以查看[NoneBot文档](https://v2.nonebot.dev/docs/tutorial/choose-driver#fastapi%E9%BB%98%E8%AE%A4)
