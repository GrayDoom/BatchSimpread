from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading
import logging

# 设置日志配置
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


# 设置ChromeDriver路径，并创建一个浏览器实例
driver_path = "chromedriver.exe"  # 使用文件名作为路径
driver = webdriver.Chrome(driver_path)


def read_urls():
    with open('todo.txt', 'r') as file:
        urls = file.readlines()
    return urls


def open_webpage(url):
    try:
        driver.get(url)
        time.sleep(5)  # 等待5秒，让网页完全加载
        logging.info(f"Webpage {url} opened successfully")
    except Exception as e:
        logging.error(f"Error opening webpage {url}: {e}")
        handle_error(url)


def check_page_loaded(url):
    return driver.current_url == url


def perform_keyboard_action():
    action = ActionChains(driver)
    action.send_keys('a').pause(0.1).send_keys('a')  # 模拟快速按下两次'a'键
    time.sleep(10)  # 等待10秒，让插件有足够的时间响应
    action.send_keys('a').pause(0.1).send_keys('t')  # 模拟快速按下'a'键和't'键
    action.perform()



def handle_error(url):
    driver.close()  # 关闭当前网页
    with open('error.txt', 'a') as file:  # 以追加模式打开error.txt文件
        file.write(url + '\n')  # 将网址写入文件


def process_urls(urls):
    for i, url in enumerate(urls):
        open_webpage(url)  # 打开网页
        if check_page_loaded(url):  # 检查网页是否正确加载
            perform_keyboard_action()  # 模拟键盘操作
        else:
            handle_error(url)  # 处理错误
        if (i + 1) % 20 == 0:  # 每完成20次操作后，脚本暂停
            print('已完成20次操作，脚本暂停。')
            break

def main():
    urls = read_urls()  # 读取网址
    num_threads = 5  # 设置线程数量
    urls_per_thread = len(urls) // num_threads  # 计算每个线程需要处理的网址数量
    threads = []  # 创建一个线程列表

    # 创建线程
    for i in range(num_threads):
        start = i * urls_per_thread
        end = (i + 1) * urls_per_thread if i != num_threads - 1 else None
        thread = threading.Thread(target=process_urls, args=(urls[start:end],))
        threads.append(thread)

    # 启动线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
