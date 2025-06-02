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

def course_score(driver):
    try:
        print("測試：學習環境-學習成績")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='tab' and contains(., '學習成績')]"))
        ).click()
        time.sleep(2)
        if "成績名稱" in driver.page_source and "成績來源" in driver.page_source:
            print("\033[32m進入學習成績成功\033[0m")
        else:
            print("\033[31m進入學習成績失敗\033[0m")

        # # 觀看
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-expansion-panel-header-18']/span/table/tbody/tr/td[6]/button"))
        # ).click()
        # print("觀看成績落點")
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-expansion-panel-header-18']/span/table/tbody/tr/td[6]/button"))
        # ).click()  

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