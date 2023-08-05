# PocketExportToMarkdownWithSimpreadAtChrome

这是一个使用Python和Selenium编写的脚本，用于自动化处理一系列网页操作。它可以按顺序打开一串网址，检查网页是否正确加载，然后模拟键盘操作以调用Chrome插件。如果网页没有正确加载，脚本会关闭网页，并将网址存储到错误日志中。每完成20次操作后，脚本会暂停。脚本支持同时打开多个网页，并可以预设延迟以确保网页和插件正常工作。

## 技术栈

- Python
- Selenium
- ChromeDriver

## 如何使用

1. 安装Python和Selenium。
2. 下载并设置ChromeDriver。
3. 运行脚本，按照提示输入网址。
4. 脚本会自动进行操作，每完成20次操作后暂停。
5. 如果遇到错误，脚本会将错误网址记录到日志中。

## 注意事项

- 请确保您的网速足够快，以便网页能够在预设的延迟时间内完全加载。
- 请确保您的Chrome插件可以通过键盘操作调用。
# PocketExportToMarkdownWithSimpreadAtChrome
