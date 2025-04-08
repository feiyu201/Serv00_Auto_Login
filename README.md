# Serv00 - 控制面板自动登录、ssh自动连接脚本


## 使用方法
　　在 GitHub 仓库中，进入右上角`Settings`，在侧边栏找到`Secrets and variables`，点击展开选择`Actions`，点击`New repository secret`，然后创建一个名为`ACCOUNTS_JSON`的`Secret`，将 JSON 格式的账号密码字符串作为它的值。在bark中填入bark软件的推送apiKey，可留空。在host填入ssh的连接地址。如下格式：  
```
[  
{ "username": "qinshihuang", "password": "linux.do", "panelnum": "0", "host": "s3.serv00.com", "TGTOKEN": "your_telegram_bot_token", "chatid": "your_chat_id" },
{ "username": "zhaogao", "password": "daqinzhonggong", "panelnum": "2", "host": "s3.serv00.com", "TGTOKEN": "your_telegram_bot_token", "chatid": "your_chat_id" },
{ "username": "heiheihei", "password": "shaibopengke", "panelnum": "3",  "host": "s3.serv00.com", "TGTOKEN": "your_telegram_bot_token", "chatid": "your_chat_id" }
]
```
> 其中`panelnum`参数为面板编号，即为你所收到注册邮件的`panel*.serv00.com`中的`*`数值。
> 其中`TGTOKEN`参数为Telegram.的机器人token,`chatid`参数为需要通知人的ID(可留空)



