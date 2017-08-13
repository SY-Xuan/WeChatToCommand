# WeChatToCommand

## 通过微信远程控制电脑
+ ###使用方法###
1. 在目标机通过 `python chatToCommand.py` 运行该程序
2. 加入了权限设置，扫描二维码登录后，需要发送-authority指令获取NameId
3. 在authority.py中的 `permissionUserName`列表中加入指定NameId
4. 重新运行*chatToCommand*即可

+ ###实现功能###
1. 可以完成大部分的命令行操作(没测试所有命令行),返回信息通过消息的形式返回
2. 可以使用`-download`命令加上文件路径下载文件(会将指定的文件以消息的形式返回)
3. 向目标微信发送文件后，会自动将文件下载到运行该程序机器的当前工作目录