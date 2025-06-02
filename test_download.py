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
from selenium_driver import initialize_driver
from dotenv import load_dotenv
import time
import os

def test_download(driver):
    try:
        print("測試：首頁-下載專區")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='category__description'][contains(text(),'下載專區')]"))
        ).click()
        time.sleep(2)
        if "下載項目" in driver.page_source:
            print("\033[32m進入下載專區成功\033[0m")
        else:
            print("\033[31m進入下載專區失敗\033[0m")
        time.sleep(2)

        # 搜尋
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        )
        keyword.send_keys("1")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用下載1" in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")
        keyword.clear()
        keyword.send_keys(" ")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用下載1" in driver.page_source and "自動化測試用下載2" in driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")
        
        # 驗證檔案
        original_window_handles = driver.window_handles
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='download-table__title text-ellipsis']"))
        ).click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(original_window_handles))
        new_window_handles = driver.window_handles

        if len(new_window_handles) > len(original_window_handles):
            new_window_handle = list(set(new_window_handles) - set(original_window_handles))[0]
            driver.switch_to.window(new_window_handle)
    
            # 檢查新分頁的網址
            time.sleep(2)
            load_dotenv()
            current_url = driver.current_url
            expected_url = os.getenv("BASE_URL") + "/base/10001/download/1/114年辦公日曆表.pdf"
            if current_url == expected_url:
                print("\033[32m新分頁打開且檔案正確\033[0m")
            else:
                print(f"\033[31m新分頁檔案不正確，當前檔案: {current_url}\033[0m")
    
            driver.close()
            driver.switch_to.window(original_window_handles[0])
        
        # 回首頁
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        print("回首頁")

    except TimeoutException as e:
        print(f"Timeout while waiting for button to be clickable: {e}")
    except NoSuchElementException as e:
        print(f"Button not found: {e}")

  
