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
from datetime import datetime
from pywinauto import Application
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import os
from dotenv import load_dotenv

def admin_FAQ(driver):
    try:
        print("測試：管理者環境-公告管理-常見問題")
        menu_expanded(driver, "公告管理", "常見問題")
        time.sleep(2)
        if "問題分類" in driver.page_source and "設定分類" in driver.page_source:
            print("\033[32m進入常見問題成功\033[0m")
        else:
            print("\033[31m進入常見問題失敗\033[0m") 
        
        # # 新增分類
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-edit-category']"))
        # ).click()
        # time.sleep(2)
        # if "自動化測試用分類" in driver.page_source:
        #     WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'del-txt') and preceding-sibling::input[@value='自動化測試用分類']]"))
        #     ).click()
        #     time.sleep(2)
        #     alert = driver.switch_to.alert
        #     alert.accept()            
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增分類')]"))
        # ).click()
        # time.sleep(2)
        # class_name = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='新分類']"))
        # )
        # class_name.send_keys("自動化測試用分類")
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='categories-submit']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # time.sleep(2)
        # if "儲存成功" in alert_text:
        #     print("\033[32m新增分類成功\033[0m")
        # else:
        #     print("\033[31m新增分類失敗\033[0m")
        # alert.accept()

        # 新增問題
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        time.sleep(2)
        select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'category'))
        )
        select = Select(select)
        select.select_by_visible_text("自動化測試用分類1")

        # 未填主旨
        driver.execute_script("checkData()")
        if "主旨名稱請務必填寫" in driver.page_source:
            print("\033[32m未填主旨不可新增\033[0m")
        else:
            print("\033[31m未填主旨可以新增\033[0m")
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="subject"]'))
        )
        name.click()
        name.send_keys("自動化測試用")
        time.sleep(2)

        # 未填內文
        driver.execute_script("checkData()")
        if "本文請務必填寫" in driver.page_source:
            print("\033[32m未填內文不可新增\033[0m")
        else:
            print("\033[31m未填內文可以新增\033[0m")
        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用</p>'", editable_body)
        # driver.switch_to.default_content()
        time.sleep(2)
        
        # 確定
        driver.execute_script("checkData()")
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增常見問題成功\033[0m")
        else:
            print("\033[31m新增常見問題失敗\033[0m")
            
        # 分類搜尋
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_category"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'自動化測試用分類')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m分類搜尋成功\033[0m")
        else:
            print("\033[31m分類搜尋失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_category"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='全部']"))
        ).click()
        time.sleep(2)

        # 關鍵字搜尋
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("自動化測試用常見問題1")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search_btn"))
        ).click()
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='wm-page-num pe-2']"))
        )
        element_text = element.text.strip()
        if element_text == "1-1 筆 (共 1 筆)":
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")

        # 轉寄
        load_dotenv()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@title='轉寄']"))
        ).click()
        alert = driver.switch_to.alert
        alert.send_keys(os.getenv("TEST_EMAIL"))
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "文章已寄出" in alert_text:
            print("\033[32m轉寄文章成功\033[0m")
        else:
            print("\033[31m轉寄文章失敗\033[0m")
        time.sleep(2)
        alert.accept()
        
        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='list-group-tool ms-auto col-auto'] span[title='刪除']"))
        ).click()           
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "您確定要刪除嗎?"
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        if "刪除成功" in alert_text:
            print("\033[32m刪除文章成功\033[0m")
        else:
            print("\033[31m刪除文章失敗\033[0m")
        time.sleep(2)
        alert.accept()

        # 另開視窗
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m轉寄常見問題收到信件\033[0m")
        else:
            print("\033[31m轉寄常見問題未收到信件\033[0m")
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