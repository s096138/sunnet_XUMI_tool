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
import os
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

# def enter(driver):
#         time.sleep(2)
#         WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
#         ).click()
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[span/text()='我的課表']"))
#         ).click()
#         WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'課程複製精靈')]"))
#         ).click()
#         print('進入學習環境')
#         time.sleep(2)

def course_exam(driver):
    try:
        # enter(driver)
        print("測試：學習環境-測驗")
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//div[@class='mat-tab-label-content'][contains(text(),'測驗')]"))
        ).click()
        time.sleep(2)
        if "測驗一" in driver.page_source:
            print("\033[32m進入測驗成功\033[0m")
        else:
            print("\033[31m進入測驗失敗\033[0m")

        # 繳交作業
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//p[@class='asg-header__title'][contains(text(),'測驗一')])[1]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'繳交測驗')]"))
        ).click()
        time.sleep(2)
        if "測驗名稱" in driver.page_source and "通過標準" in driver.page_source:
            print("\033[32m觀看測驗說明成功\033[0m")
        else:
            print("\033[31m觀看測驗說明失敗\033[0m")
        
        # 開始作答
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'開始作答')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
        ).click()

        # 題目圖片
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='蛙蛙.jpg']"))
            )
            print("\033[32m題目圖片顯示成功\033[0m")
        except:
            print("\033[31m題目圖片顯示失敗\033[0m")
            
        # 1.
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mock-radio'])[1]"))
        ).click()    

        # 2.
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mock-radio'])[3]"))
        ).click()

        # 3.
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mock-checkbox'])[1]"))
        ).click()

        # 確定送出
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定送出')]"))
        ).click()

        # 驗證
        time.sleep(2)
        if "繳交成功" in driver.page_source:
            print("\033[32m繳交測驗成功\033[0m")
        else:
            print("\033[31m繳交測驗失敗\033[0m") 
        time.sleep(2)      
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-button-wrapper' and contains(text(),'關閉')]"))
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