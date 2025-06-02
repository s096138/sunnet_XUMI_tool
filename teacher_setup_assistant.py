from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
import time

def teacher_setup_assistant(driver):
    try:
        print("測試：辦公室-人員管理-設定助教")
        menu_expanded(driver, "人員管理", "設定助教")
        time.sleep(2)
        if "新增授課助教" in driver.page_source:
            print("\033[32m進入設定助教成功\033[0m")
        else:
            print("\033[31m進入設定助教失敗\033[0m")

        # 新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "addBtn1"))
        ).click()
        user = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))
        )
        user.click()
        user.clear()
        user.send_keys("joy03")    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btn_submit"))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='回列表']"))
        ).click() 
        time.sleep(2)
        if "joy03" in driver.page_source:
            print("\033[32m新增助教成功\033[0m")
        else:
            print("\033[31m新增助教失敗\033[0m")  

        # 查詢
        search = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='queryTxt']"))
        )
        search.click()
        search.clear()
        search.send_keys("03")          
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'查詢')]"))
        ).click() 
        time.sleep(2)
        if "1-1 筆 (共 1 筆)" in driver.page_source:
            print("\033[32m查詢助教成功\033[0m")
        else:
            print("\033[31m查詢助教失敗\033[0m") 
        time.sleep(2)
        search = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='queryTxt']"))
        )
        search.click()
        search.clear()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'查詢')]"))
        ).click() 
        time.sleep(2)
        if "joy09" in driver.page_source and "joy03" in driver.page_source:
            print("\033[32m查詢空白成功\033[0m")
        else:
            print("\033[31m查詢空白失敗\033[0m")
        
        # 修改
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'修改')]"))
        ).click()        
        role = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        select = Select(role)
        select.select_by_value("instructor") 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'修改')]"))
        ).click()         
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='回列表']"))
        ).click() 
        time.sleep(2)
        if "講師" in driver.page_source:
            print("\033[32m修改助教成功\033[0m")
        else:
            print("\033[31m修改助教失敗\033[0m")
        
        # 刪除
        time.sleep(2)
        checkbox = driver.find_element(By.CSS_SELECTOR, "input[value='joy03@instructor']")
        driver.execute_script("arguments[0].click();", checkbox)     
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'刪除')]"))
        ).click() 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定要刪除嗎" in alert_text:
            print("\033[32m刪除助教成功\033[0m")
            alert.accept()
        else:
            print("\033[31m刪除助教失敗\033[0m")                 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='回列表']"))
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