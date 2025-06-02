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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
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

def admin_resultsview(driver):
    try:
        print("測試：管理者環境-問卷管理-結果檢視")
        time.sleep(2)
        menu_expanded(driver, "問卷管理", "結果檢視")
        time.sleep(2)
        if "檢視" in driver.page_source:
            print("\033[32m進入結果檢視成功\033[0m")
        else:
            print("\033[31m進入結果檢視失敗\033[0m")

        # 檢視
        driver.execute_script("view_result(100000002)")
        time.sleep(2)
        if "詳細資料" and "總問卷數" in driver.page_source:
            print("\033[32m進入檢視成功\033[0m")
        else:
            print("\033[31m進入檢視失敗\033[0m")

        initial_files = get_downloaded_files(download_directory)
        driver.execute_script("displayDialog('exportTable')") #列印
        time.sleep(2)
        driver.execute_script("exportDone()")
        time.sleep(10)
        final_files = get_downloaded_files(download_directory)
        if len(final_files) > len(initial_files):
            print("\033[32m統計表下載成功\033[0m")
        else:
            print("\033[31m統計表下載失敗\033[0m")
        
        # 詳細資料
        driver.execute_script("ShowDetailResult()")
        time.sleep(2)
        if "統計資料" and "總問卷數" in driver.page_source:
            print("\033[32m進入詳細資料成功\033[0m")
        else:
            print("\033[31m進入詳細資料失敗\033[0m")

        driver.execute_script("displayDialog('exportTable')") #列印
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="csv"]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="htm"]'))
        ).click()

        initial_files = get_downloaded_files(download_directory)
        driver.execute_script("displayDialog('exportTable')") #列印
        driver.execute_script("exportDone()")
        time.sleep(10)
        final_files = get_downloaded_files(download_directory)
        if len(final_files) > len(initial_files):
            print("\033[32m詳細資料下載成功\033[0m")
        else:
            print("\033[31m詳細資料下載失敗\033[0m")

        # 統計資料
        driver.execute_script("document.ResultForm.submit()")
        time.sleep(2)
        if "詳細資料" and "總問卷數" in driver.page_source:
            print("\033[32m進入統計資料成功\033[0m")
        else:
            print("\033[31m進入統計資料失敗\033[0m")

        driver.execute_script("displayDialog('exportTable')") #列印
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="csv"]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="xml"]'))
        ).click()

        initial_files = get_downloaded_files(download_directory)
        driver.execute_script("displayDialog('exportTable')") #列印
        driver.execute_script("exportDone()")
        time.sleep(10)
        final_files = get_downloaded_files(download_directory)
        time.sleep(2)
        if len(final_files) > len(initial_files):
            print("\033[32m統計資料下載成功\033[0m")
        else:
            print("\033[31m統計資料下載失敗\033[0m")

        # 回列表
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="回列表"]'))
        ).click()
        time.sleep(2)
        if "檢視" in driver.page_source:
            print("\033[32m回列表成功\033[0m")
        else:
            print("\033[31m回列表失敗\033[0m")

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