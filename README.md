# PocketExportToMarkdownWithSimpreadAtChrome

批量通过[Simpread简阅](http://ksria.com/simpread/)和[Quicker](https://getquicker.net/)导出为markdown文件.

## 使用的工具

- Simpread插件
- Quicker

## 如何使用

安装配置简阅和Quicker

安装这个Quicker的动作分享: [批量简阅导出](https://getquicker.net/Sharedaction?code=f3d75558-8e82-4c0a-d277-08db96d5b7be)

通过复制一串网址, Quicker会完成批量调用Simpread插件, 将网页保存为markdown文件的操作.

第一次运行需要你指定存储日志的位置.

## 注意事项

确认后请不要操作鼠标或键盘, 直到Quicker弹出提示框, 展示错误日志.

接收到的网址会存储在`完成的网址.txt`中, 保存的markdown文件会存储在简阅设置的相应文件夹中.

如果网址有变化, 比如知乎如果内容被删改, 则会跳转到知乎首页, 导致实际打开网页和输入的网页不一致.

那么Quicker会不执行操作, 而是将原网址和实际打开网址都记录到`error.txt`中, 然后关闭错误的网页.

## 一些记录

在初版的时候, 我通过向ChatGPT说明我的需求, 计划是通过python脚本, 读取导出的网页列表, 逐个打开网页, 然后调用Simpread插件, 将网页保存为markdown文件.

但是我写了一会儿开始测试时想起来Selenium是不支持持久化存储用户设置的(比较麻烦), 所以我改为直接通过Quicker在本地执行...

Pocket的离线存档是私有格式, 基于云且不提供导出功能, 所以我通过[导出](https://help.getpocket.com/article/1015-exporting-your-pocket-list)网页列表的方式, 将网页导出到本地进行存档.
