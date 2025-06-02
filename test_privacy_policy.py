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
import time

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

def test_privacy_policy(driver):
    try:
        print("測試：首頁-隱私權宣告")
        scroll_bottom(driver)
        time.sleep(2)
        if "隱私權宣告" in driver.page_source:
            print("\033[32m滾動到隱私權宣告成功\033[0m")
        else:
            print("\033[31m滾動到隱私權宣告失敗\033[0m")

        # 點擊
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'隱私權宣告')]"))
        ).click()
        time.sleep(2)
        if "個人資料之蒐集政策" in driver.page_source and "個人資料蒐集之運用政策" in driver.page_source:
            print("\033[32m進入隱私權宣告成功\033[0m")
        else:
            print("\033[31m進入隱私權宣告失敗\033[0m")

        # 回首頁
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        print('回首頁')  

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

