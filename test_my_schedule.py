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
import time
import os
from dotenv import load_dotenv

load_dotenv()

def test_my_schedule(driver):
    try:
        print("測試：首頁-會員專區-我的課表")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[span/text()='我的課表']"))
        ).click()
        time.sleep(2)
        if "課程名稱" in driver.page_source and "開課期間" in driver.page_source:
            print("\033[32m點擊我的課表成功\033[0m")
        else:
            print("\033[31m點擊我的課表失敗\033[0m") 

        # 進入課程
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{course_name}')]"))
        ).click()
        time.sleep(2)
        if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//header[contains(text(),'{course_name}')]"))
        ):
            print("\033[32m進入課程成功\033[0m")
        else:
            print("\033[31m進入課程失敗\033[0m")

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
