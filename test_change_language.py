from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException,
)
from selenium_driver import initialize_driver
import time

def test_change_language(driver):
    try:
        print("測試：首頁-切換語系")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='地球圖示']//*[name()='svg']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='English(EN)']"))
        ).click()
        time.sleep(2)
        if "Sitemap" in driver.page_source and "Latest News" in driver.page_source:
            print("\033[32m切換英文語系成功\033[0m")
        else:
            print("\033[31m切換英文語系失敗\033[0m")

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='地球圖示']//*[name()='svg']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'简体中文(中)')]"))
        ).click()
        time.sleep(2)
        if "网站导览" in driver.page_source and "常见问题" in driver.page_source:
            print("\033[32m切換簡體中文語系成功\033[0m")
        else:
            print("\033[31m切換簡體中文語系失敗\033[0m")
            
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='地球圖示']//*[name()='svg']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'繁體中文(中)')]"))
        ).click()
        time.sleep(2)
        if "網站導覽" in driver.page_source and "常見問題" in driver.page_source:
            print("\033[32m切換繁體中文語系成功\033[0m")
        else:
            print("\033[31m切換繁體中文語系失敗\033[0m")

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
    return driver
