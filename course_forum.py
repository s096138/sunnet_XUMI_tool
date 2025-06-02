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
from selenium.webdriver.common.keys import Keys
from pywinauto import Application
import time
import os

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def course_forum(driver):
    try:
        print("測試：學習環境-討論區")
        driver.refresh()
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//div[@role='tab' and contains(., '討論區')]"))
        ).click()
        time.sleep(2)
        if "發表主題" in driver.page_source:
            print("\033[32m進入討論區成功\033[0m")
        else:
            print("\033[31m進入討論區失敗\033[0m")

        # 發表
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'發表主題')]"))
        ).click()
        time.sleep(2)
        Topics = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入討論主題']"))
        )
        Topics.send_keys('自動化測試用')
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='編輯器, editor1']"))
        )
        editor_body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body.cke_editable"))
        )
        editor_body.clear()
        editor_body.send_keys("自動化測試用")
        time.sleep(2)
        driver.switch_to.default_content()
        # time.sleep(2)
        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, ".ql-editor"))
        # )
        # editable.click()  
        # editable.send_keys("自動化測試")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選擇檔案')]"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\蛙蛙.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'張貼討論')]"))
        ).click()
        
        # 驗證
        time.sleep(2)
        if "自動化測試用" in driver.page_source and "蛙蛙.jpg" in driver.page_source:
            print("\033[32m發布主題成功\033[0m")
        else:
            print("\033[31m發布主題失敗\033[0m")

        # 關鍵字搜尋
        search = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        )
        search.clear()
        search.send_keys("自動化測試用")   
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()

        # 驗證
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")

        forum_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//cgust-thread"))
        )
        for forum in forum_elements:
            title_element = forum.find_element(By.XPATH, "//em[@class='thread__title ng-star-inserted']")
            if title_element.text == "自動化測試用":
                time.sleep(2)
                dot_button = forum.find_element(By.XPATH, "//button[@class='mat-menu-trigger comment__header-btn comment__header-btn--web ng-star-inserted']//mat-icon[@aria-label='更多動作圖示']//*[name()='svg']")
                dot_button.click()
                edit_button = forum.find_element(By.XPATH, "//button[contains(text(),'編輯')]")
                edit_button.click()
                break
        time.sleep(2)
        Topics = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入標題']"))
        )
        Topics.clear()
        Topics.send_keys("自動化測試修改用")
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='編輯器, editor2']"))
        )
        editor_body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body.cke_editable"))
        )
        editor_body.clear()
        editor_body.send_keys("自動化測試修改用")
        time.sleep(2)
        driver.switch_to.default_content()
        # time.sleep(2)
        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, ".ql-editor"))
        # )
        # editable.click()  
        # editable.send_keys("自動化測試")
        time.sleep(2)

        # 修改附檔
        scroll_bottom(driver)
        WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'刪除')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選擇檔案')]"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 驗證
        driver.refresh()
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,  "#mat-tab-label-0-2"))
        ).click()
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source and "兔子.jpg" in driver.page_source:
            print("\033[32m修改主題與附檔成功\033[0m")
            if "蛙蛙.jpg" not in driver.page_source:
                print("\033[32m附檔刪除成功\033[0m")
        else:
            print("\033[31m修改主題與附檔失敗\033[0m")

        # 按讚
        topic_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//em[text()='自動化測試修改用']"))
        )
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        ).click()
        time.sleep(2)
        like_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button1 = like_button.text.strip()
        time.sleep(2)

        # 驗證
        # print(button1)
        if button1 == "1":
            print("\033[32m按讚數+1\033[0m")
        else:
            print("\033[31m按讚數無變化\033[0m")
            
        # 驗證點讚按鈕狀態
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button_class = button.get_attribute("class")
        time.sleep(2)
        if "comment__press-like--liked" in button_class:
            print("\033[32m按讚成功\033[0m")
        else:
            print("\033[31m按讚失敗\033[0m")

        # 收回讚     
        topic_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//em[text()='自動化測試修改用']"))
        )
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        ).click()
        time.sleep(2)
        like_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button0 = like_button.text.strip()
        time.sleep(2)

        # 驗證
        # print(button0)
        if button0 == "0":
            print("\033[32m按讚數-1\033[0m")
        else:
            print("\033[31m按讚數無變化\033[0m")            

        # 驗證點讚按鈕狀態
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button_class = button.get_attribute("class")
        time.sleep(2)
        if "comment__press-like--liked" not in button_class:
            print("\033[32m收回讚成功\033[0m")
        else:
            print("\033[31m收回讚失敗\033[0m")

        # 回覆討論
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回覆')]"))
        ).click()
        reply = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.reply-area__textarea"))
        )
        reply.clear()
        reply.send_keys("自動化測試回覆用")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click()

        # 驗證
        time.sleep(2)
        if "自動化測試回覆用" in driver.page_source:
            print("\033[32m回覆成功\033[0m")
        else:
            print("\033[31m回覆失敗\033[0m")

        # 取消刪除
        time.sleep(2)
        forum_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//cgust-thread"))
        )
        for forum3 in forum_elements:
            title_element = forum3.find_element(By.XPATH, "//em[@class='thread__title ng-star-inserted']")
            if title_element.text == "自動化測試修改用":
                dot_button = forum3.find_element(By.XPATH, "//button[@class='mat-menu-trigger comment__header-btn comment__header-btn--web ng-star-inserted']//mat-icon[@aria-label='更多動作圖示']//*[name()='svg']")
                dot_button.click()
                time.sleep(2)
                delete_button = forum3.find_element(By.XPATH, "//button[contains(text(),'刪除')]")
                delete_button.click()
                break
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'取消')]"))
        ).click()
        
        # 驗證
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m取消刪除成功\033[0m")
        else:
            print("\033[31m取消刪除失敗\033[0m")   

        # 刪除
        time.sleep(2)
        forum_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//cgust-thread"))
        )
        for forum3 in forum_elements:
            title_element = forum3.find_element(By.XPATH, "//em[@class='thread__title ng-star-inserted']")
            if title_element.text == "自動化測試修改用":
                time.sleep(2)
                dot_button = forum3.find_element(By.XPATH, "//button[@class='mat-menu-trigger comment__header-btn comment__header-btn--web ng-star-inserted']//mat-icon[@aria-label='更多動作圖示']//*[name()='svg']")
                dot_button.click()
                time.sleep(2)
                delete_button = forum3.find_element(By.XPATH, "//button[contains(text(),'刪除')]")
                delete_button.click()
                break
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'確定')]"))
        ).click()

        # 驗證
        time.sleep(2)
        if "自動化測試修改用" not in driver.page_source:
            print("\033[32m刪除成功\033[0m")
        else:
            print("\033[31m刪除失敗\033[0m")   

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

        