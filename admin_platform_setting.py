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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from pywinauto import Application
from selenium.webdriver.common.action_chains import ActionChains
from test_login import test_login
from admin_enter import admin_enter
from admin_management_center import admin_management_center
from course_enter import course_enter1
from teacher_enter import teacher_enter
import time
import hashlib
import requests
from PIL import Image
from io import BytesIO
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

def get_image_hash(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        img = Image.open(BytesIO(response.content))
        img_hash = hashlib.md5(img.tobytes()).hexdigest()
        return img_hash
    except requests.exceptions.RequestException as e:
        print(f"請求錯誤: {e}")
    except IOError as e:
        print(f"圖片讀取錯誤: {e}")
    return None
    
def admin_platform_setting(driver):
    try:
        print("測試：管理者環境-平台管理-平台設定")
        menu_expanded(driver, "平台管理", "平台設定")
        time.sleep(2)
        if "平台名稱" in driver.page_source:
            print("\033[32m進入平台設定成功\033[0m")
        else:
            print("\033[31m進入平台設定失敗\033[0m")

        # # 平台設定
        # time.sleep(2) 
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='平台設定']"))
        # ).click() 

        # # 平台名稱
        # time.sleep(2)
        # name = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@name='schname']"))
        # )
        # name.clear()
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # if "名稱請務必填寫" in driver.page_source:
        #     print("\033[32m未填平台名稱不可儲存\033[0m")
        # else:
        #     print("\033[31m未填平台名稱可以儲存\033[0m")
        # time.sleep(2)
        # name = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@name='schname']"))
        # )    
        # name.send_keys("X-UMI")  

        # # 管理員信箱
        # time.sleep(2)
        # mail = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@name='school_mail']"))
        # )
        # mail.clear()
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # if "管理員信箱請務必填寫" in driver.page_source:
        #     print("\033[32m未填管理員信箱不可儲存\033[0m")
        # else:
        #     print("\033[31m未填管理員信箱可以儲存\033[0m")
        # time.sleep(2)
        # mail = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@name='school_mail']"))
        # )    
        # mail.send_keys("jeff@sun.net.tw")  

        # # 主色系
        # time.sleep(2)
        # maincolor = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='main_rgb_color']"))
        # )
        # mainvalue = maincolor.get_attribute("value")
        # maincolor.clear()
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # if "主色系務必填寫" in driver.page_source:
        #     print("\033[32m未填主色系不可儲存\033[0m")
        # else:
        #     print("\033[31m未填主色系可以儲存\033[0m")
        # time.sleep(2)
        # maincolor = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='main_rgb_color']"))
        # )    
        # maincolor.send_keys(mainvalue)    

        # # 次色系
        # time.sleep(2)
        # secondcolor = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='second_rgb_color']"))
        # )
        # secondvalue = secondcolor.get_attribute("value")
        # secondcolor.clear()
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # if "次色系務必填寫" in driver.page_source:
        #     print("\033[32m未填次色系不可儲存\033[0m")
        # else:
        #     print("\033[31m未填次色系可以儲存\033[0m")
        # time.sleep(2)
        # secondcolor = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='second_rgb_color']"))
        # )    
        # secondcolor.send_keys(secondvalue)

        # # LOGO-初始
        # logo_initial_favicon = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//img[@id='logo_preview']")))
        # initial_logo_src = logo_initial_favicon.get_attribute('src')
        # if initial_logo_src:
        #     initial_logo_hash = get_image_hash(initial_logo_src)
        #     print(f"初始 logo hash: {initial_logo_hash}")
        # else:
        #     print("無法獲取初始 logo hash")
        #     initial_logo_hash = None
        # time.sleep(2)
        # last_height = driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2) 
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'uploadLogo'))
        # ).click()
        # time.sleep(2)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\蛙蛙.jpg") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        # time.sleep(5)

        # # 確定
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # assert alert.text == "更新成功！"
        # alert.accept()

        # # LOGO-新的
        # new_logo_element = driver.find_element(By.XPATH, "//img[@id='logo_preview']")
        # new_logo_src = new_logo_element.get_attribute('src')
        # if new_logo_src:
        #     new_logo_hash = get_image_hash(new_logo_src)
        #     print(f"新的 logo hash: {new_logo_hash}")
        # else:
        #     print("無法獲取新的 logo hash")
        #     new_logo_hash = None
        # if initial_logo_hash is not None and new_logo_hash is not None:
        #     if initial_logo_hash != new_logo_hash:
        #         print("\033[32m更換logo成功\033[0m")
        #     else:
        #         print("\033[31m更換logo失敗\033[0m")
        #         time.sleep(2)

        # # ICON-初始
        # icon_initial_favicon = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//link[@rel='icon']"))).get_attribute('href')
        # initial_favicon_hash = get_image_hash(icon_initial_favicon)
        # if initial_favicon_hash:
        #     print(f"初始 icon hash: {initial_favicon_hash}")
        # else:
        #     print("無法獲取初始 icon hash")
        # time.sleep(2)
        # last_height = driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2) 
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'uploadIcon'))
        # ).click()
        # time.sleep(2)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\趴八.ico") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        # time.sleep(5)

        # # 確定
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "更新成功！"  in alert_text:
        #     alert.accept()
        # else:
        #     print("未更換圖片")   

        # # ICON-新的
        # time.sleep(2)
        # icon_new_favicon = driver.find_element(By.XPATH, "//link[@rel='icon']").get_attribute('href')
        # new_favicon_hash = get_image_hash(icon_new_favicon)
        # if new_favicon_hash:
        #     print(f"新的 icon hash: {new_favicon_hash}")
        # else:
        #     print("無法獲取新的 icon hash")

        # if initial_favicon_hash != new_favicon_hash:
        #     print("\033[32m更換icon成功\033[0m")
        # else:
        #     print("\033[31m更換icon失敗\033[0m")

        # # 改回來
        # time.sleep(5)
        # last_height = driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2) 
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'uploadLogo'))
        # ).click()
        # time.sleep(2)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\xumi@1x.png") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        # time.sleep(5)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'uploadIcon'))
        # ).click()
        # time.sleep(2)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\icon.ico") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        # time.sleep(5)

        # driver.execute_script("checkData()")
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "更新成功！"  in alert_text: 
        #     alert.accept()

        # # 自由註冊
        # time.sleep(5)
        # can_reg_n = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, 'canRegN'))
        # )
        # driver.execute_script("arguments[0].checked = true;", can_reg_n) #不允許
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text 
        # if "更新成功！"  in alert_text:
        #     print("\033[32m設定自由註冊成功\033[0m")
        # else:
        #     print("\033[31m設定自由註冊失敗\033[0m")            
        # alert.accept()
        # time.sleep(2)
        # driver.execute_script("logout()") #登出
        # WebDriverWait(driver, 10).until(  #登入
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/cgust-root/cgust-header/header/div/nav[1]/ul/li[2]/div/button'))
        # ).click()
        # time.sleep(2)
        # if "註冊" not in driver.page_source:
        #     print("\033[32m自由註冊更改成功\033[0m")
        # else:
        #     print("\033[31m自由註冊更改失敗\033[0m")

        # # 復原
        # time.sleep(2)
        # load_dotenv()
        # base_url = os.getenv('BASE_URL')
        # driver.get(base_url)
        # time.sleep(2)
        # test_login(driver)
        # admin_enter(driver)
        # admin_management_center(driver)
        # time.sleep(5)
        # can_reg_c = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, 'canRegC'))
        # )
        # driver.execute_script("arguments[0].checked = true;", can_reg_c) #允許但須同意
        # driver.execute_script("checkData()")
        # time.sleep(2)
        # if "更新成功！"  in alert_text: 
        #     alert.accept()  

        # 頁尾資訊
        time.sleep(2) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='頁尾資訊']"))
        ).click() 
        time.sleep(2)
        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='Big5']"))
        )
        old_text = textarea.get_attribute('value')
        textarea.clear()
        textarea.send_keys("自動化測試用")
        time.sleep(2)
        driver.execute_script("checkData()")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text 
        time.sleep(2)
        if "更新成功！" in alert_text:
            print("\033[32m設定頁尾資訊成功\033[0m")
        else:
            print("\033[31m設定頁尾資訊失敗\033[0m")            
        alert.accept()

        # 檔案限制設定
        time.sleep(2) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='檔案限制設定']"))
        ).click()         
        teacher = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='teacher_upload_quota']"))
        )
        teacher.clear()
        teacher.send_keys("61")
        student = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='student_upload_quota']"))
        )
        student.clear()
        student.send_keys("62")
        time.sleep(2)
        driver.execute_script("checkData()")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text 
        time.sleep(2)
        if "更新成功！" in alert_text:
            print("\033[32m設定檔案限制成功\033[0m")
        else:
            print("\033[31m設定檔案限制失敗\033[0m")            
        alert.accept()    

        # 驗證
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='數位學習平台logo']"))
        ).click()     
        time.sleep(2)
        scroll_bottom(driver) 
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m驗證頁尾資訊成功\033[0m")
        else:
            print("\033[31m驗證頁尾資訊失敗\033[0m") 

        time.sleep(2)
        scroll_top(driver)
        course_enter1(driver)
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//div[@role='tab' and contains(., '討論區')]"))
        ).click()        
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'發表主題')]"))
        ).click()
        time.sleep(2)
        if " 單一上傳檔案尺寸 (size) 不得超過 62MB，總檔案大小不得超過 62MB。 " in driver.page_source:
            print("\033[32m驗證學生環境檔案限制成功\033[0m")
        else:
            print("\033[31m驗證學生環境檔案限制失敗\033[0m") 
        
        time.sleep(2)
        scroll_top(driver)
        teacher_enter(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'教材檔案管理')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab04"))
        ).click()
        time.sleep(2)
        if "61M" in driver.page_source:
            print("\033[32m驗證教師環境檔案限制成功\033[0m")
        else:
            print("\033[31m驗證教師環境檔案限制失敗\033[0m")

        # 返回
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='數位學習平台logo']"))
        ).click()        
        admin_enter(driver)
        time.sleep(2)
        admin_management_center(driver)
        time.sleep(2)

        # 復原
        time.sleep(2) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='頁尾資訊']"))
        ).click() 
        time.sleep(2)
        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='Big5']"))
        )
        textarea.clear()
        textarea.send_keys(old_text)
        time.sleep(2)
        driver.execute_script("checkData()")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text 
        time.sleep(2)
        if "更新成功！"  in alert_text:
            print("\033[32m復原頁尾資訊成功\033[0m")
        else:
            print("\033[31m復原頁尾資訊失敗\033[0m")            
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
