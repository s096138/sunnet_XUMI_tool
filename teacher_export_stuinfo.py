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
import time
import os
from dotenv import load_dotenv

def teacher_export_stuinfo(driver):
    try:
        print("測試：辦公室-人員管理-匯出學員資料")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'匯出學員資料')]"))
        ).click()
        time.sleep(2)
        if "個人資訊" in driver.page_source:
            print("\033[32m點擊匯入學員資料成功\033[0m")
        else:
            print("\033[31m點擊匯入學員資料失敗\033[0m")

        # 收件者
        time.sleep(2)
        load_dotenv()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save_btn']"))
        ).click()  
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請輸入 email" in alert_text:
            print("\033[32m未輸入eamil不可匯出\033[0m")
            alert.accept()
        else:
            print("\033[31m未輸入eamil可以匯出\033[0m")     
        time.sleep(2)  
        send = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='send_email']"))
        )
        send.click()
        send.send_keys(os.getenv("TEST_EMAIL"))
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save_btn']"))
        ).click()     
        if "已發送" in driver.page_source:
            print("\033[32m寄信成功\033[0m")
        else:
            print("\033[31m寄信失敗\033[0m")    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-wm-purple-outline']"))
        ).click()   

        # 另開視窗
        time.sleep(5) #等待發信
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(2)
        if "匯出人員資料" in driver.page_source:
            print("\033[32m匯出人員資料成功\033[0m")
        else:
            print("\033[31m匯出人員資料未收到信\033[0m")
        driver.close()
        driver.switch_to.window(windows[0])
        time.sleep(2)     

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