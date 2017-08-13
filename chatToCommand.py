import authority
import itchat
import os
#因为popen实现机制问题无法使用cd命令

#使用-download 文件名 命令来下载指定文件
@itchat.msg_register([itchat.content.TEXT])#注册文本消息回复
def text_reply(msg):
    if msg['Text'] == '-authority':
        itchat.send(msg["FromUserName"], msg['FromUserName'])
    elif msg["FromUserName"] in authority.permissionUserName:
        print('permit')
        if msg['Text'].split(" ")[0] == '-download':#下载文件指令
            itchat.send_file(msg['Text'].split(' ')[1], msg['FromUserName'])
        elif msg['Text'].split(" ")[0] == 'cd':#拦截cd命令通过os.chdir来实现目录切换
            os.chdir(msg['Text'].split(' ')[1])
        else:
            with os.popen(msg['Text']) as cmd:#普通指令
                itchat.send(cmd.read(), msg["FromUserName"])

@itchat.msg_register([itchat.content.ATTACHMENT, itchat.content.PICTURE, itchat.content.RECORDING, itchat.content.VIDEO])
def download_files(msg):#接收到文件图片语音视频时将其存到本地
    if msg['FromUserName'] in authority.permissionUserName:
        print(msg["Text"])
        with open(msg["FileName"], 'wb') as f:
            f.write(msg["Text"]())



itchat.auto_login(True)
itchat.run()

