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

def teacher_file_upload(driver):
    try:
        print("測試：辦公室-課程管理-教材上傳")
        menu_expanded(driver, "課程管理", "教材上傳")
        time.sleep(2)
        if "上傳檔案" in driver.page_source:
            print("\033[32m進入教材上傳成功\033[0m")
        else:
            print("\033[31m進入教材上傳失敗\033[0m")
        
        # 選擇檔案
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='iframeFileUpload']"))
        )  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#uploadStep1"))
        ).click()        
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\蛙蛙.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > span:nth-child(3) > input:nth-child(1)"))
        ).click()  
        if "上傳完成" in driver.page_source:
            print("\033[32m教材上傳成功\033[0m")
        else:
            print("\033[31m教材上傳失敗\033[0m")        

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > span:nth-child(5) > input:nth-child(1)"))
        ).click()  

        # driver.switch_to.default_content()
        
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