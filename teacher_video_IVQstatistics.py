from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
from selenium_driver import initialize_driver
from selenium import webdriver
import time
import os

download_directory = "c:\\Users\\SGQA2\\Downloads"
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False,  # 允許不安全下載

}
options.add_experimental_option("prefs", prefs)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--disable-blink-features=AutomationControlled')

def get_downloaded_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def teacher_video_IVQstatistics(driver):
    try:   
        print("測試：辦公室-課程管理-全能影像轉譯(IVQ統計)")
        menu_expanded(driver, "課程管理", "全能影像轉譯")
        time.sleep(2)
        if "讓備課更輕鬆" in driver.page_source:
            print("\033[31m影片列表沒有影片可供測試\033[0m")
            return
        else:
            pass

        # IVQ統計
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@id='go#202410旭航v4.mp4']"))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'IVQ統計')])[1]"))
        ).click()
        time.sleep(2)
        if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "itemsCountStat"))
        ).text != "0":
            print("\033[32m進入全能影像轉譯(IVQ統計)成功\033[0m")
            pass
        else:
            print("\033[31m沒有題目無法統計\033[0m")
            return

        # 匯出統計資料
        time.sleep(2)
        initial_files = get_downloaded_files(download_directory)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'匯出統計結果')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='exportBtn']"))
        ).click()
        time.sleep(5)
        final_files = get_downloaded_files(download_directory)
        if len(final_files) > len(initial_files):
            print("\033[32m匯出統計結果成功\033[0m")
        else:
            print("\033[31m匯出統計結果失敗\033[0m")

        # IVQ數量
        time.sleep(2)
        statistics = driver.find_element(By.ID, "itemsCountStat").text
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='bank-tab']"))
        ).click()
        time.sleep(2)
        quenestions = driver.find_element(By.ID, "itemsCount").text
        time.sleep(2)
        if int(statistics) == int(quenestions):
            print("\033[32mIVQ題目與統計數量一致\033[0m")
        else:
            print("\033[31mIVQ題目與統計數量不一致\033[0m")

    except TimeoutException as e:
        print(f"等待元素可點擊超時: {e}")
        return
    except NoSuchElementException as e:
        print(f"未找到元素: {e}")
        return
    except ElementClickInterceptedException as e:
        print(f"無法點擊該元素: {e}")
        return
    except StaleElementReferenceException as e:
        print(f"元素已不再可用: {e}")
        return
    except ElementNotInteractableException as e:
        print(f"元素不可互動: {e}")
        return
    except WebDriverException as e:
        print(f"WebDriver 錯誤: {e}")
        return
    except Exception as e:
        print(f"發生未預期的錯誤: {e}")
        return 