# PocketExportToMarkdownWithSimpreadAtChrome

简单记录下我如何将[pocket导出](https://help.getpocket.com/article/1015-exporting-your-pocket-list)的网页列表,
批量通过[Simpread简阅](http://ksria.com/simpread/)和[Quicker](https://getquicker.net/)导出为markdown文件的过程.

## 使用的工具

- Simpread插件
- Quicker

## 一些记录

因为pocket的离线存档是私有格式, 基于云的不提供导出功能, 所以我只能通过导出网页列表的方式, 将网页导出到本地.
在初版的时候, 我通过向ChatGPT说明我的需求, 计划是通过python脚本, 读取导出的网页列表, 逐个打开网页, 然后调用Simpread插件, 将网页保存为markdown文件.
但是我完成后才了解到, Selenium是不支持持久化存储用户设置的(比较麻烦), 所以我改为直接通过Quicker在本地执行...

这个是Quicker的动作分享

[Link](https://getquicker.net)
通过简单地复制一串网址, Quicker会完成批量调用Simpread插件, 将网页保存为markdown文件的操作.

- (TODO) 第一次运行需要你指定存储日志的位置.
- 接收到的网址会存储在`url.txt`中, 保存的markdown文件会存储在简阅设置的相应文件夹中.
- 如果网址有变化, 比如知乎如果内容被擅长, 会redirect到知乎首页, 那么Quicker会将原网址和实际打开网址都记录到`error.txt`中.
