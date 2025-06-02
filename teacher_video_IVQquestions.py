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
from teacher_enter import teacher_enter
from selenium_driver import initialize_driver
import time
import os
from dotenv import load_dotenv

load_dotenv()

def scroll_top(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def teacher_video_IVQquestions(driver):
    try:
        print("測試：辦公室-課程管理-全能影像轉譯(IVQ題庫)")
        menu_expanded(driver, "課程管理", "全能影像轉譯")
        time.sleep(2)
        if "讓備課更輕鬆" in driver.page_source:
            print("\033[31m影片列表沒有影片可供測試\033[0m")
            return
        else:
            pass

        # IVQ設定
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@id='go#202410旭航v4.mp4']"))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'IVQ題庫')])[1]"))
        ).click()
        time.sleep(2) 
        if driver.page_source.count("未生成字幕") == 2:
            print("\033[31m未生成字幕 無法產生IVQ\033[0m")
        elif driver.page_source.count("自動生成題目") == 2:
            print("\033[32m進入全能影像轉譯(IVQ題庫)成功\033[0m")
        else:
            print("\033[31m進入全能影像轉譯(IVQ題庫)失敗\033[0m") 
        time.sleep(2)
        if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "itemsCount"))
        ).text == "0":
            pass
        else:
            print("先刪除現有題目 避免重複建立")
            delete_elements = driver.find_elements(By.XPATH, "//span[contains(text(),'delete')]")
            count = len(delete_elements)
            for i in range(count):
                delete_elements[i].click()
                time.sleep(2)
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                alert = driver.switch_to.alert
                alert.accept()

        # 自動生成題目
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='newItem_AI']"))
        ).click() 
        scroll_bottom(driver)
        time.sleep(2)
        single = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='single_num']"))
        )
        single.clear()
        single.send_keys("1")
        yn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='YN_num']"))
        )
        yn.clear()
        yn.send_keys("1")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm_button']"))
        ).click() 
        time.sleep(15) # 等待生成
        scroll_bottom(driver)
        if driver.page_source.count("題型:單選") == 2 and driver.page_source.count("題型:是非") == 2:
            print("\033[32m生成題型與題數成功\033[0m")
        else:
            print("\033[31m生成題型與題數失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='formItem1'] button:nth-child(2)"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-wm-purple'][contains(text(),'要')]"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()        
        time.sleep(2)
        if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "itemsCount"))
        ).text == "2":
            print("\033[32m自動建立題目成功\033[0m")
        else:
            print("\033[31m自動建立題目失敗\033[0m")

        # 新增題目
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='newItem']"))
        ).click() 
        scroll_bottom(driver)
        time.sleep(2)
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='subject']"))
        )
        subject.send_keys("自動化測試用")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='material-icons-outlined wm-cursor-pointer addoption']"))
        ).click() 
        time.sleep(2)
        option1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//textarea[@placeholder='請輸入選項...'])[1]"))
        )
        option1.send_keys("自動化測試A")
        option2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//textarea[@placeholder='請輸入選項...'])[2]"))
        )
        option2.send_keys("自動化測試B")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "itemsCount"))
        ).text == "3" and "自動化測試用" in driver.page_source and "自動化測試A" in driver.page_source and "自動化測試B" in driver.page_source:
            print("\033[32m手動建立題目成功\033[0m")
        else:
            print("\033[31m手動建立題目失敗\033[0m")

        # 編輯題目
        scroll_top(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'border_color')])[1]"))
        ).click() 
        time.sleep(2)
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='subject']"))
        )
        subject.clear()
        subject.send_keys("自動化測試修改用")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "itemsCount"))
        ).text == "3" and "自動化測試修改用" in driver.page_source:
            print("\033[32m編輯題目成功\033[0m")
        else:
            print("\033[31m編輯題目失敗\033[0m")

        # 標籤
        scroll_top(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'全能影像轉譯')]"))
        ).click()
        time.sleep(2)
        label = driver.find_element(By.XPATH, "//span[contains(text(),'IVQ')]").get_attribute("class")   
        if "green-label" in label:
            print("\033[32m標籤顏色顯示正確\033[0m")
        else:
            print("\033[31m標籤顏色顯示錯誤\033[0m")
        time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//img[@id='go#202410旭航v4.mp4']"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[@id='bank-tab']"))
        # ).click()   

        # 前台驗證
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='btnGo']"))
        ).click()

        # 點擊影片
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'202410旭航v4')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//vm-control[contains(@class, 'vm-control')]//vm-icon"))
        ).click()

        # 作答IVQ
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'自動化測試B')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出作答')]"))
        ).click()

        time.sleep(2)
        if "再次作答" in driver.page_source:
            print("\033[32mIVQ作答錯誤成功\033[0m")
        else:
            print("\033[31mIVQ作答錯誤失敗\033[0m")

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'自動化測試A')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'再次作答')]"))
        ).click()

        time.sleep(2)
        if "繼續觀看" in driver.page_source:
            print("\033[32mIVQ作答正確成功\033[0m")
        else:
            print("\033[31mIVQ作答正確失敗\033[0m")

        # 返回全能影像轉譯
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        time.sleep(2)
        teacher_enter(driver)
        time.sleep(2)
        menu_expanded(driver, "課程管理", "全能影像轉譯")
        time.sleep(2)        

        # # 刪除題目
        # time.sleep(2)
        # scroll_top(driver)
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'delete')])[1]"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.accept()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.accept()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'delete')])[1]"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.accept()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.accept()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'delete')])[1]"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.accept()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.accept()
        # time.sleep(2)
        # if WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "itemsCount"))
        # ).text == "0":
        #     print("\033[32m刪除題目成功\033[0m")
        # else:
        #     print("\033[31m刪除題目失敗\033[0m")

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