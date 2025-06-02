from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from test_login import test_login
from admin_enter import admin_enter
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
from datetime import datetime
import time
import os
from dotenv import load_dotenv

nowdatetime = datetime.now().strftime("%Y-%m-%d")

def admin_add_account(driver):
    try:
        print("測試：管理者環境-帳號管理-新增帳號")
        time.sleep(2)
        menu_expanded(driver, "帳號管理", "新增帳號")
        time.sleep(2)
        if "批次帳號管理" in driver.page_source:
            print("\033[32m進入新增帳號成功\033[0m")
        else:
            print("\033[31m進入新增帳號失敗\033[0m")
            
        # 批次帳號管理
        time.sleep(2)
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='userlist']"))
        )
        userlist.clear()
        userlist.send_keys("yyy12345")
        begin = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='begin_date']"))
        )
        begin.clear()
        begin.send_keys(nowdatetime)
        end = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='end_date']"))
        )
        end.clear()
        end.send_keys(nowdatetime)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='create_btn']"))
        ).click()

        # 驗證
        time.sleep(2)
        if "新增成功" in driver.page_source:
            print("\033[32m新增不規則帳號成功\033[0m")
        else:
            print("\033[31m新增不規則帳號失敗\033[0m")
        time.sleep(2)

        # 記得密碼
        load_dotenv()
        code = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr td:nth-child(2)"))
        ).text
        print(code)
        time.sleep(2)
        email = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email[yyy12345]']"))
        )
        email.clear()
        email.send_keys(os.getenv("TEST_EMAIL"))
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-send']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='modal_error_btn']"))
        ).click()

        # 查詢人員
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'查詢人員')]"))
        ).click()
        time.sleep(2)
        type = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "keytype"))
        )
        select = Select(type)
        select.select_by_value("account")
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.clear()
        keyword.send_keys('yyy12345')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "1-1 筆 (共 1 筆)" in driver.page_source and "yyy12345" in driver.page_source:
            print("\033[32m查詢人員帳號成功\033[0m")
        else:
            print("\033[31m查詢人員帳號失敗\033[0m")  

        # 個人資料
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='badge']"))
        ).click()  
        time.sleep(2)
        begin_value = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "begin_time"))
        ).get_attribute("value")
        end_value = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "expire_time"))
        ).get_attribute("value")
        if begin_value == nowdatetime and end_value == nowdatetime:
            print("\033[32m帳號使用期限設定成功\033[0m")
        else:
            print("\033[31m帳號使用期限設定失敗\033[0m")    

        # 帳號啟用信
        time.sleep(10)
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(2)
        if "網路學園帳號啟用通知信" in driver.page_source:
            print("\033[32m發送帳號啟用信成功\033[0m")
        else:
            print("\033[31m發送帳號啟用信失敗\033[0m")
        driver.close()
        driver.switch_to.window(windows[0])
        time.sleep(2)

        # 登出
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='btnlogout']"))
        ).click() 
        time.sleep(2)

        # 登入新帳號
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='action__button-text']"))
        ).click() 
        ac = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, '//input[@id="account"]'))
        )
        ac.click()
        ac.send_keys("yyy12345")
        pw = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))
        )
        pw.click()
        pw.send_keys(code)
        # ca = WebDriverWait(driver, 10).until(  
        #     EC.element_to_be_clickable((By.XPATH, '//input[@id="captcha"]'))
        # )
        # ca.click()
        # ca.send_keys("9453")            
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()
        time.sleep(2)
        if "登入失敗" not in driver.page_source:
            print("\033[32m新增帳號登入成功\033[0m")
        else:
            print("\033[31m新增帳號登入失敗\033[0m")   

        # 復原
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mat-focus-indicator.action__button.action__button--blue.action__button--vertical-center.mat-button.mat-button-base"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'登出')]"))
        ).click()
        time.sleep(2)
        test_login(driver)
        admin_enter(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'查詢人員')]"))
        ).click()
        time.sleep(2)
        type = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "keytype"))
        )
        select = Select(type)
        select.select_by_value("account")
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.clear()
        keyword.send_keys('yyy12345')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click()  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#btn_del"))
        ).click() 
        time.sleep(2) 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除嗎" in alert_text:
            alert.accept()
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-dismiss='modal'][contains(text(),'確定')]"))
            ).click() 

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
