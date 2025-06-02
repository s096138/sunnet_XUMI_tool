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

def teacher_video_list(driver):
    try:
        print("測試：辦公室-課程管理-全能影像轉譯(影片列表)")
        menu_expanded(driver, "課程管理", "全能影像轉譯")
        time.sleep(2)
        if "讓備課更輕鬆" in driver.page_source:
            print("\033[32m進入全能影像轉譯(影片列表)成功\033[0m")
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'立即探索!')]"))
            ).click()
            try:
                time.sleep(2)
                alert = driver.switch_to.alert
                alert_text = alert.text            
                time.sleep(2)
                if "還沒有影片嗎?讓我們先上傳影片吧!" in alert_text:
                    alert.accept()
            except NoAlertPresentException:
                print("\033[32m沒有出現alert\033[0m")
        else:
            print("\033[31m影片列表已有影片\033[0m")
            return

        # 新增影片
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-add']"))
        ).click()  
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='start']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        if "請選擇檔案" in alert_text:
            print("\033[32m未上傳影片不可新增\033[0m")
        else:
            print("\033[31m未上傳影片可以新增\033[0m")
        alert.accept()

        # 上傳影片
        upload = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='fileupload']"))
        ) 
        driver.execute_script("arguments[0].click();", upload)
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\202410旭航v4.mp4") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='start']"))
        ).click()
        time.sleep(30) #等待上傳
        if "202410旭航v4.mp4" in driver.page_source:
            print("\033[32m新增影片成功\033[0m")
        else:
            print("\033[31m新增影片失敗\033[0m")

        # 刪除
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-del']"))
        ).click() 
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        if "請勾選檔案" in alert_text:
            print("\033[32m未勾選檔案不可刪除\033[0m")
            alert.accept()
        else:
            print("\033[31m未勾選檔案可以刪除\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='file#202410旭航v4.mp4']"))
        ).click()        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-del']"))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='delete']"))
        ).click() 
        time.sleep(2)
        if "test.jpg" not in driver.page_source:
            print("\033[32m刪除影片成功\033[0m")
        else:
            print("\033[31m刪除影片失敗\033[0m")

        # 再新增影片
        try:
            time.sleep(2)
            alert = driver.switch_to.alert
            alert_text = alert.text            
            time.sleep(2)
            if "還沒有影片嗎?讓我們先上傳影片吧!" in alert_text:
                alert.accept()
        except NoAlertPresentException:
            print("\033[32m沒有出現alert\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-add']"))
        ).click()  
        upload = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='fileupload']"))
        ) 
        driver.execute_script("arguments[0].click();", upload)
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\202410旭航v4.mp4") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='start']"))
        ).click()
        time.sleep(10) #等待上傳


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