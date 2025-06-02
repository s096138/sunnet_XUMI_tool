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
from menu_expanded import menu_expanded_with_sibling   
import time

def teacher_hw_correct(driver):
    try:
        print("測試：辦公室-作業管理-作業批改")
        menu_expanded_with_sibling(driver, "作業管理", "作業批改")
        time.sleep(2)
        if "作業一" in driver.page_source and "改完" in driver.page_source:
            print("\033[32m進入作業批改成功\033[0m")
        else:
            print("\033[31m進入作業批改失敗\033[0m")

        # 批改
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@value='批改'])[1]"))
        ).click()        
        time.sleep(5)
        if "請點選左側所列學員" in driver.page_source:
            print("\033[32m進入批改成功\033[0m")
        else:
            print("\033[31m進入批改失敗\033[0m")

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