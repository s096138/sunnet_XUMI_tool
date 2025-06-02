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

def test_study_record(driver):

    try:
        print("測試：首頁-會員專區-學習紀錄") 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[span/text()='學習紀錄']"))
        ).click()
        time.sleep(2)
        if "課程名稱" in driver.page_source and "上課次數" in driver.page_source and "討論次數" in driver.page_source and "最後上課時間" in driver.page_source and "閱讀時數" in driver.page_source:
            print("\033[32m進入學習紀錄成功\033[0m")
        else:
            print("\033[31m進入學習紀錄失敗\033[0m")

        # 觀看
        load_dotenv()
        base_url = os.getenv('BASE_URL')
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > cgust-root:nth-child(3) > div:nth-child(2) > cgust-my-learning:nth-child(3) > cgust-common-layout:nth-child(1) > section:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > mat-accordion:nth-child(1) > mat-expansion-panel:nth-child(1) > mat-expansion-panel-header:nth-child(1) > span:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(1)'))
        ).click()  
        time.sleep(2)
        img_element = driver.find_element(By.XPATH, "(//img[@class='record-detail__icon'])[1]")
        # actual_src = img_element.get_attribute('src')
        # print(f"img 的 src 屬性值為: {actual_src}")
        # image_url = f"{base_url}/moocs/assets/images/learning/badge_info.svg"
        if "未閱讀" in driver.page_source:
            print("\033[32m列表展開成功\033[0m")
        else:
            print("\033[31m列表展開失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > cgust-root:nth-child(3) > div:nth-child(2) > cgust-my-learning:nth-child(3) > cgust-common-layout:nth-child(1) > section:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > mat-accordion:nth-child(1) > mat-expansion-panel:nth-child(1) > mat-expansion-panel-header:nth-child(1) > span:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(1)'))
        ).click()    
        print("\033[32m列表收合成功\033[0m")  

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