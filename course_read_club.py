from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from selenium.webdriver.common.action_chains import ActionChains
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

def course_read_club(driver):
    try:
        print("測試：學習環境-讀書會")
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "(//div[@class='mat-tab-label-content'][contains(text(),'讀書會')])[1]"))
        ).click()
        time.sleep(5)
        if "讀書會會會" in driver.page_source:
            print("\033[32m進入讀書會成功\033[0m")
        else:
            print("\033[31m進入讀書會失敗\033[0m")

        # 進入設定
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//button[contains(text(),'進入設定')]"))
        ).click()
        time.sleep(2)

        # 檔案1
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//button[contains(text(),'上傳檔案')]"))
        ).click()
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//input[@id='title-for-files']"))
        )
        title.clear()   
        title.send_keys("自動化測試1")    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選擇檔案')]"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\xumi@1x.png") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 檔案2
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//button[contains(text(),'上傳檔案')]"))
        ).click()
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//input[@id='title-for-files']"))
        )
        title.clear()   
        title.send_keys("自動化測試2")    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選擇檔案')]"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\202410旭航v4.mp4") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 檔案3 (隱藏)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//button[contains(text(),'上傳檔案')]"))
        ).click()
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//input[@id='title-for-files']"))
        )
        title.clear()   
        title.send_keys("自動化測試3")    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選擇檔案')]"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\114年辦公日曆表.pdf") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'隱藏')]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 驗證檔案上傳
        time.sleep(2)
        if "自動化測試1" in driver.page_source and "自動化測試2" in driver.page_source and "自動化測試3" in driver.page_source:
            print("\033[32m上傳檔案成功\033[0m")
        else:
            print("\033[31m上傳檔案失敗\033[0m")

        # 驗證switch狀態
        time.sleep(2)
        switch1 = driver.find_element(By.ID, "mat-slide-toggle-1-input")
        switch2 = driver.find_element(By.ID, "mat-slide-toggle-2-input")
        switch3 = driver.find_element(By.ID, "mat-slide-toggle-3-input")
        is_checked1 = switch1.get_attribute("aria-checked") == "true"
        is_checked2 = switch2.get_attribute("aria-checked") == "true"
        is_checked3 = switch3.get_attribute("aria-checked") == "false"
        time.sleep(2)
        if is_checked1 and is_checked2 and is_checked3:
            print("\033[32mswitch切換狀態成功\033[0m")
        else:
            print("\033[31mswitch切換狀態失敗\033[0m")

        # 回列表 進入討論
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
        ).click()
        time.sleep(2)  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-tab-body//button[2]"))
        ).click()  

        # 讀書會
        time.sleep(2)
        if "暫停畫面" in driver.page_source:
            print("\033[32m進入討論成功\033[0m")
        else:
            print("\033[31m進入討論失敗\033[0m")

        # # 投影區
        # driver.switch_to.frame(0)
        # time.sleep(2)
        # if "交通部中央氣象署" in driver.page_source:
        #     print("\033[32m投影區顯示成功\033[0m")
        # else:
        #     print("\033[31m投影區顯示失敗\033[0m")
        # # driver.switch_to.default_content()

        # 節點
        time.sleep(2)
        if "自動化測試1" in driver.page_source and "自動化測試2" in driver.page_source and "自動化測試3" not in driver.page_source:
            print("\033[32m檔案節點顯示成功\033[0m")
        else:
            print("\033[31m檔案節點顯示失敗\033[0m")        
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), '自動化測試1')]"))
        ).click()         
        time.sleep(2)
        image_element1 = driver.find_element(By.XPATH, "//img[@alt='undefined']")
        image_src1 = image_element1.get_attribute("src")
        if ".png" in image_src1:
            print("\033[32m點擊節點顯示成功\033[0m")
        else:
            print("\033[31m點擊節點顯示失敗\033[0m")

        # 回列表
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回到列表')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'進入設定')]"))
        ).click()

        # 編輯
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[7]"))
        ).click()
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//input[@id='title-for-files']"))
        )
        title.clear()   
        title.send_keys("自動化測試123")  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選擇檔案')]"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 回列表 進入討論
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
        ).click()
        time.sleep(2)  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-tab-body//button[2]"))
        ).click()  

        # 讀書會
        time.sleep(2)
        if "自動化測試123" in driver.page_source:
            print("\033[32m編輯檔案名稱成功\033[0m")
        else:
            print("\033[31m編輯檔案名稱失敗\033[0m")  
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), '自動化測試123')]"))
        ).click()         
        time.sleep(2)
        image_element2 = driver.find_element(By.XPATH, "//img[@alt='undefined']")
        image_src2 = image_element2.get_attribute("src")
        if image_src1 != image_src2:
            print("\033[32m編輯檔案節點顯示成功\033[0m")
        else:
            print("\033[31m編輯檔案節點顯示失敗\033[0m")

        # 回列表
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回到列表')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'進入設定')]"))
        ).click()

        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[6]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[8]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='note__icon-action note__remove']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
        ).click()
        time.sleep(2)
        if "自動化測試123" not in driver.page_source and "自動化測試2" not in driver.page_source and "自動化測試3" not in driver.page_source:
            print("\033[32m刪除檔案成功\033[0m")
        else:
            print("\033[31m刪除檔案失敗\033[0m")  

        # 回列表
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
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