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
from pywinauto import Application
import time
import os
from dotenv import load_dotenv

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def course_chatroom_history(driver):
    try:
        print("測試：學習環境-聊天室紀錄/讀書會紀錄")
        scroll_bottom(driver)
        chatroom_or_bookclub = [
            (By.XPATH, "//div[@role='tab' and contains(., '聊天室紀錄')]"),
            (By.XPATH, "//div[@role='tab' and contains(., '讀書會紀錄')]"),
        ]
        for by, value in chatroom_or_bookclub:
            try:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((by, value))
                ).click()
                break
            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, WebDriverException):
                pass
        time.sleep(2)
        if "sysop" in driver.page_source:
            print("\033[32m進入聊天室紀錄成功\033[0m")
        else:
            print("\033[31m進入聊天室紀錄失敗\033[0m")
        time.sleep(2)

        # 發信 - 壞的
        load_dotenv()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//mat-icon[@aria-label='信件圖示'][normalize-space()='mail'])[1]"))
        ).click()
        email = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='轉寄']"))
        )
        email.click()
        email.send_keys(os.getenv("TEST_EMAIL"))
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='加號圖示']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()
        time.sleep(2)
        if "發送成功" in driver.page_source:
            print("\033[32m轉寄聊天室紀錄成功\033[0m")
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'關閉')]"))
            ).click()
        else:
            print("\033[31m轉寄聊天室紀錄失敗\033[0m")

        # # 另開視窗
        # time.sleep(10)
        # driver.execute_script("window.open('');")
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])
        # driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        # time.sleep(2)
        # if "自動化測試用" in driver.page_source:
        #     print("\033[32m確實收到信件\033[0m")
        # else:
        #     print("\033[31m未收到信件\033[0m")
        # driver.close()
        # driver.switch_to.window(windows[0])
        # time.sleep(2)

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