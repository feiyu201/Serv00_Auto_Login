import os
import json
import paramiko
import requests

# 从环境变量中读取 ACCOUNTS_JSON
accounts_json = os.getenv('ACCOUNTS')
accounts = json.loads(accounts_json)

# 尝试通过SSH连接的函数
def ssh_connect(host, username, password, TGTOKEN, chatid):
    transport = None
    try:
        transport = paramiko.Transport((host, 22))
        transport.connect(username=username, password=password)
        ssh_status = "serv00SSH连接成功"
        print(f"serv00SSH连接成功。")

        # 使用 Telegram 发送连接成功消息
        if TGTOKEN and chatid:
            url = f"https://api.telegram.org/bot{TGTOKEN}/sendMessage"
            payload = {
                'chat_id': chatid,
                'text': f"serv00账号 {username} SSH连接成功。"
            }
            requests.post(url, data=payload)
    except Exception as e:
        ssh_status = f"serv00SSH连接失败，错误信息: {e}"
        print(f"serv00SSH连接失败: {e}")

        # 使用 Telegram 发送连接失败消息
        if TGTOKEN and chatid:
            url = f"https://api.telegram.org/bot{TGTOKEN}/sendMessage"
            payload = {
                'chat_id': chatid,
                'text': f"serv00账号 {username} SSH连接失败，请检查账号和密码是否正确。"
            }
            requests.post(url, data=payload)
    finally:
        if transport is not None:
            transport.close()

# 循环执行任务
for account in accounts:
    ssh_connect(account['host'], account['username'], account['password'], account.get("TGTOKEN"), account.get("chatid"))
