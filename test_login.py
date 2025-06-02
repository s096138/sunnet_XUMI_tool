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
from selenium_driver import initialize_driver
from sql_injection_payloads import sql_injection_payloads
from dotenv import load_dotenv
import os
import time

def test_login(driver):
    driver = initialize_driver()
    try:
        print("測試：首頁-登入")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        time.sleep(2)
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "action__button-text"))
        )
        login_button.click()
        time.sleep(2)
        username_input = driver.find_element(By.ID, 'account')
        password_input = driver.find_element(By.ID, 'password')
        # captcha_input = driver.find_element(By.XPATH, '//input[@id="captcha"]')
        submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')  

        # # 執行測試
        # for payload in sql_injection_payloads:
        #     print(f'Testing payload: {payload}')
    
        #     # 清除輸入框並輸入 SQL 注入載荷
        #     username_input.clear()
        #     username_input.send_keys("joy09")
        #     password_input.clear()
        #     password_input.send_keys(payload)  
        #     captcha_input.send_keys("9453")
        #     # 送出
        #     submit_button.click()
        #     time.sleep(2)
    
        #     # 檢查回應是否有異常（這裡需要根據具體情況調整）
        #     try:
        #         alert = driver.switch_to.alert
        #         print("\033[31m非正常回應\033[0m")
        #         alert.accept()  
        #     except:
        #         if "登入失敗" in driver.page_source:
        #             print("\033[32m正常回應\033[0m")
        #             WebDriverWait(driver, 20).until(
        #                 EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="confirm"]'))
        #             ).click()
        #         else:
        #             print("\033[31m非正常回應\033[0m")
        
        # 取環境變數
        load_dotenv()
        username = os.getenv('XUMI_USERNAME')
        password = os.getenv('XUMI_PASSWORD')

        password_input.clear()
        password_input.send_keys(password)
        print('\033[32m輸入密碼成功\033[0m')

        submit_button.click()
        print('\033[32m未輸入帳號不可進行登入\033[0m')
        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//mark[@class='mark mark--invalid-message ng-star-inserted' and contains(text(),'此欄必填')]"))
            )
            print('\033[32m帳號欄位必填訊息顯示正確\033[0m')
        except TimeoutException:
            print('\033[31m帳號欄位必填訊息未顯示\033[0m')
        username_input.clear()
        username_input.send_keys(username)
        print('\033[32m輸入帳號成功\033[0m')
        time.sleep(2)

        # captcha_input.send_keys('9453')
        # print('\033[32m輸入驗證碼成功\033[0m')
    
        # close_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="關閉"]'))
        # )
        # close_button.click()
        
        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit_button.click()
        print('\033[32m登入成功\033[0m')
   
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
