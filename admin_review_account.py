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
    WebDriverException,
    UnexpectedAlertPresentException
)
from menu_expanded import menu_expanded
from selenium.webdriver.common.alert import Alert
from test_login import test_login
from admin_enter import admin_enter
import time
import os
from dotenv import load_dotenv

def check_mailinator_inbox(email_prefix, driver):
    """
    檢查 Mailinator 是否收到指定前綴的郵件。
    
    :param email_prefix: 用於生成臨時郵箱的前綴部分，"yyytest"。
    :param driver: 已初始化的 WebDriver 實例。
    :return: 返回 True 表示郵件已經收到，返回 False 表示郵件未收到。
    """
    # 打開 Mailinator 網站，檢查是否收到了郵件
    driver.get("https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
    
    time.sleep(2)
    if "註冊成功通知信" in driver.page_source:
        print("\033[32m已收到註冊信件\033[0m")    
    else:
        print("\033[31m未收到註冊信件\033[0m")

def admin_review_account(driver):
    try:
        print("測試：管理者環境-帳號管理-審核帳號")
        time.sleep(2)
        menu_expanded(driver, "帳號管理", "審核帳號")
        time.sleep(2)
        if "註冊時間" in driver.page_source:
            print("\033[32m進入審核帳號成功\033[0m")
        else:
            print("\033[31m進入審核帳號失敗\033[0m")
        time.sleep(5)
        if "沒有需要審核的帳號" in driver.page_source:
            print("\033[32m目前沒有需要審核的帳號\033[0m")
        else:
            print("\033[32m目前有需要審核的帳號\033[0m")
            keyword = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="keyword"]'))
            )
            keyword.click()
            keyword.send_keys("05")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@id="search_btn"]'))
            ).click()
            time.sleep(2)
            if "1-1 筆" in driver.page_source:
                print("\033[32m關鍵字搜尋成功\033[0m")
            else:
                print("\033[31m關鍵字搜尋失敗\033[0m")
        time.sleep(2)
        driver.execute_script("logout()") #登出
        time.sleep(2)
        WebDriverWait(driver, 10).until(  #登入
            EC.element_to_be_clickable((By.XPATH, '/html/body/cgust-root/cgust-header/header/div/nav[1]/ul/li[2]/div/button'))
        ).click()

        # 註冊
        load_dotenv()
        time.sleep(2)
        WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-dialog-0"]/cgust-dialog-login/main/form/div[2]/button[2]'))
        ).click()
        account = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="account"]'))
        )
        account.click()
        account.send_keys("yyy000")
        pw1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="register-password"]'))
        )
        pw1.click()
        pw1.send_keys("A12345")
        pw2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="confirm-password"]'))
        )
        pw2.click()
        pw2.send_keys("A12345")
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]'))
        )
        name.click()
        name.send_keys("yyy000")
        email = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))
        )
        email.click()
        email.send_keys(os.getenv("TEST_EMAIL"))
        # 10秒自己填驗證碼喔
        time.sleep(10)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"送出")]'))
        ).click()
        time.sleep(2)    
        if " 表單送出成功" in driver.page_source:
            print("\033[32m註冊成功\033[0m") 
        else:
            print("\033[31m註冊失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="confirm"]'))
        ).click()

        # 回 審核帳號
        time.sleep(2)
        load_dotenv()
        base_url = os.getenv('BASE_URL')
        driver.get(base_url)
        time.sleep(2)
        test_login(driver)
        admin_enter(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sldebar-nav"]/li[1]/div'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[3]/a'))
        ).click()
        time.sleep(5)
        if "yyy000" in driver.page_source:
            print("\033[32m審核帳號顯示成功\033[0m")
        else:
            print("\033[31m審核帳號顯示失敗\033[0m")

        # 不通過
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/input'))
        ).click()               
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="btn_notpass"]'))
        ).click() 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除這些帳號嗎? " in alert_text:
            print("\033[32m審核不通過\033[0m")
            alert.accept()
            time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"取消")]'))
        ).click()            
            
        # 通過
        WebDriverWait(driver, 10).until(  #取消全選
            EC.element_to_be_clickable((By.XPATH, '//input[@id="checkAll"]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="yyy000"]'))
        ).click()               
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="btn_pass"]'))
        ).click()   
        time.sleep(2)
        if "沒有需要審核的帳號" in driver.page_source:
            print("\033[32m審核已通過\033[0m")
        else:
            print("\033[31m審核未通過\033[0m")

        # 查看審核信
        time.sleep(2) 
        check_mailinator_inbox("yyytest", driver)
        time.sleep(2)
        load_dotenv()
        base_url = os.getenv('BASE_URL')
        driver.get(base_url)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/cgust-root/cgust-header/header/div/nav[1]/ul/li[2]/div/ul/li[8]/a"))
        ).click()
            
        # 嘗試登入
        time.sleep(2)
        WebDriverWait(driver, 10).until(  #登入
            EC.element_to_be_clickable((By.XPATH, '/html/body/cgust-root/cgust-header/header/div/nav[1]/ul/li[2]/div/button'))
        ).click()
        ac = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, '//input[@id="account"]'))
        )
        ac.click()
        ac.send_keys("yyy000")
        pw = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))
        )
        pw.click()
        pw.send_keys("A12345")
        ca = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, '//input[@id="captcha"]'))
        )
        ca.click()
        ca.send_keys("9453")            
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()
        time.sleep(2)
        if "登入失敗" not in driver.page_source:
            print("\033[32m已審核過帳號登入成功\033[0m")
        else:
            print("\033[31m已審核過帳號登入失敗\033[0m")

        # 復原
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mat-focus-indicator.action__button.action__button--blue.action__button--vertical-center.mat-button.mat-button-base"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'登出')]"))
        ).click()
        time.sleep(2)
        test_login(driver)
        admin_enter(driver)

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