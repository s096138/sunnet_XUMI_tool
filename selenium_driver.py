from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

load_dotenv()

driver = None
def initialize_driver(download_dir=None, url=None):
    global driver
    if driver is None:
        # 從 .env 讀取 BASE_URL
        base_url = os.getenv("BASE_URL")
        if not base_url:
            raise ValueError("BASE_URL未定義")

        # 初始化 WebDriver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)  # 不自動關閉瀏覽器
        options.add_argument('--start-maximized')  # 瀏覽器放大
        # options.add_argument('--proxy-server=http://127.0.0.1:8080') # Burp Suite

        # # iPhone
        # options.add_argument("--window-size=375,812")  
        # options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1")
        # # Android
        # options.add_argument("--window-size=360,640")
        # options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36")
        
        # 使用 webdriver_manager 自動管理 ChromeDriver
        driver = webdriver.Chrome(
            service=webdriver.ChromeService(ChromeDriverManager().install()),
            options=options
        )

        if download_dir:
            prefs = {'download.default_directory': download_dir}
            options.add_experimental_option('prefs', prefs)

        driver.get(base_url)
        print(f"\033[34m測試站台：{os.getenv('BASE_URL')}\033[0m")

    return driver