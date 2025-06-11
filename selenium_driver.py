from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from dotenv import load_dotenv
import os
import time

load_dotenv()

# 全局變數用於存儲 driver 實例
_driver = None

def get_driver():
    """獲取 WebDriver 實例，如果不存在則創建一個新的"""
    global _driver
    
    # 檢查現有 driver 是否有效
    if _driver is not None:
        try:
            # 檢查 session 是否仍然有效
            _driver.current_url  # 嘗試訪問一個屬性來檢查 session 是否有效
            return _driver
        except WebDriverException:
            # 如果 session 無效，則關閉並重置 driver
            if _driver is not None:
                try:
                    _driver.quit()
                except:
                    pass
                _driver = None
    
    # 創建新的 WebDriver 實例
    return _create_new_driver()

def _create_new_driver(download_dir=None, url=None):
    """創建一個新的 WebDriver 實例"""
    global _driver
    
    try:
        # 從 .env 讀取 BASE_URL
        base_url = url if url else os.getenv("BASE_URL")
        if not base_url:
            raise ValueError("BASE_URL 未定義")

        # 初始化 WebDriver 選項
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)  # 不自動關閉瀏覽器
        options.add_argument('--start-maximized')  # 瀏覽器放大
        options.add_argument('--no-sandbox')  # 解決某些系統權限問題
        options.add_argument('--disable-dev-shm-usage')  # 解決資源限制問題
        options.add_argument('--disable-blink-features=AutomationControlled')  # 避免被檢測為自動化測試
        
        # 設置下載目錄（如果提供）
        if download_dir:
            os.makedirs(download_dir, exist_ok=True)
            prefs = {
                'download.default_directory': download_dir,
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True
            }
            options.add_experimental_option('prefs', prefs)

        # 使用 webdriver_manager 自動管理 ChromeDriver
        _driver = webdriver.Chrome(
            service=webdriver.ChromeService(ChromeDriverManager().install()),
            options=options
        )
        
        # 設置頁面加載超時和腳本超時
        _driver.set_page_load_timeout(30)
        _driver.set_script_timeout(30)
        
        # 訪問目標 URL
        _driver.get(base_url)
        print(f"\033[34m測試站台：{base_url}\033[0m")
        
        # 等待頁面加載
        time.sleep(2)
        
        return _driver
        
    except Exception as e:
        # 如果發生異常，確保清理 driver
        if _driver is not None:
            try:
                _driver.quit()
            except:
                pass
            _driver = None
        raise RuntimeError(f"創建 WebDriver 失敗: {str(e)}")

def close_driver():
    """關閉當前的 WebDriver 實例"""
    global _driver
    if _driver is not None:
        try:
            _driver.quit()
        except:
            pass
        _driver = None

def initialize_driver(download_dir=None, url=None):
    """初始化 WebDriver（為了向後兼容）"""
    return get_driver()