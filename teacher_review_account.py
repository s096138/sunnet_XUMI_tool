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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from test_login import test_login
from teacher_enter import teacher_enter
import time

def login_for_course(driver, username, password, captcha, course_name):
    try:
        # 登入 yyytest
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "action__button-text"))
        )
        login_button.click()
        time.sleep(2)
        username_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'account'))
        )
        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        # captcha_input = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.ID, 'captcha'))
        # )
        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        
        time.sleep(2)
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        # captcha_input.clear()
        # captcha_input.send_keys(captcha)

        time.sleep(2)
        submit_button.click()
        print("使用學生帳號登入")

        # 搜尋課程
        time.sleep(2)
        search = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='您想學習什麼課程?']"))
        )
        search.clear()
        search.send_keys(course_name)
        search.send_keys(Keys.ENTER)

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='card__link']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='立即報名']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'正式生')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='mat-focus-indicator button--primary mat-button mat-button-base']"))
        ).click()
        time.sleep(2)

        if "您已完成課程報名" in driver.page_source:
            print("\033[32m報名課程成功\033[0m")
        else:
            print("\033[31m報名課程失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='confirm']"))
        ).click()
        
        # 回教師環境
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mat-focus-indicator.action__button.action__button--blue.action__button--vertical-center.mat-button.mat-button-base"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'登出')]"))
        ).click()
        time.sleep(2)
        test_login(driver)
        teacher_enter(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'審核學員')]"))
        ).click()

    except Exception as e:
        print(f"發生錯誤: {e}")

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def teacher_review_account(driver):
    try:
        print("測試：辦公室-人員管理-審核學員")
        menu_expanded(driver, "人員管理", "審核學員")
        time.sleep(2)
        if "同意修課" in driver.page_source:
            print("\033[32m進入審核學員成功\033[0m")
        else:
            print("\033[31m進入審核學員失敗\033[0m")
        
        # 無資料
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click()        
        driver.execute_script("rvAction(true);")  
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        if "請先選取要同意的人員" in alert_text:
            print("\033[32m未勾選人員不可同意\033[0m")
        else:
            print("\033[31m未勾選人員可以同意\033[0m")  
        alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click()        
        driver.execute_script("rvAction(false);")  
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        if "請先選取要不同意的人員" in alert_text:
            print("\033[32m未勾選人員不可不同意\033[0m")
        else:
            print("\033[31m未勾選人員可以不同意\033[0m")  
        alert.accept()
        time.sleep(2)
        
        # 登出
        driver.execute_script("logout();") 
        print("登出教師帳號") 
        login_for_course(driver, 'yyytest', 'A12345', '9453', '自動化測試主課程')

        # 不同意修課
        time.sleep(2)
        if "yyytest" in driver.page_source:
            print("\033[32m人員顯示於審核列表成功\033[0m")
        else:
            print("\033[31m人員顯示於審核列表失敗\033[0m") 
        time.sleep(2)          
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'審核')]"))
        ).click()
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn3"))
        ).click()        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click() 
        time.sleep(2)
        if "yyytest" in driver.page_source and "成功" in driver.page_source:
            print("\033[32m不同意修課成功\033[0m")
        else:
            print("\033[31m不同意修課失敗\033[0m")             
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btnReturn']"))
        ).click()

        # 驗證
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        ).click()
        time.sleep(2)
        if "yyytest" not in driver.page_source:
            print("\033[32m到課統計未顯示不通過人員成功\033[0m")
        else:
            print("\033[31m到課統計未顯示不通過人員失敗\033[0m")   
        
        # 登出
        driver.execute_script("logout();")  
        print("登出教師帳號")
        login_for_course(driver, 'yyytest', 'A12345', '9453', '自動化測試主課程')

        # 不同意修課
        time.sleep(2)
        if "yyytest" in driver.page_source:
            print("\033[32m人員顯示於審核列表成功\033[0m")
        else:
            print("\033[31m人員顯示於審核列表失敗\033[0m") 
        time.sleep(2)          
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'審核')]"))
        ).click()
        time.sleep(2)
        scroll_bottom(driver)       
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click() 
        time.sleep(2)
        if "yyytest" in driver.page_source and "成功" in driver.page_source:
            print("\033[32m同意修課成功\033[0m")
        else:
            print("\033[31m同意修課失敗\033[0m")             
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btnReturn']"))
        ).click()

        # 驗證
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        ).click()
        time.sleep(2)
        if "yyytest" in driver.page_source:
            print("\033[32m到課統計顯示通過人員成功\033[0m")
        else:
            print("\033[31m到課統計顯示通過人員失敗\033[0m")    

        # # 刪除
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'增刪學員')]"))
        # ).click()
        # time.sleep(2)
        # userlist = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        # )
        # userlist.clear()
        # userlist.send_keys("yyytest")
        # scroll_bottom(driver)
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='移除']"))
        # ).click()
        # time.sleep(2)  
        # add4 = False        
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "您確定要刪除嗎" in alert_text:
        #     alert.accept()
        #     if "移除" in driver.page_source and "確定" in driver.page_source:
        #         add4 = True
        # else:
        #     add4 = False
        #     time.sleep(5)
        #     alert.accept()        
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        # ).click()  
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        # ).click()
        # time.sleep(2)
        # select_element  = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        # )
        # select = Select(select_element)
        # select.select_by_visible_text("全部")
        # time.sleep(2) 
        # if "yyytest" not in driver.page_source and add4 == True:
        #     print("\033[32m移除學員成功\033[0m")
        # else:
        #     print("\033[31m移除學員失敗\033[0m")                 

        # # 另開視窗
        # time.sleep(10)
        # driver.execute_script("window.open('');")
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])
        # driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        # time.sleep(2)
        # if "自動化測試主課程" in driver.page_source:
        #     print("\033[32m寄出審核信成功\033[0m")
        # else:
        #     print("\033[31m寄出審核信失敗\033[0m")
        # driver.close()
        # driver.switch_to.window(windows[0])
        # time.sleep(2)       

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