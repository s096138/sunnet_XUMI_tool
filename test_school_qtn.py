from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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
from dotenv import load_dotenv

# 滾動到底部
def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def test_school_qtn(driver):
    try:
        print("測試：首頁-會員專區-問卷調查")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[span/text()='問卷調查']"))
        ).click()
        time.sleep(2)
        if "問卷調查" in driver.page_source:
            print("\033[32m進入問卷調查成功\033[0m")
        else:
            print("\033[31m進入問卷調查失敗\033[0m")

        # 填寫問卷
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'自動化測試用問卷')]"))
        ).click()
        time.sleep(2)
        if "問卷說明" in driver.page_source:
            print("\033[32m問卷說明顯示成功\033[0m")
        else:
            print("\033[31m問卷說明顯示失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'開始作答')]"))
        ).click()
           
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

        # 滾動到「確定繳交」按鈕並點擊
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'確定送出')]"))
        ).click()
        time.sleep(2)
        if "繳交成功" in driver.page_source:
            print("\033[32m繳交問卷調查成功\033[0m")
        else:
            print("\033[31m繳交問卷調查失敗\033[0m")

        # # 回列表
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'返回列表')]"))
        ).click()
        # load_dotenv()
        # base_url = os.getenv("BASE_URL")
        # driver.get(f"{base_url}/moocs/#/material/school-qtn")

        # 已作答
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'已作答')]"))
        ).click()    
        time.sleep(2)   
        icon_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//mat-icon[@svgicon='common:done']"))
        )

        # 判斷元素是否具有 "common:done" 的 svgicon
        if icon_element.get_attribute("svgicon") == "common:done":
            print("\033[32m問卷歸類到已完成\033[0m")
        else:
            print("\033[31m問卷未歸類到已完成\033[0m")
           
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