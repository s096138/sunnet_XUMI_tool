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

def test_footer(driver):
    try:
        print("測試：首頁-頁尾分享")
        scroll_bottom(driver)
        time.sleep(2)
        share_list = ["facebook", "twitter", "line"]
        for share in share_list:
            if f"{share}商標圖示(另開新視窗)" in driver.page_source:
                print(f"\033[32m有{share}分享圖示\033[0m")
                try:
                    driver.find_element(By.XPATH, f"//img[@alt='{share}']").click()
                    time.sleep(5)
                    handles = driver.window_handles
                    for handle in handles:
                        if handle != driver.current_window_handle:
                            driver.switch_to.window(handle)
                            driver.close()
                    driver.switch_to.window(handles[0])
                    print(f"\033[32m點擊{share}圖示成功\033[0m")
                except ElementClickInterceptedException as e:
                    print(f"\033[31m點擊{share}圖示失敗: {e}\033[0m")
                    pass
            else:
                print(f"\033[31m沒有{share}圖示\033[0m")
        
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