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
from datetime import datetime
import time

nowdatetime = datetime.now().strftime("%Y-%m")

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def teacher_warning(driver):
    try:
        print("測試：辦公室-人員管理-預警通知")
        menu_expanded(driver, "人員管理", "預警通知")
        time.sleep(2)
        if "預警設定" in driver.page_source:
            print("\033[32m點擊預警通知成功\033[0m")
        else:
            print("\033[31m點擊預警通知失敗\033[0m")

        # 預警設定
        role = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        role.click()
        select = Select(role)
        select.select_by_visible_text("正式生")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='ckFilter']"))
        ).click()        
        mtOP = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='mtOP']"))
        )
        select = Select(mtOP)
        select.select_by_value("greater")
        times = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='mtVal']"))
        )
        times.click()
        times.send_keys("1")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='start_pick']"))
        ).click()   
        time.sleep(2)      
        if driver.page_source.count("寄送通知信") == 2:
            print("\033[32m挑選成功\033[0m")
        else:
            print("\033[31m挑選失敗\033[0m")  
        time.sleep(2) 
        td = driver.find_element(By.XPATH, '//*[@id="resTable"]/tbody/tr/td[6]')
        if td.text >= '1':
            print("\033[32m挑選資料正確\033[0m")
        else:
            print("\033[31m挑選資料錯誤\033[0m")     

        # 自動預警設定 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "tab02"))
        ).click() 
        time.sleep(2)       
        if "自動化點名寄信機制" in driver.page_source:
            print("\033[32m切換頁籤成功\033[0m")
        else:
            print("\033[31m切換頁籤失敗\033[0m")  

        # 新增
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增')]"))
        ).click()                     
        times = WebDriverWait(driver, 20).until( # 條件
            EC.element_to_be_clickable((By.XPATH, "//input[@id='mtVal']"))
        )
        times.click()
        times.send_keys("1")
        WebDriverWait(driver, 20).until( # 頻率
            EC.element_to_be_clickable((By.XPATH, "//input[@id='freq_once_day']"))
        ).click() 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td[normalize-space()='1']"))
        ).click() 
        time.sleep(2)
        start = WebDriverWait(driver, 20).until( # 起
            EC.element_to_be_clickable((By.XPATH, "//input[@id='begin_time']"))
        ) 
        startday = f"{nowdatetime}-01" 
        driver.execute_script("arguments[0].setAttribute('value', arguments[1])", start, startday)
        time.sleep(2)
        end = WebDriverWait(driver, 20).until( # 訖
            EC.element_to_be_clickable((By.XPATH, "//input[@id='end_time']"))
        )
        endday = f"{nowdatetime}-30" 
        driver.execute_script("arguments[0].setAttribute('value', arguments[1])", end, endday)
        scroll_bottom(driver)
        time.sleep(2)
        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用</p>'", editable_body)
        # driver.switch_to.default_content()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="確定"]'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增點名規則成功" in alert_text:
            print("\033[32m新增點名規則成功\033[0m")
            alert.accept()
        else:
            print("\033[31m新增點名規則失敗\033[0m") 

        # 停用
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsSystem"]/tbody/tr[5]/td[1]/input'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'停用')]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "停用成功" in alert_text:
            print("\033[32m停用點名規則成功\033[0m")
            alert.accept()
        else:
            print("\033[31m停用點名規則失敗\033[0m") 

        # 啟用
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsSystem"]/tbody/tr[5]/td[1]/input'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'啟用')]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "啟用成功" in alert_text:
            print("\033[32m啟用點名規則成功\033[0m")
            alert.accept()
        else:
            print("\033[31m啟用點名規則失敗\033[0m") 

        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsSystem"]/tbody/tr[5]/td[1]/input'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'刪除')]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "您確定要刪除嗎？"
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "刪除成功" in alert_text:
            print("\033[32m刪除點名規則成功\033[0m")
            alert.accept()
        else:
            print("\033[31m刪除點名規則失敗\033[0m") 

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