from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def scroll_top(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,0);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def admin_course_permission(driver):
    try:
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程設定')]"))
        # ).click()

        # 接續admin_course_introduction
        print("測試：管理者環境-課程管理-課程設定(權限設定)") 
        driver.refresh()
        scroll_top(driver)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="setup-tab"]'))
        ).click() 

        # 教師
        time.sleep(2)
        driver.execute_script("select_teacher('setTeacherValue')") 
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("yyy") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="yyytest"]'))
        ).click() 
        driver.execute_script("ReturnWork()") 
        time.sleep(2)
        if "yyytest" in driver.page_source:
            print("\033[32m新增教師成功\033[0m")
        else:
            print("\033[31m新增教師失敗\033[0m")

        # 講師
        time.sleep(2)
        driver.execute_script("select_teacher('setInstructorValue')") 
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("yyy") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="yyytest"]'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "帳號yyytest已存在於教師名單中" in alert_text:
            print("\033[32m教師名單不可重複\033[0m")
        else:
            print("\033[31m教師名單可以重複\033[0m")
        alert.accept()
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.clear()
        keyword.send_keys("MUMU") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="MUMUMU"]'))
        ).click() 
        driver.execute_script("ReturnWork()")
        time.sleep(2)
        if "MUMUMU" in driver.page_source:
            print("\033[32m新增講師成功\033[0m")
        else:
            print("\033[31m新增講師失敗\033[0m")

        # 助教
        time.sleep(2)
        driver.execute_script("select_teacher('setAssistantValue')") 
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("MU") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="MUMUMU"]'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "帳號MUMUMU已存在於講師名單中" in alert_text:
            print("\033[32m講師名單不可重複\033[0m")
        else:
            print("\033[31m講師名單可以重複\033[0m")
        alert.accept()
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.clear()
        keyword.send_keys("didi") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="didi"]'))
        ).click() 
        driver.execute_script("ReturnWork()")
        time.sleep(2)
        if "didi" in driver.page_source:
            print("\033[32m新增助教成功\033[0m")
        else:
            print("\033[31m新增助教失敗\033[0m")  

        # 重複
        time.sleep(2)
        driver.execute_script("select_teacher('setTeacherValue')") 
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.clear()
        keyword.send_keys("didi") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()
        time.sleep(2) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="didi"]'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "帳號didi已存在於助教名單中" in alert_text:
            print("\033[32m助教名單不可重複\033[0m")
        else:
            print("\033[31m助教名單可以重複\033[0m")
        alert.accept()
        time.sleep(2)
        driver.execute_script("ReturnWork()")
        
        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="setup-tab"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="teach_yyytest"]/span'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="teach_MUMUMU"]/span'))
        ).click()         
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="teach_didi"]/span'))
        ).click() 
        driver.execute_script("save_step(6)")
        time.sleep(2)   
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功" in alert_text:
            print("\033[32m儲存修改成功\033[0m")
        else:
            print("\033[31m儲存修改失敗\033[0m")
        alert.accept()
        time.sleep(2)  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="setup-tab"]'))
        ).click()   
        if "yyytest" not in driver.page_source:
            print("\033[32m刪除教師成功\033[0m")
        else:
            print("\033[31m刪除教師失敗\033[0m")
        time.sleep(2)
        if "MUMUMU" not in driver.page_source:
            print("\033[32m刪除講師成功\033[0m")
        else:
            print("\033[31m刪除講師失敗\033[0m")
        time.sleep(2)
        if "didi" not in driver.page_source:
            print("\033[32m刪除講師成功\033[0m")
        else:
            print("\033[31m刪除講師失敗\033[0m")

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