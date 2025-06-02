from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from datetime import datetime
from pywinauto import Application
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
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
            
def teacher_notice_board(driver):
    try:
        print("測試：辦公室-教室管理-課程公告板")
        menu_expanded(driver, "教室管理", "課程公告板")
        time.sleep(2)
        if "課程公告板" in driver.page_source:
            print("\033[32m進入課程公告板成功\033[0m")
        else:
            print("\033[31m進入課程公告板失敗\033[0m")   

        # 修改
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'修改')]"))
        ).click()
        time.sleep(2)
        if "填寫更多語言" in driver.page_source:
            print("\033[32m進入修改課程公告板成功\033[0m")
        else:
            print("\033[31m進入修改課程公告板失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='回列表']"))
        ).click()
        time.sleep(2)

        # 進入課程公告板
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='課程公告板']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'張貼')]"))
        ).click()
        time.sleep(2)
        title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='subject'][type='text']"))
        )
        title.send_keys("自動化測試用")
        editor = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))
        )
        editor.send_keys("自動化測試用")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='btnBrowse']"))
        ).click()
        time.sleep(5)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source and "兔子.jpg" in driver.page_source:
            print("\033[32m新增課程公告成功\033[0m")
        else:
            print("\033[31m新增課程公告失敗\033[0m")

        # 修改
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='修改']"))
        ).click()
        time.sleep(2)
        title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='subject'][type='text']"))
        )
        title.clear()
        title.send_keys("自動化測試修改用")
        editor = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ql-editor']"))
        )
        editor.clear()
        editor.send_keys("自動化測試修改用")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='material-icons text-secondary']"))
        ).click()
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']"))
        ).click()
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source and "自動化測試用" not in driver.page_source and "兔子.jpg" not in driver.page_source:
            print("\033[32m修改課程公告成功\033[0m")
        else:
            print("\033[31m修改課程公告失敗\033[0m")

        # 回覆
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'回覆')]"))
        ).click()
        time.sleep(2)
        editor = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))
        )
        editor.clear()
        editor.send_keys("自動化測試回覆用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='btnBrowse']"))
        ).click()
        time.sleep(5)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']"))
        ).click()
        time.sleep(2)
        if "自動化測試回覆用" in driver.page_source and "兔子.jpg" in driver.page_source:
            print("\033[32m回覆課程公告成功\033[0m")
        else:
            print("\033[31m回覆課程公告失敗\033[0m")

        # 刪除
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='reply node-info']//div[@title='刪除']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定刪除?" in alert_text:
            alert.accept()
        else:
            print(f"alert text: {alert_text}")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "刪除成功" in alert_text:
            alert.accept()
        else:
            print(f"alert text: {alert_text}")
        time.sleep(2)
        if "自動化測試回覆用" not in driver.page_source and "兔子.jpg" not in driver.page_source:
            print("\033[32m刪除回覆成功\033[0m")
        else:
            print("\033[31m刪除回覆失敗\033[0m")
            
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='刪除']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定刪除?" in alert_text:
            alert.accept()
        else:
            print(f"alert text: {alert_text}")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "刪除成功" in alert_text:
            alert.accept()
        else:
            print(f"alert text: {alert_text}")
        time.sleep(2)
        if "課程公告板" in driver.page_source:
            print("\033[32m刪除課程公告成功\033[0m")
        else:
            print("\033[31m刪除課程公告失敗\033[0m")

        # 訂閱
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='subscribe']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "成功訂閱" in alert_text:
            alert.accept()
        else:
            print(f"alert text: {alert_text}")
        time.sleep(2)
        if "取消訂閱" in driver.page_source:
            print("\033[32m訂閱課程公告成功\033[0m")
        else:
            print("\033[31m訂閱課程公告失敗\033[0m")
        
        # 取消訂閱
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='subscribe']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "成功取消訂閱" in alert_text:
            alert.accept()
        else:
            print(f"alert text: {alert_text}")
        time.sleep(2)
        if "訂閱" in driver.page_source:
            print("\033[32m取消訂閱課程公告成功\033[0m")
        else:
            print("\033[31m取消訂閱課程公告失敗\033[0m")       

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