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

# 取得當前時間
nowdatetime = datetime.now().strftime("%Y-%m-%d")

def admin_homedownload(driver):
    try:
        print("測試：管理者環境-公告管理-首頁下載專區")
        menu_expanded(driver, "公告管理", "首頁下載專區")
        time.sleep(2)
        if "附檔" in driver.page_source:
            print("\033[32m進入首頁下載專區成功\033[0m")
        else:
            print("\033[31m進入首頁下載專區失敗\033[0m") 
        
        # 新增
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'title'))
        )
        name.click()
        name.send_keys("自動化測試用")
        time.sleep(2)
        day1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'open_date'))
        )
        day1.click()
        day1.send_keys(nowdatetime)
        day2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'close_date'))
        )
        day2.click()
        day2.send_keys(nowdatetime)
        time.sleep(2)
        photo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'upload'))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\蛙蛙.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)

        # 確定
        driver.execute_script("checkData()")
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="4"]'))
        # ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增檔案成功\033[0m")
        else:
            print("\033[31m新增檔案失敗\033[0m") 
        
        # 修改
        time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="4"]'))
        # ).click()
        time.sleep(2)
        found_and_edit = False
        for tr in driver.find_elements(By.XPATH, '//tr'):
            tds = tr.find_elements(By.TAG_NAME, 'td')
            if len(tds) > 0 and tds[1].text == "自動化測試用":
                found_and_edit = True
                tds[-1].find_element(By.TAG_NAME, 'span').click()
                break
        time.sleep(2)
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'title_edit'))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試修改用")
        driver.execute_script("EditData()")
        time.sleep(2)
        if found_and_edit and "自動化測試修改用" in driver.page_source:
            print("\033[32m修改檔案成功\033[0m")
        else:
            print("\033[31m修改檔案失敗\033[0m") 
        
        # 刪除
        time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="4"]'))
        # ).click()
        time.sleep(2)
        found_and_deleted = False
        for tr in driver.find_elements(By.XPATH, '//tr'):
            tds = tr.find_elements(By.TAG_NAME, 'td')
            if len(tds) > 0 and tds[1].text == "自動化測試修改用":
                found_and_deleted = True
                tr.find_element(By.XPATH, './/input[@type="checkbox"]').click()
                break
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="btn_del"]'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "您確定要刪除嗎?"
        alert.accept()

        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "刪除成功"
        alert.accept()

        time.sleep(2)
        if found_and_deleted and "自動化測試修改用" not in driver.page_source:
            print("\033[32m刪除檔案成功\033[0m")
        else:
            print("\033[31m刪除檔案失敗\033[0m") 

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