


<div align=center><img width="320" height="320" src="https://s2.loli.net/2023/01/16/7b4TJpn1tYP8sej.png"/></div>


<div align=center><p>一款为芳文党服务的胡桃同学！</p></div>

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

在 [go-cqhttp仓库](https://github.com/Mrs4s/go-cqhttp) 下载Releases最新版本，运行后选择反向WS/正向WS，然后打开go-cqhttp生成的`config.yml`在对应地方填写`0.0.0.0:6700`

例如选择正向WS，go-cqhttp生成的`config.yml`中对应的地方填写应该这样

```yml
  # 正向WS设置
  - ws:
      # 正向WS服务器监听地址
      address: 0.0.0.0:6700
      middlewares:
        <<: *default # 引用默认中间件
```

### 2.配置AoBot

首先先获取本仓库文档，您可以下载[zip](https://github.com/misaka10843/AoBot/archive/refs/heads/main.zip)或者`git clone https://github.com/misaka10843/AoBot.git`

如果您是下载的`zip`，请解压后`cd AoBot-main`

如果您是`git clone`，请允许`cd AoBot`

然后打开`.env`，配置以下内容

```.env

SUPERUSERS = ["机器人管理员qq"] #超级管理员

# bilibili URL解析插件设置
analysis_whitelist = [qq号,qq号] # 不解析里面填写的QQ号发的链接 List[int]
analysis_group_whitelist = [群号,群号] # 不解析里面填写的QQ群号发的链接 List[int]

```
