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
from pywinauto import Application
import time

def scroll_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def course_chatroom(driver):
    try:
        print("測試：學習環境-聊天室/讀書會")
        scroll_bottom(driver)
        chatroom_or_bookclub = [
            (By.XPATH, "(//div[@class='mat-tab-label-content'][contains(text(),'聊天室')])[1]"),
            (By.XPATH, "(//div[@class='mat-tab-label-content'][contains(text(),'讀書會')])[1]"),
        ]
        for by, value in chatroom_or_bookclub:
            try:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((by, value))
                ).click()
                break
            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, WebDriverException):
                pass
        time.sleep(2)
        if "同步討論室" in driver.page_source:
            print("\033[32m進入聊天室成功\033[0m")
        else:
            print("\033[31m進入聊天室失敗\033[0m")
        time.sleep(2)

        # 進入聊天室
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'進入討論')]"))
        ).click()
        time.sleep(10)

        # 聊天
        input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//p[@class='chat-response__content']"))
        )
        input.click()
        input.send_keys("哈囉")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click()
        time.sleep(10)
        if "哈囉" in driver.page_source:
            print("\033[32m訊息已送出\033[0m")
        else:
            print("\033[31m訊息未送出\033[0m")
        time.sleep(2)

        # 語氣
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@role='combobox' and contains(@class, 'mat-select')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'公告')]"))
        ).click()
        input.click()
        input.send_keys("哈囉")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click()
        time.sleep(10)
        if "公告" in driver.page_source:
            print("\033[32m語氣-公告訊息已送出\033[0m")
        else:
            print("\033[31m語氣-公告訊息未送出\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@role='combobox' and contains(@class, 'mat-select')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'求助')]"))
        ).click()
        input.click()
        input.send_keys("哈囉")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click()
        time.sleep(10)
        if "求助" in driver.page_source:
            print("\033[32m語氣-求助訊息已送出\033[0m")
        else:
            print("\033[31m語氣-求助訊息未送出\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@role='combobox' and contains(@class, 'mat-select')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'討論')]"))
        ).click()
        input.click()
        input.send_keys("哈囉")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click()
        time.sleep(10)
        if "討論" in driver.page_source:
            print("\033[32m語氣-討論訊息已送出\033[0m")
        else:
            print("\033[31m語氣-討論訊息未送出\033[0m")
        time.sleep(2)

        # 附檔
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='附檔圖示']"))
        ).click()   
        time.sleep(2)
        description = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='description-for-files']"))
        )
        description.click()  
        description.send_keys("自動化測試用")  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增檔案')]"))
        ).click()    
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='刪除圖示']"))
        ).click() 
        time.sleep(5)
        if "宮下和" not in driver.page_source:
            print("\033[32m刪除檔案成功\033[0m")
        else:
            print("\033[31m刪除檔案失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增檔案')]"))
        ).click() 
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn--primary upload-dialog__btn']"))
        ).click()
        time.sleep(5)
        if "自動化測試用" in driver.page_source:
            print("\033[32m分享檔案成功\033[0m")
        else:
            print("\033[31m分享檔案失敗\033[0m")

        # 回列表
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回到列表')]"))
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