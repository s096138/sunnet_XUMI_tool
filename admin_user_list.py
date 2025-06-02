from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException,
    StaleElementReferenceException
)
from menu_expanded import menu_expanded
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from admin_enter import admin_enter
import time
import os

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def admin_user_list(driver):
    try:
        print("測試：管理者環境-帳號管理-查詢人員")
        time.sleep(2)
        menu_expanded(driver, "帳號管理", "查詢人員")
        time.sleep(2)
        if "變更身分" in driver.page_source:
            print("\033[32m進入查詢人員成功\033[0m")
        else:
            print("\033[31m進入查詢人員失敗\033[0m")

        # 姓名搜尋
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.send_keys('小精靈')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "1-1 筆 (共 1 筆)" in driver.page_source:
            print("\033[32m姓名查詢成功\033[0m")
        else:
            print("\033[31m姓名查詢失敗\033[0m")   
        
        # 空白搜尋
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.clear()
        keyword.send_keys(' ')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "1-1 筆 (共 1 筆)" not in driver.page_source:
            print("\033[32m空白查詢成功\033[0m")
        else:
            print("\033[31m空白查詢失敗\033[0m")   

        # 帳號搜尋
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
        keyword.send_keys('joy09')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "1-1 筆 (共 1 筆)" in driver.page_source:
            print("\033[32m帳號查詢成功\033[0m")
        else:
            print("\033[31m帳號查詢失敗\033[0m")       
        
        # 個人資料
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='badge']"))
        ).click()
        time.sleep(2)
        if "小精靈" in driver.page_source:
            print("\033[32m查看個人資料成功\033[0m")
        else:
            print("\033[31m查看個人資料失敗\033[0m")    
        scroll_bottom(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='back_btn']"))
        ).click()  

        # 修課紀錄
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
        keyword.send_keys('joy09')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='pending_actions']"))
        ).click()
        time.sleep(2)
        if "最近上課時間" in driver.page_source:
            print("\033[32m查看修課紀錄成功\033[0m")
        else:
            print("\033[31m查看修課紀錄失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='back_btn']"))
        ).click()  

        # 修課紀錄
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
        keyword.send_keys('joy09')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "tbody tr td:nth-child(8) span:nth-child(1)"))
        ).click()
        time.sleep(2)
        if "修課狀態" in driver.page_source:
            print("\033[32m查看學習成果成功\033[0m")
        else:
            print("\033[31m查看學習成果失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='back_btn']"))
        ).click()  

        # 變更身分
        time.sleep(2) # 第一位
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(9) span:nth-child(1)"))
        ).click()         
        time.sleep(2)
        convert_user_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "convert_user"))
        )
        name = convert_user_element.text
        print(f"切換登入身分: {name}")  
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='loginsubmit']"))
        ).click()
        time.sleep(2)
        if "無法變更擁有管理者權限的身分" in driver.page_source:
            print("\033[31m變更身分失敗\033[0m")
            return
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'個人資料')]"))
        ).click()        
        time.sleep(2)
        username = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).get_attribute("value")
        if username == name:
            print("\033[32m變更身分成功\033[0m")
        else:
            print("\033[31m變更身分失敗\033[0m")

        # 登出
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'登出')]"))
        ).click()  
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "action__button-text"))
        ).click()
        username_input = driver.find_element(By.ID, 'account')
        username_input.clear()
        username_input.send_keys('joy09')
        password_input = driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('j123456')
        # captcha_input = driver.find_element(By.XPATH, '//input[@id="captcha"]')
        # captcha_input.clear()
        # captcha_input.send_keys('9453')
        submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')         
        submit_button.click()
        admin_enter(driver)

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