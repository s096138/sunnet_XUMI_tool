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
from pywinauto import Application
import time

def teacher_file_management(driver):
    try:
        print("測試：辦公室-課程管理-教材檔案管理")
        menu_expanded(driver, "課程管理", "教材檔案管理")
        time.sleep(2)
        if "檔案總管" in driver.page_source:
            print("\033[32m進入教材檔案管理成功\033[0m")
        else:
            print("\033[31m進入教材檔案管理失敗\033[0m")

        # 上傳檔案
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab04"))
        ).click()
        time.sleep(2)
        file = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='upload[]']"))
        )
        driver.execute_script("arguments[0].click();", file)
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='上傳']"))
        ).click()

        # 上傳壓縮檔
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab05"))
        ).click()
        file = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='uploadz']"))
        )
        driver.execute_script("arguments[0].click();", file)
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\chromedriver-win64.zip") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='上傳壓縮檔']"))
        ).click()

        # 新建目錄
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab02"))
        ).click()
        time.sleep(2)
        dir = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='newdir']"))
        )
        dir.click()
        dir.clear()
        dir.send_keys("自動化測試用")        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定建立')]"))
        ).click()

        # 檔案總管
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab01"))
        ).click()
        time.sleep(2)
        if "兔子" in driver.page_source:
            print("\033[32m上傳檔案成功\033[0m")
        else:
            print("\033[31m上傳檔案失敗\033[0m")
        time.sleep(2)
        if "chromedriver" in driver.page_source:
            print("\033[32m上傳壓縮檔成功\033[0m")
        else:
            print("\033[31m上傳壓縮檔失敗\033[0m")
        time.sleep(2)    
        if "自動化測試用" in driver.page_source:
            print("\033[32m新建目錄成功\033[0m")
        else:
            print("\033[31m新建目錄失敗\033[0m")

        # 複製
        copy = False
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='file_entry[]'])[1]"))
        ).click()
        driver.execute_script("copy('cp');") 
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'自動化測試用')]"))
        ).click()
        time.sleep(2)
        if "兔子" in driver.page_source:
            copy = True
        else:
            copy = False

        # 檢查 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'自動化測試用')]"))
        ).click()    
        time.sleep(2)
        if "兔子" in driver.page_source and copy == True:
            print("\033[32m複製檔案成功\033[0m")
        else:
            print("\033[31m複製檔案失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//b[normalize-space()='..']"))
        ).click()   

        # 搬移
        move = False
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='file_entry[]'])[1]"))
        ).click()
        
        driver.execute_script("copy('mv');")
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'自動化測試用')]"))
        ).click()
        if "兔子" not in driver.page_source:
            move = True
        else:
            move = False

        # 檢查 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'自動化測試用')]"))
        ).click()    
        time.sleep(2)
        if "兔子" in driver.page_source and move == True:
            print("\033[32m搬移檔案成功\033[0m")
        else:
            print("\033[31m搬移檔案失敗\033[0m")  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//b[normalize-space()='..']"))
        ).click()

        # 刪除
        time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='1'][name='dir_entry[]']"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='2'][name='dir_entry[]']"))
        # ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='ckbox']"))
        ).click()
        time.sleep(2)
        driver.execute_script("removeFile();")   
        time.sleep(2) 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除這些選定的項目嗎？" in alert_text:
            print("\033[32m刪除檔案及目錄成功\033[0m")
        else:
            print("\033[31m刪除檔案及目錄失敗\033[0m") 
        alert.accept()          
            
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
