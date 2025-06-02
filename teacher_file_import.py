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

def teacher_file_import(driver):
    try:
        print("測試：辦公室-課程管理-教材匯入")
        menu_expanded(driver, "課程管理", "教材匯入")
        time.sleep(2)
        if "單一上傳檔案size不得超過" in driver.page_source:
            print("\033[32m進入教材匯入成功\033[0m")
        else:
            print("\033[31m進入教材匯入失敗\033[0m")

        # 上傳
        time.sleep(2)
        file = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#package_file"))
        )
        # driver.execute_script("arguments[0].click();", file)
        file.send_keys(r"C:\Users\SGQA2\Downloads\chromedriver-win64.zip")
        # time.sleep(2)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\chromedriver-win64.zip") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn6"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()
        time.sleep(2) 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "匯入教材完成" in alert_text:
            print("\033[32m匯入一般檔案教材成功\033[0m")
            alert.accept()
        else:
            print("\033[31m匯入一般檔案教材失敗\033[0m")   

        # 驗證
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'教材檔案管理')]"))
        ).click()
        time.sleep(2)
        if "chromedriver-win64" in driver.page_source:
            print("\033[32m檔案教材管理顯示教材成功\033[0m")
        else:
            print("\033[31m檔案教材管理顯示教材失敗\033[0m")              
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='1'][name='dir_entry[]']"))
        ).click()  
        driver.execute_script("removeFile();")     
        time.sleep(2) 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除這些選定的項目嗎？" in alert_text:
            alert.accept()

        # SCORM課程包
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'教材匯入')]"))
        ).click()

        # 上傳
        time.sleep(2)
        file = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#package_file"))
        )
        file.send_keys(r"C:\Users\SGQA2\Desktop\SCORM 課程.zip")
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn3"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()
        time.sleep(2) 
        alert = driver.switch_to.alert 
        alert_text = alert.text
        if "匯入教材完成" in alert_text:
            print("\033[32m匯入SCORM課程包成功\033[0m")
            alert.accept()
        else:
            print("\033[31m匯入SCORM課程包失敗\033[0m")

        # 驗證
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'教材檔案管理')]"))
        ).click()
        time.sleep(2)
        if "sco_cmi.xml" in driver.page_source:
            print("\033[32m檔案教材管理顯示教材成功\033[0m")
        else:
            print("\033[31m檔案教材管理顯示教材失敗\033[0m")              
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ckbox"))
        ).click()  
        driver.execute_script("removeFile();")     
        time.sleep(2) 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除這些選定的項目嗎？" in alert_text:
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