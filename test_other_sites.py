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
import time
from selenium_driver import initialize_driver

# 滾動到底部
def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def test_other_sites(driver): 
    try:
        print("測試：首頁-相關網站連結")
        scroll_bottom(driver)
        time.sleep(2)
        if "平台人數" in driver.page_source:
            print("\033[32m滾動到相關網站連結成功\033[0m")
        else:
            print("\033[31m滾動到相關網站連結失敗\033[0m")
        
        # 左右
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@svgicon='common:chevron-right']//*[name()='svg']"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@svgicon='common:chevron-left']//*[name()='svg']")) 
        ).click()
        time.sleep(2)

        # 相關網站連結跳轉
        original_window_handles = driver.window_handles
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='輪播圖第 0 張']"))
        ).click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(original_window_handles))
        new_window_handles = driver.window_handles

        if len(new_window_handles) > len(original_window_handles):
            new_window_handle = list(set(new_window_handles) - set(original_window_handles))[0]
            driver.switch_to.window(new_window_handle)
    
            # 檢查新分頁的網址
            time.sleep(2)
            current_url = driver.current_url
            expected_url = "https://www.sun.net.tw/product-dtmc"
            if current_url == expected_url:
                print("\033[32m點選相關網站連結並跳轉成功一次\033[0m")
            else:
                print("\033[31m點選相關網站連結失敗\033[0m")
        driver.close()
        driver.switch_to.window(original_window_handles[0])

        # 相關網站連結跳轉
        original_window_handles = driver.window_handles
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='輪播圖第 1 張']"))
        ).click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(original_window_handles))
        new_window_handles = driver.window_handles

        if len(new_window_handles) > len(original_window_handles):
            new_window_handle = list(set(new_window_handles) - set(original_window_handles))[0]
            driver.switch_to.window(new_window_handle)
    
            # 檢查新分頁的網址
            time.sleep(2)
            current_url = driver.current_url
            expected_url = "https://www.sun.net.tw/products-ctms"
            if current_url == expected_url:
                print("\033[32m點選相關網站連結並跳轉成功兩次\033[0m")
            else:
                print("\033[31m點選相關網站連結失敗\033[0m")
        driver.close()
        driver.switch_to.window(original_window_handles[0])

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
