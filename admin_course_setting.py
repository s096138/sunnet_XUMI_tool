from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pywinauto import Application
from datetime import datetime
import time
import random
import os
from dotenv import load_dotenv

def scroll_top(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,0);")
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

def admin_course_setting(driver):
    try:
        print("測試：管理者環境-課程管理-課程設定")  
        menu_expanded(driver, "課程管理", "課程設定")
        time.sleep(2)
        if "新增課程" in driver.page_source:
            print("\033[32m進入課程設定成功\033[0m")
        else:
            print("\033[31m進入課程設定失敗\033[0m")

        # 新增課程
        new = False
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_addCourse'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試用")
        scroll_bottom(driver)
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.click()
        point.send_keys("2")
        time.sleep(2)
        driver.execute_script("save_step(1)") 
        time.sleep(2)     
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增課程成功，繼續設定其他內容。" in alert_text:
            new = True
            alert.accept()
        else:
            new = False
            alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source and new == True:
            print("\033[32m新增課程成功\033[0m")
        else:
            print("\033[31m新增課程失敗\033[0m")

        # 空白搜尋
        load_dotenv()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()
        time.sleep(2)
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        if course_name in driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")

        # 關鍵字搜尋
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("自動化測試主課程")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()
        time.sleep(2)
        if "1-1 筆 (共 1 筆)" in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")

        # 加入群組
        add = False
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkAll'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()      
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_submit'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請勾選群組" in alert_text:
            print("\033[32m未勾選群組不能加入群組\033[0m")
            alert.accept()
        else:
            print("\033[31m未勾選群組可以加入群組\033[0m")
            alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 10).until( 
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'圖書館系')]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_submit'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        if "課程加入群組成功" in alert_text:
            add = True
            alert.accept()
        else:
            add = False
            alert.accept()

        # 檢視群組
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='圖書館系']"))
        ).click() 
        time.sleep(2)
        if "自動化測試用" in driver.page_source and add == True:
            print("\033[32m加入群組成功\033[0m")
        else:
            print("\033[31m加入群組失敗\033[0m")

        # 寄給群組
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkAll'))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_mail'))
        ).click()      
        time.sleep(2)
        WebDriverWait(driver, 10).until( 
            EC.element_to_be_clickable((By.XPATH, '//input[@id="student"]')) #取消正式生
        ).click()
        WebDriverWait(driver, 10).until( 
            EC.element_to_be_clickable((By.XPATH, '//input[@id="assistant"]')) #取消助教
        ).click()
        WebDriverWait(driver, 10).until( 
            EC.element_to_be_clickable((By.XPATH, '//input[@id="instructor"]')) #取消講師
        ).click()
        WebDriverWait(driver, 10).until( 
            EC.element_to_be_clickable((By.XPATH, '//input[@id="teacher"]')) #取消教師
        ).click()
        time.sleep(2)
        to = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'to'))
        )
        to.click()
        to.send_keys(os.getenv("TEST_EMAIL"))
        time.sleep(2)
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'send_mail'))
        ).click()       
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請輸入主旨" in alert_text:
            print("\033[32m未輸入主旨不能發送信件\033[0m")
            alert.accept()
        else:
            print("\033[31m未輸入主旨可以發送信件\033[0m")
            alert.accept()
        time.sleep(2)  
        title = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'subject'))
        )    
        title.click()
        title.send_keys("自動化測試用")  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'send_mail'))
        ).click()  
        time.sleep(2)     
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請輸入內容" in alert_text:
            print("\033[32m未輸入內容不能發送信件\033[0m")
            alert.accept()
        else:
            print("\033[31m未輸入內容可以發送信件\033[0m")
            alert.accept()
        time.sleep(2)
        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用</p>'", editable_body)
        # driver.switch_to.default_content()
        time.sleep(2)          
        photo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"更多附檔")]'))
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
            EC.element_to_be_clickable((By.ID, 'send_mail'))
        ).click()  
        time.sleep(2) 
        if "已發送" in driver.page_source:
            print("\033[32m寄給人員成功\033[0m")
        else:
            print("\033[31m寄給人員失敗\033[0m") 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"確定")]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()             
        
        # 匯出人員
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='圖書館系']"))
        ).click() 
        time.sleep(2)   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_account_mail'))
        ).click()  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_choose_submit'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請勾選群組" in alert_text:
            print("\033[32m未勾選群組不能匯出\033[0m")
            alert.accept()
        else:
            print("\033[31m未勾選群組可以匯出\033[0m")
            alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='groups-choose-modal']//label[contains(text(), '圖書館系')]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_choose_submit'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_choose_confirm'))
        ).click() 
        time.sleep(2)   
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請輸入 email" in alert_text:
            print("\033[32m未輸入email不能匯出\033[0m")
            alert.accept()
        else:
            print("\033[31m未輸入email可以匯出\033[0m")
            alert.accept()            
        time.sleep(2)   
        mail = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'send_email'))
        )
        mail.click()
        mail.send_keys(os.getenv("TEST_EMAIL"))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_choose_confirm'))
        ).click() 
        time.sleep(2)
        if "已發送" in driver.page_source:
            print("\033[32m匯出人員成功\033[0m")
        else:
            print("\033[31m匯出人員失敗\033[0m") 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="modal_result"]/div/div/div[3]/button'))
        ).click() 

        # 每頁數量 
        time.sleep(2)
        page_num = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'page_num'))
        )
        page_num.click() 
        select = Select(page_num)
        options = {"每頁10筆":10, "每頁20筆":20, "每頁50筆":50}
        random_option_text = random.choice(list(options.keys()))
        random_option_number = options[random_option_text]
        select.select_by_value(str(random_option_number))
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
        tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        print(len(tr_elements))
        if len(tr_elements) == random_option_number:
            print("\033[32m每頁顯示數量正確\033[0m")
        else:
            print("\033[31m每頁顯示數量不正確\033[0m")   

        # 刪除課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='圖書館系']"))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkAll'))
        ).click()     
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_delCourse'))
        ).click()
        time.sleep(2) 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "你確定要刪除嗎？" in alert_text:
            alert.accept()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "刪除成功！" in alert_text:
                print("\033[32m刪除課程成功\033[0m")
                alert.accept()               
            else:
                print("\033[32m刪除課程失敗\033[0m")
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